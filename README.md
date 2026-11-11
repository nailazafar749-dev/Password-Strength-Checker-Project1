# Password Strength Checker 🔐

**DecodeLabs Cyber Security Internship | Project 1 (Batch 2026)**

A simple Python program that checks whether a password is Weak, Medium, or Strong, and gives suggestions to improve it.

**Features**

- Checks password length (less than 8 characters = Weak)
- Checks for uppercase letters, lowercase letters, numbers and symbols
- Detects common / leaked passwords (e.g. `password`, `123456`)
- Estimates password entropy (in bits)
- Gives suggestions to make the password stronger
- Password input is hidden while typing (using `getpass`)

 **Requirements**

- Python 3.9 or higher
- No external libraries needed (uses only the standard library)

 **How to Run**

```bash
python project1.py
```
Then type a password and press Enter.

 **Example**

| Password | Result |
|---|---|
| `abc` | WEAK |
| `Hello@123` | MEDIUM |
| `MyS3cure#Pass2026!` | STRONG |

**How It Works**

1. Input: the user enters a password.
2. Process: the program scans the password once (linear scan, O(n)) and checks length, character types, and the common-password list. Entropy is estimated as `length x log2(character pool size)`.
3. Output: the program prints a report with the strength result and suggestions.

Security Notes
- The program never stores or saves the password anywhere.
- Passwords in a real system should be hashed (e.g. with Argon2id) and never stored as plain text.

 **Screenshots**

<img width="277" height="218" alt="image" src="https://github.com/user-attachments/assets/8d16b425-08af-477d-81b6-eb600aace040" />
<img width="252" height="175" alt="image" src="https://github.com/user-attachments/assets/3ea8dc0b-2935-407d-aad6-a720f9a1b728" />

**Skills Practiced**
String handling, conditional logic, security basics, input validation.

 **Author**

Made by Naila Zafar as part of the DecodeLabs Industrial Training Kit.
