def sum_of_digits(n):
    assert n >=0, 'Sum of digit function only accepts positive integer value'
    if n in range(0, 10):
        # Single digit number is always that number
        return n
    else:
        return int((n % 10) + sum_of_digits(n / 10))
        # Remainder (%) is always 1 digit,
        # Dividend is 2 digits so we re-call function again


n = int(input())
print(sum_of_digits(n))
