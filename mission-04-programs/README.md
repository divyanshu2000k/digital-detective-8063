# Mission 4 - How Programs Run

## 1. Task / objective
Create and run a basic Python 3 script (`hello.py`) from the Terminal and compare how compilers and interpreters translate and execute code.

## 2. Work completed
* Created `mission-04-programs/hello.py` to print `"Hello from Python"`.
* Executed the script using `python3` in Terminal and verified the output.
* Built a side-by-side comparison table and written explanation of compilers vs. interpreters.

## 3. Commands / tools used
* `python3 mission-04-programs/hello.py` — Invoked the Python 3 interpreter to execute the source file.
* `git add` & `git commit` — Committed `hello.py` and Mission 4 documentation.

## 4. My understanding
### Task 4.2 — Compiler vs. Interpreter Comparison
| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the entire source code into machine code *before* the program runs (ahead of time). | Translates and executes source code line-by-line (or via bytecode) *at runtime*. |
| **Typical output** | Produces a standalone binary executable file (e.g., `.exe` or Mach-O binary). | Produces no standalone executable; directly outputs program results during execution. |
| **One example** | C / C++ (`gcc` or `clang`) | Python (`python3`) or Ruby |
| **One advantage** | Faster runtime execution because translation is already complete before launch. | Easier cross-platform portability and rapid testing without a separate build step. |

A **compiler** reads the entire program upfront, checks for syntax/type errors across all files, and generates a standalone machine-code executable that runs directly on the CPU at high speed. In contrast, an **interpreter** reads and executes instructions dynamically while the program is running, which means you can run scripts like `hello.py` immediately without compiling first. While compiled programs typically execute faster in production, interpreted languages offer quicker iteration and portability wherever the interpreter is installed.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
* `mission-04-programs/hello.py`
* `mission-04-programs/README.md`

## 8. Commit details
* **Commit message:** `Compare compilers and interpreters`
* **Status:** Committed and pushed to GitHub on `main`.
