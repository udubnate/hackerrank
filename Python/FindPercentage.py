if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


    def average(query_name):
        current = student_marks[query_name]
        total = 0
        for num in current:
            total += float(num)
        avg = total / len(current)
        print(format(avg,'.2f'))

    average(query_name)


