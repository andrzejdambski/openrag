# PR #1161 review measurements

The October 9 prompt evaluation and held-out checks are in the linked result files. The direct follow-up below addresses Andy’s current UI, latency, recall, and nit comments.

## October 12 live comparison

The bundled contextualizer now validates in the admin UI, including both uses of `max_query_subqueries`. We tested the UI against the actual bundled template.

For latency, `develop` (`db7f6c66`) and candidate (`d9db441e`) each ran in a fresh Compose project with branch-specific prompt seeds and storage. Both indexed the same two research PDFs. We replayed the same three comparison questions three times per revision, using streamed one-token replies and excluding one warm-up request per revision. Median TTFT was **3.82 s on develop** and **4.17 s on the candidate** (+0.35 s / 9.2% in this run). This small sample does not support a latency-improvement claim.

For source recall on the same two papers, both revisions retrieved both relevant PDFs for both prior example questions (2/2 each). On three new comparisons over the five supplied `mini-data` PDFs, `develop` retrieved 6/6 relevant source files and the candidate retrieved 5/6 (0.83). The candidate missed the soybean document on one comparison. This is a small source-level sample, not a general recall claim.

The evaluator and production retry now share the same over-cap instruction. The stale query-cap comment is corrected.

Validation: 300 focused Python tests and 435 UI tests passed; Ruff check, Ruff format check, and `git diff --check` passed.

Detailed evidence: [label evaluation](results/andy_review_labels_20261009.json), [full prompt run](results/andy_review_full_summary_20261009.json), [October 9 recall](results/andy_review_recall_20261009.json), [October 9 latency](results/andy_review_latency_20261009.json), [current recall comparison](results/andy_review_recall_20261012.json), and [current TTFT comparison](results/andy_review_latency_20261012.json).
