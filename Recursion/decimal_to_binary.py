def decimal_to_binary(n):
    assert n >= 0, 'Decimal to Binary function allows positive integers only'
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimal_to_binary(int(n/2))


n = int(input())
print(decimal_to_binary(n))
