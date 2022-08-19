def print_pairs(a, b):
    for i in range(0, len(a)):                 # O(a)
        for j in range(0, len(b)):             # O(b)
            for k in range(0, 100000):              # O(1) - 100,000 is constant work not looping thru any array
                print(f"{a[i]} , {b[j]}")           # O(1)


# Runtime complexity is O(ab)
a = [1, 2, 6, 7]
b = [5, 4, 10, 8]
print_pairs(a, b)
