number = int(input("Enter you number:"))
def palindrome(n):
    revNum = 0  
    dup = n  

    while n > 0:
        ld = n % 10  
        n //= 10
    
    return dup == revNum  
    
if palindrome(number): 
        print(f"{number} is a palindrome.")
else:
        print(f"{number} is not a palindrome.")