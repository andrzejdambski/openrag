from unittest.mock import AsyncMock, Mock

import pytest
from services.persistence.connection import ConnectionManager
from sqlalchemy.exc import IntegrityError


class RDBConfigStub:
    host = "db"
    port = 5432
    user = "root"
    password = "root_password"
    database = "partitions_for_collection_test"
    auto_create_database = True
    pool_min_size = 1
    pool_max_size = 4
    command_timeout = 10


def test_ensure_database_exists_creates_missing_database(monkeypatch):
    manager = ConnectionManager(RDBConfigStub())
    create_database = Mock()

    monkeypatch.setattr("sqlalchemy_utils.database_exists", lambda url: False)
    monkeypatch.setattr("sqlalchemy_utils.create_database", create_database)

    manager._ensure_database_exists()

    create_database.assert_called_once()


def test_ensure_database_exists_skips_existing_database(monkeypatch):
    manager = ConnectionManager(RDBConfigStub())
    create_database = Mock()

    monkeypatch.setattr("sqlalchemy_utils.database_exists", lambda url: True)
    monkeypatch.setattr("sqlalchemy_utils.create_database", create_database)

    manager._ensure_database_exists()

    create_database.assert_not_called()


def test_ensure_database_exists_tolerates_concurrent_creation(monkeypatch):
    manager = ConnectionManager(RDBConfigStub())
    database_exists = Mock(side_effect=[False, True])
    create_database = Mock(
        side_effect=IntegrityError(
            "CREATE DATABASE partitions_for_collection_test",
            {},
            Exception("duplicate key value violates pg_database_datname_index"),
        ),
    )

    monkeypatch.setattr("sqlalchemy_utils.database_exists", database_exists)
    monkeypatch.setattr("sqlalchemy_utils.create_database", create_database)

    manager._ensure_database_exists()

    assert database_exists.call_count == 2
    create_database.assert_called_once()


def test_ensure_database_exists_reraises_if_create_fails_and_database_is_missing(monkeypatch):
    manager = ConnectionManager(RDBConfigStub())
    database_exists = Mock(side_effect=[False, False])
    create_error = IntegrityError(
        "CREATE DATABASE partitions_for_collection_test",
        {},
        Exception("permission denied"),
    )
    create_database = Mock(side_effect=create_error)

    monkeypatch.setattr("sqlalchemy_utils.database_exists", database_exists)
    monkeypatch.setattr("sqlalchemy_utils.create_database", create_database)

    with pytest.raises(IntegrityError) as exc_info:
        manager._ensure_database_exists()

    assert exc_info.value is create_error
    assert database_exists.call_count == 2


@pytest.mark.asyncio
async def test_initialize_skips_database_creation_when_auto_create_is_disabled(monkeypatch):
    class NoCreateDBConfig(RDBConfigStub):
        auto_create_database = False

    manager = ConnectionManager(NoCreateDBConfig())
    ensure_database_exists = Mock()
    create_pool = AsyncMock(return_value=object())

    monkeypatch.setattr(manager, "_ensure_database_exists", ensure_database_exists)
    monkeypatch.setattr("services.persistence.connection.asyncpg.create_pool", create_pool)

    await manager.initialize()

    ensure_database_exists.assert_not_called()
    create_pool.assert_awaited_once()
