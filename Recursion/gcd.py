def gcd(a, b):
    assert a and b >= 0, 'Power function allows positive integers only'
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


a = int(input())
b = int(input())
print(gcd(a, b))
