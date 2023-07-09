class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
            # sys.exit("Missing name")

        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "horse"
            case "Otter":
                return "shoe"
            case "Jack Russell Terrier":
                return "dog"
            case _:
                return "fizzle"


def main():
    student = get_student()
    # if student[0] == "Padma":
    #     student[1] = "Rvenclaw"

    # if student["name"] == "Padma":
    #     student["house"] = "Rvenclaw"
    #
    # # name = get_name()
    # # house = get_house()
    # print(f"{student[0]} from {student[1]}")
    # print(f"{student['name']} from {student['house']}")
    # print(f"{student.name} from {student.house}")
    print("Expecto Patronum")
    print(student.charm())


# def get_house():
#     return input("House: ")
#
#
# def get_name():
#     return input("name: ")


def get_student():
    # name = input("Name:")
    # house = input("House:")
    # return [name, house]

    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student
    # return {"name": name, "house": house}

    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    # return student

    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    student = Student(name, house, patronus)
    return student


if __name__ == "__main__":
    main()
