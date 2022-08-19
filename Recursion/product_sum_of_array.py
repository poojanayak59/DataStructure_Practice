def product_sum(b):
    xproduct = 1   # O(1)
    xsum = 0       # O(1)
    for i in b:     # O(n)
        xproduct *= i
    for j in b:     # O(n)
        xsum += j
    print(f"{xsum}\n{xproduct}")    # O(1)


# Runtime complexity is O(n)
b = [5, 4, 10, 8]
product_sum(b)
