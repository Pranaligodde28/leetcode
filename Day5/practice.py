def fibonacci(N):
    # Base case: if N is 0 or 1, return N
    if N <= 1:
        return N

    # Recursive calls: calculate previous two terms
    last = fibonacci(N - 1)   # (N-1)th term
    slast = fibonacci(N - 2)  # (N-2)th term

    return last + slast

# Driver code
N = 4
print(fibonacci(N))  # Output: 3
