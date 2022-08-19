def print_pairs(b):
    for i in range(0, len(b)):                 # O(n^2)
        for j in range(i+1, len(b)):             # O(n)
            print(f"{b[i]} , {b[j]}")           # O(1)


# Runtime complexity is O(n^2)
b = [5, 4, 10, 8]
print_pairs(b)
