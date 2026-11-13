# Four-Function Calculator

A calculator built together by the club. Each role owns one file.

## How the pieces fit

```
 User types "3 + 4 * 2" in the GUI
        │
        ▼
 tokenizer.py   →  [3.0, "+", 4.0, "*", 2.0]
        │
        ▼
 evaluator.py   →  11.0   (uses operations.py for the math)
        │
        ▼
 GUI shows 11
```

## Roles

| Role | Level | File | Your tests |
|------|-------|------|------------|
| Basic Functions | Simple | `calculator/operations.py` | `tests/test_operations.py` |
| Multi Input Handling | Medium | `calculator/tokenizer.py` | `tests/test_tokenizer.py` |
| Order of Operations | Medium | `calculator/evaluator.py` | `tests/test_evaluator.py` |
| App GUI | Medium | `calculator/gui.py` | run `python main.py` and click around |
| Integration & Testing | Simple | `main.py`, `tests/` | `tests/test_calculate.py` |

Open your file - the comment at the top explains exactly what to build.

## Setup

```powershell
python -m venv .venv               # only once
.venv\Scripts\Activate.ps1         # every time you open a new terminal
pip install -r requirements.txt    # after cloning, and whenever requirements.txt changes
```

If you add a library, add it to `requirements.txt` with a version (e.g. `PySide6==6.8.1`).

## Running

```powershell
python main.py                                 # launch the calculator
python -m unittest                             # run ALL tests
python -m unittest tests.test_operations       # run just your tests
```

All tests fail at the start - that's expected! Your role is done when your tests pass.
