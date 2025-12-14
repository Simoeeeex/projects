from password_utils import strength_level, suggestions, generate_password

def main():
    print("=== Password Strength Analyzer ===\n")
    while True:
        password = input("Enter a password (or 'exit' to quit): ")
        if password.lower() == "exit":
            print("Exiting Password Strength Analyzer.")
            break

        level = strength_level(password)
        print(f"\nPassword Strength: {level}")

        tips = suggestions(password)
        if tips:
            print("Suggestions to improve your password:")
            for tip in tips:
                print(f"- {tip}")
        else:
            print("Your password is strong!")

        print("\nDo you want a strong random password? (y/n)")
        choice = input().lower()
        if choice == 'y':
            new_password = generate_password()
            print(f"Generated strong password: {new_password}")
        
        print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    main()

