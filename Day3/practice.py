num = int(input("Enter a number:"))
def palindrome(n):
    revNum = 0  
    dup = n  
    while n > 0:
        ld = n % 10  
        revNum = (revNum * 10) + ld 
        n //= 10 
    return dup == revNum  

if palindrome(num):  
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
