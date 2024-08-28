def is_prime(n: int):
    if n <= 1:
        return []
    
    
    divisors = [(n % i == 0, i) for i in range(2, int(n**0.5) + 1)]
    
    return divisors


result = is_prime(11)
print(result)