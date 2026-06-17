# How to drive this demo (click-by-click)

This is the hands-on companion to `README.md`. Follow it in order and you'll
watch a Pull Request go through the full pipeline.

---

## Step 0 — One-time: create the empty repo on GitHub

Log in as **ameer-obe** and create a **new, empty** repository named
`pipeline_demo` (no README, no .gitignore — we already have those).
Easiest at: https://github.com/new

You'll land on a page that shows a URL like:
`https://github.com/ameer-obe/pipeline_demo.git`

---

## Step 1 — Push the code (run these from the project folder)

```powershell
cd C:\Users\AShaik\pipeline_demo

# point this local repo at your new GitHub repo
git remote add origin https://github.com/ameer-obe/pipeline_demo.git

# push main (the stable branch) and set it as the default upstream
git push -u origin main

# push the feature branch that contains the new power() function
git push -u origin feature/add-power
```

The first push will pop a browser/credential prompt — log in as ameer-obe.

> After this, open the repo's **Actions** tab. The `push` to `main` already
> triggered the **CI** and **Deploy (simulated)** workflows once. Watch them run.

---

## Step 2 — Open the Pull Request (this is the moment you asked about)

1. Go to the repo on GitHub. A yellow banner will offer
   **"Compare & pull request"** for `feature/add-power` — click it.
   (Or: **Pull requests** tab → **New pull request** →
   base: `main`, compare: `feature/add-power`.)
2. Give it a title (e.g. *"Add power() operation"*) and click
   **Create pull request**.

The instant the PR is created, **`ci.yml` runs against the proposed merge.**

---

## Step 3 — Watch the pipeline on the PR

Scroll to the bottom of the PR page. You'll see a checks box that updates live:

```
Some checks haven't completed yet
  ◐ CI / Lint (flake8 + black)
  ◐ CI / Test (Python 3.9)
  ◐ CI / Test (Python 3.10)
  ◐ CI / Test (Python 3.11)
  ◐ CI / Test (Python 3.12)
  ◐ CI / Build artifact        (waits for lint + test)
```

- Click **Details** next to any check to see the live log of every step.
- `lint` and the four `test` jobs run in **parallel**.
- `build` only starts after they all pass (because of `needs: [lint, test]`).
- When all are ✅ green, the PR becomes mergeable.

Open the **Actions** tab too — the same run is shown there as a job graph.

---

## Step 4 — Merge, and watch deployment fire

Click **Merge pull request** → **Confirm merge**.

Merging adds a commit to `main`, which triggers:
- **CI** again (verifying main itself), and
- **Deploy (simulated)** — open it in Actions to see the 🚀 deploy log.

That's the complete loop: **branch → PR → CI checks → merge → deploy.**

---

## Step 5 (optional but very instructive) — make CI go RED

Want to *see* the pipeline catch a bug? On a new branch, break a test:

```powershell
git checkout main
git checkout -b feature/break-it
# edit calculator/operations.py so add() returns a - b   (wrong on purpose)
git commit -am "Intentionally break add()"
git push -u origin feature/break-it
```

Open a PR. The `test` jobs will fail ❌, the PR will show it can't be safely
merged, and the logs will point at exactly which assertion failed. Fix it,
push again, and watch the same PR turn green — re-runs happen automatically
on every new push to the branch.

---

## Step 6 (optional) — require checks before merge (branch protection)

To make green CI *mandatory* before anyone can merge to `main`:

**Settings → Branches → Add branch ruleset (or rule) for `main`** →
enable **"Require status checks to pass before merging"** and select the
`CI` checks. Now a red pipeline physically blocks the merge button — this is
how real teams keep `main` always-working.
