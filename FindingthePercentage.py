n = int(input())
students_marks = {}
for _ in range(n):
    line = input().split()
    names, scores = line[0], (line[1:])
    students_marks[names] = scores
query = input()

list1 = [float(i) for i in students_marks[query]]

print("{0:.2f}".format(sum(list1)/3))

