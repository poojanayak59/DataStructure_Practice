def recursive_method(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursive_method(n - 1)
        print(n)


user_input = input("Enter a number of your choice\n")
n = int(user_input)
recursive_method(n)
