def power(base, expo):
    assert base and expo >= 0, 'Power function allows positive integers only'
    if expo == 0:
        return 1  # x^0 =1
    elif expo == 1:
        return base  # x^1 = X
    else:
        return base * power(base, expo - 1)  # x^n = x * x^n-1

# Runtime complexity is O(2^n)

base = int(input())
expo = int(input())
print(power(base, expo))
