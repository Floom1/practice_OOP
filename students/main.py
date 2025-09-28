from students import Student
from group import Group


students = []
with open("students/in.txt", "r") as f:
    try:
        for line in f:
            parts = line.strip().split(' ')
            if len(parts) == 3:
                st = Student(parts[0], parts[1], parts[2])
                students.append(st)

    except:
        print("Oops")

groups = []
with open("students/in2.txt", "r") as f:
    try:
        for line in f:
            parts = line.strip().split(' ')
            if len(parts) == 1:
                gr = Group(parts[0])
                groups.append(gr)

    except:
        print("Oops")
# print(groups[0])



print(len(groups[0]), groups[0] == groups[1])

groups[0] = groups[0] + students[0]
groups[0] += students[1]
print(len(groups[0]), groups[0] == groups[1])
print(groups[0])

with open("out.txt", "w") as f:
    try:
        for group in groups:
            f.write(str(group) + "\n")
    except Exception as e:
        print(f"Oops {e}")
