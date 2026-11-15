# Mission 5 - Numbers and Data

## 1. Task / objective
Perform manual number-base conversions across decimal, binary, and hexadecimal, verify results in Python, build `number_converter.py`, and explain character encoding standards (ASCII and UTF-8).

## 2. Work completed
* Worked through seven manual conversions between decimal, binary, and hexadecimal step by step.
* Verified every manual conversion using Python's built-in `bin()`, `hex()`, and `int(..., base)` functions.
* Created and tested `number_converter.py` with multiple positive integers.
* Documented ASCII values and the role of UTF-8 text encoding.

## 3. Commands / tools used
* `python3` (Interactive REPL & script runner) — Executed conversion checks and ran `number_converter.py`.
* `int()`, `bin()`, `hex()` — Built-in Python functions for integer parsing and base-2 / base-16 string formatting.

## 4. My understanding
### Task 5.1 — Manual Number Conversions
| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary.** | $13 \div 2 = 6$ rem **1**; $6 \div 2 = 3$ rem **0**; $3 \div 2 = 1$ rem **1**; $1 \div 2 = 0$ rem **1**. Reading remainders bottom-to-top: **`1101`** ($8 + 4 + 0 + 1 = 13$). |
| **Convert decimal 25 to binary.** | $25 \div 2 = 12$ rem **1**; $12 \div 2 = 6$ rem **0**; $6 \div 2 = 3$ rem **0**; $3 \div 2 = 1$ rem **1**; $1 \div 2 = 0$ rem **1**. Reading bottom-to-top: **`11001`** ($16 + 8 + 0 + 0 + 1 = 25$). |
| **Convert binary 1010 to decimal.** | $(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0) = 8 + 0 + 2 + 0 =$ **`10`**. |
| **Convert binary 1101 to decimal.** | $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) = 8 + 4 + 0 + 1 =$ **`13`**. |
| **Convert hexadecimal A to decimal.** | In base 16, $A$ represents $10 \times 16^0 =$ **`10`**. |
| **Convert hexadecimal 1F to decimal.** | $(1 \times 16^1) + (15 \times 16^0) = 16 + 15 =$ **`31`**. |
| **Convert binary 1111 to hexadecimal.** | $1111_2 = 8 + 4 + 2 + 1 = 15_{10}$, which corresponds to **`F`** in hexadecimal. |

### Task 5.2 — Python Verification
| Expression tested | Result | Matches manual calculation? |
| :--- | :--- | :--- |
| `bin(13)` | `'0b1101'` | Yes (`1101`) |
| `bin(25)` | `'0b11001'` | Yes (`11001`) |
| `int('1010', 2)` | `10` | Yes (`10`) |
| `int('1101', 2)` | `13` | Yes (`13`) |
| `int('A', 16)` | `10` | Yes (`10`) |
| `int('1F', 16)` | `31` | Yes (`31`) |
| `hex(int('1111', 2))` | `'0xf'` | Yes (`F`) |

### Task 5.3 — Number Converter Test Runs (`number_converter.py`)
* **How the functions work:** `input()` reads user text as a string, `int()` converts that string into a base-10 integer, `bin()` returns its binary string prefixed with `0b`, and `hex()` returns its hexadecimal string prefixed with `0x`.

| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| `13` | `0b1101` | `0xd` |
| `25` | `0b11001` | `0x19` |
| `255` | `0b11111111` | `0xff` |

### Task 5.4 — How Text Is Stored
* **ASCII decimal codes:** Uppercase `'A'` is **`65`** (`01000001` in binary), and lowercase `'a'` is **`97`** (`01100001` in binary).
* **Why encoding standards are needed:** Computer hardware only stores binary digits (`0`s and `1`s), so an encoding standard provides a universal mapping between numeric byte values and human-readable characters across devices.
* **Non-ASCII character example:** The Indian Rupee symbol **`₹`** (or accented letters like **`é`** and emojis like **`🚀`**) requires UTF-8 encoding because standard 7-bit ASCII only covers codes 0–127.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
* `mission-05-numbers-data/number_converter.py`
* `mission-05-numbers-data/README.md`

## 8. Commit details
* **Commit message:** `Build number converter and practise data representation`
* **Status:** Committed and pushed to GitHub on `main`.
