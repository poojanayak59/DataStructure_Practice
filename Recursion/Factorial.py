def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)


# Runtime complexity is O(n)

n = int(input())
print(factorial(n))
