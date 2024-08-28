def is_palindrome(s: str):
    s = s.lower()  
    is_palindrome = s == s[::-1]  
    

    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return is_palindrome, frequency

result = is_palindrome("Radar")
print(result)