
def palindrome(n):
    revNum = 0  
    dup = n 
    
    while n > 0:
        ld = n % 10  
        revNum = (revNum * 10) + ld  
        n //= 10 

    return dup == revNum 

number = 4645233332546
if palindrome(number): 
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
