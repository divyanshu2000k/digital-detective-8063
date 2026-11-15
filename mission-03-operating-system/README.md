# Mission 3 - Understand the Operating System

## 1. Task / objective
Inspect operating system details, active processes, storage usage, file paths, and owner permissions, and summarize core OS responsibilities.

## 2. Work completed
* Explored OS kernel details, active user session, disk space usage, and live process snapshots using privacy-safe redaction.
* Explained processes, PIDs, absolute vs. relative paths, and `rwx` file permission bits.
* Completed the six-part operating system responsibilities table with concrete examples.

## 3. Commands / tools used
* `uname -srm` — Displayed OS kernel name, version, and CPU architecture.
* `whoami` — Checked the active user account identity (redacted in notes).
* `df -h` — Displayed mounted filesystem capacity, used space, and available storage.
* `ps aux` / `top` — Listed running processes and their Process IDs (PIDs).
* `ls -l` — Inspected file permission strings (`-rw-r--r--`).

## 4. My understanding
### Task 3.1 — Exploring the Operating System
| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| Operating system / system details | Identifies the OS kernel, release version, and hardware architecture. | Unix-like OS running on 64-bit (`arm64` / `x86_64`) architecture. |
| Current account identity | Shows which user account owns the current shell session and its privileges. | Active standard user: `[redacted]` (non-root). |
| Available and used storage | Reports total disk size, used space, free space, and mount points. | Root filesystem `/` showed healthy free capacity in GiB (`df -h`). |
| System activity snapshot | Shows currently executing programs, CPU/memory load, and process states. | Multiple background daemons and user terminal/editor processes active. |

### Task 3.2 — Understanding Processes
* **What is a process?** A process is an active instance of a program loaded into memory and being executed by the CPU, complete with its own memory space and system resources.
* **What does the PID column represent?** PID stands for **Process Identifier**—a unique integer assigned by the OS kernel to track, schedule, and manage each running process.
* **Two examples of running processes:** A shell process (`zsh` or `bash`) handling terminal commands, and a web browser or code editor process (`Code` / `Safari`).

### Task 3.3 — Paths and Permissions
* **Absolute vs. Relative Path:** An **absolute path** starts from the root directory (`/`) and uniquely locates a file regardless of your current directory (e.g., `/Users/[redacted]/digital-detective-xxxx/mission-03-operating-system/README.md`). A **relative path** starts from your current working directory (e.g., `./mission-03-operating-system/README.md` or `../README.md`).
* **Owner Permissions:** Inspecting `terminal-practice/notes.txt` with `ls -l` showed `-rw-r--r--`. The first three permission characters for the owner are `rw-`, meaning the owner can **read** and **write** the file, but cannot **execute** it as a program.

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| `r` - Read | Allows a file's contents to be read (or a directory's contents to be listed). | Opening a text file with `cat notes.txt`. |
| `w` - Write | Allows a file's contents to be modified (or files created/deleted in a directory). | Editing and saving `README.md`. |
| `x` - Execute | Allows a file to be run as a program; on a directory, allows entering (`cd`) into it. | Running a script like `./script.sh`. |

### Task 3.4 — Operating-System Responsibilities
| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Schedules CPU time across running programs, creates/terminates processes, and handles multitasking. | Switching smoothly between Terminal and a web browser while code runs. |
| **Memory management** | Allocates and frees RAM for active processes while keeping process memory isolated. | Allocating RAM buffers to Python when running a script and reclaiming it on exit. |
| **Device management** | Communicates with hardware peripherals using device drivers and I/O queues. | Sending keystrokes from a USB/built-in keyboard to the active window. |
| **File management** | Organizes data into hierarchical directories, files, and metadata on storage drives. | Storing mission folders and tracking permissions on the SSD filesystem. |
| **User interface / shell** | Provides a way for users to interact with the OS via graphical windows or a command-line shell. | Typing commands into `zsh`/`bash` in Terminal or clicking icons in Finder. |
| **Security and permissions** | Enforces user authentication and file access rules so unauthorized users cannot alter system data. | Preventing standard user accounts from modifying `/System` files without privileges. |

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
* `mission-03-operating-system/README.md`

## 8. Commit details
* **Commit message:** `Document operating system and file management`
* **Status:** Committed and pushed to GitHub on `main`.
