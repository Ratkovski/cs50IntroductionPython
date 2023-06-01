students = ["Hermione", "Harry", "Ron"]

##1

# print(students[0])
# print(students[1])
# print(students[2])


##2
# for student in students:
#     print(student)

##3
# for i in range(len(students)):
#     print(i + 1, students[i])

##4
# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])
#
# for student in students:
#     print(student , students[student], sep=", ")

## 5

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
