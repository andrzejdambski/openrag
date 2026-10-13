from __future__ import annotations

from core.config import load_config


def test_prompt_refresh_defaults_to_on_and_can_be_disabled(monkeypatch, tmp_path):
    (tmp_path / "config.yaml").write_text(
        "retriever:\n  type: single\nreranker:\n  provider: infinity\nwebsearch:\n  provider: staan\n"
    )
    monkeypatch.delenv("PROMPTS_REFRESH_DEFAULTS", raising=False)
    assert load_config(config_path=tmp_path).prompts.refresh_defaults is True

    monkeypatch.setenv("PROMPTS_REFRESH_DEFAULTS", "false")
    assert load_config(config_path=tmp_path).prompts.refresh_defaults is False


def test_web_query_budget_defaults_to_one_and_can_be_configured(monkeypatch, tmp_path):
    import pytest
    from pydantic import ValidationError

    (tmp_path / "config.yaml").write_text("websearch:\n  provider: staan\n")
    monkeypatch.delenv("WEBSEARCH_MAX_QUERIES", raising=False)
    assert load_config(config_path=tmp_path).websearch.max_queries == 1
    monkeypatch.setenv("WEBSEARCH_MAX_QUERIES", "3")
    assert load_config(config_path=tmp_path).websearch.max_queries == 3
    for invalid in ("0", "9"):
        monkeypatch.setenv("WEBSEARCH_MAX_QUERIES", invalid)
        with pytest.raises(ValidationError):
            load_config(config_path=tmp_path)
