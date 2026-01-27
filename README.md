
# Password Strength Checker

A simple, robust Python CLI tool to evaluate password strength based on length and character variety.

## Features
- **Interactive CLI**: Continuously checks passwords until you exit.
- **Detailed Feedback**: Tells you exactly *why* a password is weak (e.g., "Missing numbers").
- **Clear Classification**: valid classification into **Weak**, **Medium**, or **Strong**.

## Classification Logic

| Strength | Criteria |
| :--- | :--- |
| **Weak** | Length < 8 characters **OR** contains fewer than 3 different character types. |
| **Medium** | Length >= 8 characters **AND** contains exactly 3 different character types. |
| **Strong** | Length >= 8 characters **AND** contains all 4 character types (Uppercase, Lowercase, Numbers, Special). |

**Character Types Checked:**
1. Uppercase Letters (A-Z)
2. Lowercase Letters (a-z)
3. Digits (0-9)
4. Special Characters (!@#$...)

## Installation & Usage

1. **Prerequisites**: Python 3.x installed.
2. **Run the tool**:
   ```bash
   python password_checker.py
   ```
3. **Run Tests**:
   ```bash
   python -m unittest test_password_checker.py
   ```

## Example Run

```text
--- Password Strength Checker ---
Type 'q' or 'quit' to exit.
------------------------------

Enter a password to check: password123
Strength: WEAK
Feedback:
 - Password needs more variety (at least 3 different character types).
 - Missing character types: uppercase letters, special characters.

Enter a password to check: P@ssword1
Strength: STRONG
Feedback:
 - Excellent! Your password meets all strength criteria.
```
