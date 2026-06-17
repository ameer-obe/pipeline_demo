# pipeline_demo

A deliberately tiny Python project whose real purpose is to **teach you how a
GitHub Actions CI/CD pipeline works, end to end.** The "app" is a 4-function
calculator. Everything interesting is in the pipeline.

---

## 1. What's in this repo

```
pipeline_demo/
├── calculator/              # the "application" code
│   ├── __init__.py
│   └── operations.py        # add, subtract, multiply, divide
├── tests/
│   └── test_operations.py   # pytest tests the pipeline runs
├── .github/workflows/       # ← THE PIPELINE LIVES HERE
│   ├── ci.yml               # runs on every Pull Request to main
│   └── deploy.yml           # runs after a merge to main (simulated deploy)
├── requirements-dev.txt     # tools the pipeline installs (pytest, flake8, black)
├── pyproject.toml           # shared config so local == CI
└── .gitignore
```

GitHub treats **any `.yml` file under `.github/workflows/`** as a pipeline.
That folder is the only "magic" — everything else is normal code.

---

## 2. The core idea: CI vs CD

| | When it runs | Question it answers | File |
|---|---|---|---|
| **CI** (Continuous Integration) | On every Pull Request | "Is this change safe to merge?" | `ci.yml` |
| **CD** (Continuous Deployment) | After merge to `main` | "Ship the merged change" | `deploy.yml` |

So the lifecycle you'll watch is:

```
 you push a branch  ─►  open PR to main  ─►  CI runs (lint, test, build)
        │                                          │
        │                                   all green? ✅
        ▼                                          ▼
   make fixes  ◄── red ❌ ── CI re-runs ──►  merge the PR  ─►  Deploy runs on main 🚀
```

---

## 3. How `ci.yml` is structured

A **workflow** contains **jobs**; each job contains **steps**.

- **Trigger (`on:`)** — this workflow fires on `pull_request` to `main`,
  on `push` to `main`, and via a manual button (`workflow_dispatch`).
- **Job `lint`** — checks formatting (`black`) and style (`flake8`).
- **Job `test`** — runs `pytest` on a **matrix** of Python 3.9–3.12.
  A matrix clones the same job once per version and runs them in parallel.
- **Job `build`** — `needs: [lint, test]`, so it only starts once both pass,
  then packages the code and uploads it as a downloadable **artifact**.

Key vocabulary you'll see in the YAML:

- `runs-on: ubuntu-latest` — a fresh, throwaway VM GitHub gives you for free.
- `uses:` — pull in a prebuilt action (e.g. `actions/checkout@v4`).
- `run:` — execute a shell command, exactly like typing it in a terminal.
- `needs:` — declare job order/dependencies.
- `${{ ... }}` — a GitHub Actions expression (e.g. the matrix value).

Jobs run **in parallel** by default; `needs:` is how you force order.

---

## 4. Run the pipeline's checks locally (optional)

Everything CI does, you can do on your machine first:

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows PowerShell
pip install -r requirements-dev.txt

black --check .                  # formatting
flake8 . --max-line-length=88    # linting
pytest --cov=calculator          # tests + coverage
```

If those pass locally, they'll pass in CI — that's the whole point of the
shared `pyproject.toml`.

---

## 5. Watching it run on GitHub

1. Open the **Actions** tab of the repo — every run is listed here.
2. Click a run to see the three jobs as a graph (`lint`, `test`, `build`).
3. Click any job to expand each step's live log output.
4. On a Pull Request, the same checks appear at the bottom as ✅/❌ status checks.
5. After merging, watch the **Deploy (simulated)** workflow fire on `main`.

See `LEARN.md` (or the "How to drive this demo" section your assistant gave
you) for the exact click-by-click PR walkthrough.
