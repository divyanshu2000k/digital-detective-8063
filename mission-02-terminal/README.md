# Mission 2 - Become Comfortable with the Terminal

## 1. Task / objective
Practice core command-line navigation and file management inside a safe sandbox folder, understand command flags and pipes, and inspect a package manager.

## 2. Work completed
* Tested directory navigation, file creation, copying, moving, and inspection commands.
* Created `terminal-practice/` to test overwriting (`>`) vs. appending (`>>`) and safe file backups.
* Compared standard `ls` output against `ls -lah` and combined `ls -l` with `head` using a pipe (`|`).
* Checked package manager version and installed packages safely without modifying system software.

## 3. Commands / tools used
* `pwd`, `ls`, `ls -l`, `ls -lah`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`, `head` — Core POSIX file and directory utilities.
* `|` (Pipe operator) — Redirects standard output of one command into standard input of the next.
* `brew --version` & `brew list` — Inspected the Homebrew package manager status.

## 4. My understanding
### Task 2.1 — Basic Terminal Operations
| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| Current-directory display (`pwd`) | Prints the full absolute path of the current working directory. | Displayed `/Users/[redacted]/digital-detective-...` |
| Directory listing (`ls`) | Lists visible files and folders in the current directory. | Showed all mission folders and `README.md`. |
| Detailed listing (`ls -l`) | Displays permissions, owner, file size in bytes, and modification date. | Listed each item on its own line with metadata. |
| Change directory (`cd ..`) | Moves the shell session up one level to the parent directory. | `pwd` changed to the parent folder path. |
| Create directory (`mkdir`) | Creates a new empty folder at the specified path. | Created `terminal-practice` without errors. |
| Create empty file (`touch`) | Creates a zero-byte file or updates its timestamp if it exists. | Created an empty `notes.txt` file. |
| Copy file (`cp`) | Duplicates a file to a new path while keeping the original intact. | Both original and copied files existed side by side. |
| Move / rename file (`mv`) | Moves a file to a new directory or renames it in place. | Renamed `notes-copy.txt` to `notes-backup.txt`. |
| Display file contents (`cat`) | Reads a file and prints its text contents directly to the terminal. | Printed both lines stored inside `notes.txt`. |

### Task 2.2 — Safe File Practice Questions
* **Replacing vs. adding text:** Using `>` truncates (overwrites) the file before writing new text, whereas `>>` appends new text to the end of the file while preserving existing lines.
* **Copying vs. moving a file:** `cp` creates an independent duplicate leaving the source file untouched; `mv` relocates or renames the original file so only one copy remains.
* **Current-directory display (`pwd`):** Shows your exact location in the directory tree from the root (`/`), preventing accidental edits in the wrong folder.
* **Why directory listing (`ls`) is useful:** Lets you immediately verify file names, folder structure, hidden files, and permissions directly from the keyboard.

### Task 2.3 — Flags and Pipes
* **Flags (`ls` vs. `ls -lah`):** Plain `ls` shows only non-hidden names in columns. Adding `-l` switches to long metadata format, `-a` reveals hidden dotfiles (like `.git`), and `-h` formats file sizes into human-readable units (`B`, `K`, `M`).
* **Pipes (`ls -l | head -n 5`):** The pipe symbol (`|`) connects the standard output (`stdout`) of `ls -l` directly to the standard input (`stdin`) of `head -n 5`. `ls -l` generates the full detailed file list, and `head -n 5` filters that stream to display only the first 5 lines.

### Task 2.4 — Package Managers
Package managers (such as Homebrew on macOS or `apt` on Ubuntu) automate downloading, verifying, installing, updating, and removing command-line tools and libraries from trusted repositories. They automatically resolve software dependencies so tools work without manual compilation or path configuration.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
* `mission-02-terminal/README.md`
* `terminal-practice/notes.txt`
* `terminal-practice/notes-backup.txt`

## 8. Commit details
* **Commit message:** `Complete Terminal and file management mission`
* **Status:** Committed and pushed to GitHub on `main`.
