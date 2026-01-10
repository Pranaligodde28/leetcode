num = int(input("Enter a num:"))
def romanToInt(num):
    roman_To_Int ={'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000} 
    reult = 0
    while num >= 1000:
        roman += "M"
        num -= 1000

    while num >= 500:
        roman += "D"
        num -= 500

    while num >= 100:
        roman += "C"
        num -= 100

    while num >= 50:
         roman += "L"
         num -= 50

    while num >= 10:
        roman += "X"
        num -= 10

    while num >= 5:
        roman += "V"
        num -= 5

    while num >= 1:
        roman += "I"
        num -= 1

print("Roman number:",roman)