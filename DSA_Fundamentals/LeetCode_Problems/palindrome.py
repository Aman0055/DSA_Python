# check the palindrome of a string :

def is_palindrome(n : int) -> bool:
    if n < 0 or (n % 10 == 0 and n != 0):
        return False
    reversed_half = 0
    while n > reversed_half:
        reversed_half = reversed_half * 10 + n % 10
        n //= 10
    return n == reversed_half or n == reversed_half // 10

print(is_palindrome(121)) 
print(is_palindrome(-121))
print(is_palindrome(10))
print(is_palindrome(12321))