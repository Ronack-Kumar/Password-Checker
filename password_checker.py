
import string
import sys

def check_password_strength(password):
    """
    Checks the strength of a password based on length and character types.
    
    Args:
        password (str): The password to check.
        
    Returns:
        dict: A dictionary containing:
            - 'strength': 'Weak', 'Medium', or 'Strong'
            - 'feedback': A list of feedback strings explaining the rating.
            - 'criteria_met': A list of criteria that were met.
    """
    
    # Criteria flags
    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    # Collect met criteria for detailed reporting
    criteria_met = []
    if length_ok: criteria_met.append("Length >= 8")
    if has_upper: criteria_met.append("Uppercase")
    if has_lower: criteria_met.append("Lowercase")
    if has_digit: criteria_met.append("Digit")
    if has_special: criteria_met.append("Special Char")

    # Count character type criteria (excluding length for the count logic as per requirement)
    # Logic: 
    #   Weak: Length < 8 OR < 3 character types
    #   Medium: Length >= 8 AND 3 character types
    #   Strong: Length >= 8 AND 4 character types
    type_criteria_count = sum([has_upper, has_lower, has_digit, has_special])
    
    strength = "Weak"
    feedback = []

    if not length_ok:
        feedback.append("Password is too short (must be at least 8 characters).")

    # Determine missing types for feedback
    missing = []
    if not has_upper: missing.append("uppercase letters")
    if not has_lower: missing.append("lowercase letters")
    if not has_digit: missing.append("numbers")
    if not has_special: missing.append("special characters")
    
    if missing:
        feedback.append(f"Missing character types: {', '.join(missing)}.")

    # Classification Logic
    if length_ok:
        if type_criteria_count == 4:
            strength = "Strong"
            feedback = ["Excellent! Your password meets all strength criteria."]
        elif type_criteria_count == 3:
            strength = "Medium"
            feedback.append("Consider adding the missing character type for a Strong rating.")
        else:
            strength = "Weak" # Met length but not enough variety
            feedback.append("Password needs more variety (at least 3 different character types).")
    
    return {
        "strength": strength,
        "feedback": feedback,
        "criteria_met": criteria_met
    }

def main():
    """
    Main function to run the password checker in an interactive loop.
    """
    print("--- Password Strength Checker ---")
    print("Type 'q' or 'quit' to exit.")
    print("-" * 30)

    while True:
        try:
            user_input = input("\nEnter a password to check: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break

        if user_input.lower() in ('q', 'quit'):
            print("Goodbye!")
            break
        
        if not user_input:
            print("Please enter a non-empty password.")
            continue

        result = check_password_strength(user_input)
        
        print(f"\nStrength: {result['strength'].upper()}")
        print("Feedback:")
        for note in result['feedback']:
            print(f" - {note}")

if __name__ == "__main__":
    main()
