def Ipower_of_2(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power


def Rpower_of_2(n):
    if n == 0:
        return 1
    else:
        power = Rpower_of_2(n-1)
        return power*2


n = int(input())
print(f" Using Recursion {Ipower_of_2(n)}")
print(f" Using Iteration {Rpower_of_2(n)}")
