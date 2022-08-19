if __name__ == '__main__':
    N = int(input())
    my_list = []
    cmd = []
    for i in range(1, N + 1):
        cmd = input().split(" ")
        if cmd[0] == 'insert':
            final = "my_list." + str(cmd[0]) + "(" + str(cmd[1]) + ", " + str(cmd[2]) + ")"
            exec(final)
        elif cmd[0] == 'print':
            print(my_list)
        elif cmd[0] == 'remove':
            final = "my_list." + str(cmd[0]) + "(" + str(cmd[1]) + ")"
            exec(final)
        elif cmd[0] == 'append':
            final = "my_list." + str(cmd[0]) + "(" + str(cmd[1]) + ")"
            exec(final)
        elif cmd[0] == 'sort':
            my_list.sort()
        elif cmd[0] == 'pop':
            my_list.pop()
        elif cmd[0] == 'reverse':
            my_list.reverse()



