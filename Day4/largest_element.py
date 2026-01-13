arr1 = list(map(int, input("Enter numbers").split( ',' )))
def findLargestElement(arr1, n):
    max = arr1[0]

    for i in range(1, n):
        if arr1[i] > max:
         max = arr1[i]
    return max

n = len(arr1)
max = findLargestElement(arr1, n)
print("LArgest Element is:", max)
