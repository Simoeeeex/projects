import re
import string
import random

COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "111111", "123123", "iloveyou", "admin", "letmein"
]

def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return any(c.isupper() for c in password)

def check_lowercase(password):
    return any(c.islower() for c in password)

def check_digits(password):
    return any(c.isdigit() for c in password)

def check_special_chars(password):
    special_chars = string.punctuation
    return any(c in special_chars for c in password)

def check_common(password):
    return password.lower() not in COMMON_PASSWORDS

def score_password(password):
    score = 0
    if check_length(password): score += 1
    if check_uppercase(password): score += 1
    if check_lowercase(password): score += 1
    if check_digits(password): score += 1
    if check_special_chars(password): score += 1
    if check_common(password): score += 1
    return score

def strength_level(password):
    score = score_password(password)
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score == 5:
        return "Strong"
    else:
        return "Very Strong"

def suggestions(password):
    tips = []
    if not check_length(password):
        tips.append("Use at least 8 characters (stronger ≥12).")
    if not check_uppercase(password):
        tips.append("Add uppercase letters.")
    if not check_lowercase(password):
        tips.append("Add lowercase letters.")
    if not check_digits(password):
        tips.append("Add digits.")
    if not check_special_chars(password):
        tips.append("Add special characters like !@#$%.")
    if not check_common(password):
        tips.append("Avoid common passwords.")
    return tips

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

