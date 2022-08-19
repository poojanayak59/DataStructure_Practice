if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    avg = 0.00
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a = 0.00
    for s in student_marks[query_name]:
        a += s
        avg = a / 3
    print(student_marks[query_name])
    print("{:.2f}".format(avg))

"""
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
"""
