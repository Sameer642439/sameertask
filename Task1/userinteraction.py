from Task1.Palindrome import is_palindrome
from Task1.errorhandle import get_integer_input
from Task1.prime import is_prime


def main():
    results = []
    
    user_string = input("Enter a string to check if it is a palindrome: ")
    palindrome_result = is_palindrome(user_string)
    
    user_number = get_integer_input("Enter a number to check if it is prime: ")
    if user_number is not None:
        prime_result = is_prime(user_number)
    else:
        prime_result = []
    
    
    result = {
        "input_string": user_string,
        "palindrome_check": palindrome_result,
        "input_number": user_number,
        "prime_check": prime_result
    }
    results.append(result)
    
    
    print("Results:", results)


main()