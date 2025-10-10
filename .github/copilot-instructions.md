## Purpose

This repository is a small, local collection of Python learning exercises (scripts and notebooks). The goal of these instructions is to help an AI coding agent be immediately productive fixing small bugs, improving examples, and adding low-risk improvements (docs, small refactors, tests).

## Big-picture architecture (what to know)

- Flat exercise structure: top-level folders `basic_02/` and `basic_03/` contain independent Python scripts and Jupyter notebooks. There is no package, server, or CI configured.
- Each file is usually a self-contained example or exercise (e.g., `basic_02/list_1.py`, `basic_02/input_1.py`, `basic_03/set.ipynb`). Treat files as standalone snippets rather than library modules.

## Key files and directories

- `Read.md` — repo purpose (learning/python basics).
- `basic_02/` — many small `.py` scripts (day-based subfolders like `day-2/`, `day-3/`). Example: `basic_02/day-2/loop-1.py`.
- `basic_03/` — example notebooks (`*.ipynb`) and more exercises (e.g., `basic_03/set.ipynb`).

## Developer workflows (how to run and verify changes)

- Run a single script with the local Python interpreter: `python <relative-path-to-file>` (assume Python 3.8+). Example: `python basic_02/list_1.py`.
- Open notebooks in VS Code or Jupyter to run cells interactively. Do not try to run all notebooks in CI (they are examples).
- There is no test runner, package manifest, or virtualenv config. If you add third-party dependencies, also add a `requirements.txt` and brief README instructions.

## Project-specific conventions & patterns

- File names use lowercase underscore style and are standalone examples (e.g., `user_define_function.py`, `return_func_from_func.py`).
- Many scripts print output directly and use `input()` for interactive examples (`input_1.py`). When editing, avoid breaking interactive behavior without noting it.
- Notebooks are used as teaching examples. Preserve cell ordering and avoid changing `metadata.id` values in notebook cells.

## Common issues to look for (examples found)

- Small syntax issues or stray quotes can appear in notebook cell source during editing. Example file to inspect: `basic_03/set.ipynb` (cells demonstrate set/dict examples).
- Print-only scripts may benefit from returning values for testability (small refactors are welcome).

## What AI agents should do first (concrete, low-risk tasks)

- Fix small syntax bugs and typos in scripts and notebooks. Run the modified script or notebook cell locally to confirm no SyntaxError.
- Convert an example script to a small function + simple CLI guard when it improves reuse, e.g. add:

- Add a tiny pytest when the change makes functions testable; keep tests minimal and place them next to the file in a new `tests/` folder.

## What not to change without human sign-off

- Do not reorganize the repository into a package or change the top-level layout. These are student exercises and the structure reflects lesson order.
- Do not run large-scale automated transformations across notebooks (risk of breaking teaching intent).

## PR/commit guidance

- Keep changes small and focused. Example commit messages: `fix: correct syntax in basic_03/set.ipynb cell`, `chore: add requirements.txt for new dependency`.

## Useful references in this repo

- Example script: `basic_02/list_1.py` — quick look at script style and prints.
- Notebook: `basic_03/set.ipynb` — demonstrates typical notebook content and common edit surfaces.

If anything in this file is unclear or you want the agent to prefer different behaviors (for example, always add tests, or adopt a strict formatting/linting step), tell me and I will update this guidance.
