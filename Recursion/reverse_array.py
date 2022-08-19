def reverse_array(a):
    for i in range(0, int(len(a) / 2)):     # O(n)
        l = len(a) - i - 1                  # O(1)
        temp = a[i]                         # O(1)
        a[i] = a[l]                         # O(1)
        a[l] = temp
    print(a)


# Runtime complexity is O(n)
a = [1, 2, 6, 7]
reverse_array(a)
