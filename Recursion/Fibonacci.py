def fibonacci(n):
    assert n >= 0, 'Enter positive integer number only'
    if n in [0, 1]:  # ----------                       ---O(1)
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # -----O(2^n)  -O(Branches ^ depth)


n = int(input())
print(fibonacci(n))
"""
f=0 1 2 3 4 5 6 7  8  9  10 11 12
  0 1 1 2 3 5 8 13 21 34 55 89 144 
"""
