from password_utils import check_length, check_uppercase, check_lowercase, check_digits, check_special_chars, check_common, score_password, strength_level

def test_passwords():
    passwords = [
        "123",          # Weak
        "password",     # Weak (common)
        "Hello123",     # Medium
        "Strong!Pass1", # Strong
        "V3ry$tr0ngPwd!" # Very Strong
    ]

    for pwd in passwords:
        print(f"Password: {pwd}")
        print(f" - Strength: {strength_level(pwd)}")
        print(f" - Score: {score_password(pwd)}\n")

if __name__ == "__main__":
    test_passwords()

