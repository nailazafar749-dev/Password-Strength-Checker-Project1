"""
Project 1: Password Strength Checker (DecodeLabs - Cyber Security)
 
Checks:
  - Length (< 8 = immediate WEAK)
  - Uppercase, lowercase, digits, symbols
  - Common / leaked passwords
  - Estimated entropy (bits)
Result: Weak / Medium / Strong
"""
 
import getpass
import math
import string
 
MIN_LENGTH = 8
 
# Small sample of commonly leaked passwords (extend this list for your own experiments)
COMMON_PASSWORDS = {
    "123456", "12345678", "123456789", "password", "password1", "qwerty",
    "qwerty123", "abc123", "111111", "letmein", "iloveyou", "admin",
    "welcome", "monkey", "dragon", "football", "login", "passw0rd",
    "p@ssw0rd", "admin123", "pakistan", "india123",
}
 
 
def analyze(password: str) -> dict:
    """Scan the password once and collect which character types it uses."""
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
 
    # Entropy estimate = length * log2(size of character pool)
    pool = 0
    if has_lower:
        pool += 26
    if has_upper:
        pool += 26
    if has_digit:
        pool += 10
    if has_symbol:
        pool += len(string.punctuation)
    entropy = len(password) * math.log2(pool) if pool else 0
 
    return {
        "length": len(password),
        "upper": has_upper,
        "lower": has_lower,
        "digit": has_digit,
        "symbol": has_symbol,
        "common": password.lower() in COMMON_PASSWORDS,
        "entropy": round(entropy, 1),
    }
 
 
def rate(info: dict) -> tuple[str, list[str]]:
    """Return (strength, list_of_suggestions)."""
    tips = []
 
    if info["common"]:
        return "WEAK", ["This is a very common/leaked password. Never use it."]
 
    if info["length"] < MIN_LENGTH:
        return "WEAK", [f"Use at least {MIN_LENGTH} characters."]
 
    score = 0
    if info["length"] >= 12:
        score += 2
    elif info["length"] >= MIN_LENGTH:
        score += 1
 
    for key, label in (
        ("upper", "an uppercase letter (A-Z)"),
        ("lower", "a lowercase letter (a-z)"),
        ("digit", "a number (0-9)"),
        ("symbol", "a symbol (!@#$...)"),
    ):
        if info[key]:
            score += 1
        else:
            tips.append(f"Add {label}.")
 
    if info["length"] < 12:
        tips.append("Make it 12+ characters for a stronger password.")
 
    if score >= 6:
        return "STRONG", tips
    if score >= 4:
        return "MEDIUM", tips
    return "WEAK", tips
 
 
def main() -> None:
    print("=== Password Strength Checker ===")
    # getpass hides what you type on screen
    password = input("Enter password to check: ")

    info = analyze(password)
    strength, tips = rate(info)
 
    print("\n--- Report ---")
    print(f"Length        : {info['length']}")
    print(f"Uppercase     : {'Yes' if info['upper'] else 'No'}")
    print(f"Lowercase     : {'Yes' if info['lower'] else 'No'}")
    print(f"Numbers       : {'Yes' if info['digit'] else 'No'}")
    print(f"Symbols       : {'Yes' if info['symbol'] else 'No'}")
    print(f"Entropy (est) : {info['entropy']} bits")
    print(f"\nStrength      : {strength}")
 
    if tips:
        print("\nSuggestions:")
        for t in tips:
            print(f"  - {t}")
 
    # Don't keep the password around longer than needed
    del password
 
 
if __name__ == "__main__":
    main()
 