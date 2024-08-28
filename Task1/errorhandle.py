def get_integer_input(prompt: str):
    errors = []
    for _ in range(3):  
        try:
            user_input = input(prompt)
            if not user_input.isdigit():
                raise ValueError("Invalid input. Please enter a valid integer.")
            return int(user_input)
        except ValueError as e:
            print(e)
            errors.append((user_input, str(e)))
    
    print("Error: Maximum retries reached.")
    print("Logged Errors:", errors)
    return None


user_number = get_integer_input("Enter a number: ")