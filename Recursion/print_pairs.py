def print_pairs(b):
    for i in b:                 # O(n^2)
        for j in b:             # O(n)
            print(f"{i},{j}")    # O(1)


# Runtime complexity is O(n^2)
b = [5, 4, 10, 8]
print_pairs(b)

