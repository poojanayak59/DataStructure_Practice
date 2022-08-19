def find_largest(a):
    biggest_value = a[0]  # ------------------O(1)-----O(n) (remove non dominant)----------------O(n)
    for index in range(1, len(a)):  # --------O(n)
        if a[index] > biggest_value:  # ------O(1)-----2(O(1) = O(1) (remove constant)-->2(O(1) =O(1)------> O(n) (ND)
            biggest_value = a[index]  # ------O(1)
    print(biggest_value)  # ------------------O(1)------------->O(1)


def find_largest_recursion(b, n):  # ------------------M(n)
    if n == 1:  # n is size of array b  # ------------------O(1)--------------->O(1)
        return b[0]  # ------------------O(1)
    else:
        return max(b[n-1], find_largest_recursion(b, n-1))  # ------------------M(n-1)----------M(n-1)


"""
M(n) = O(1) + M(n-1)
M(1) = O(1) when n = 1
M(n) = 1 + M(n-1)
     = 1 + (O(1) + (M(n-1) -1))
     = 1 + (1 + (M(n-1) -1))
     = 2 + M(n-2)
     .........pattern says we moving to next set of n in backward direction so replace 2 with n-1
     = n-1 + M(n-(n-1))
     = n-1 + 1
     = n 
"""
a = [5, 4, 10, 8, 11, 68, 87]
find_largest(a)
b = [5, 4, 10, 8, 95, 11, 68, 87]
print(find_largest_recursion(b, 8))
