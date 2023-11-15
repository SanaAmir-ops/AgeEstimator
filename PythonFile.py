from datetime import datetime

def calculate_age(birthdate):
    # Assuming birthdate is in the format 'YYYY-MM-DD'
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

if __name__ == "__main__":
    user_dob = input("Enter your date of birth (YYYY-MM-DD): ")
    age = calculate_age(user_dob)
    print(f"Your age is: {age} years.")
