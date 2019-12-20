def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

def isPalindrome(n):
    global rev
    res = False
    if rev == n:
        res = True
        return res
    return res
    

n = 123
rev = reverse(n)
res = isPalindrome(n)
print()