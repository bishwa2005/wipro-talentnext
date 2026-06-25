records = {}

n = int(input("Enter number of students: "))

for _ in range(n):
    student = input("Student Name: ")
    marks = list(map(float, input("Enter 3 marks: ").split()))
    records[student] = marks

search_name = input("Enter name to search: ")

if search_name in records:
    avg = sum(records[search_name]) / len(records[search_name])
    print(f"Average percentage mark: {avg:.2f}")
else:
    print("Student not found.")