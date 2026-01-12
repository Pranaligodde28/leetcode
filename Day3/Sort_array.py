
def isSorted(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False
    return True 

arr = [1, 2, 9, 4, 5]
n = len(arr)

ans = isSorted(arr, n)

if ans:
    print("True")
else:
    print("False")
