
##1
# for _ in range(3):
#     print("#")

##2

# def main():
#     print_column(3)
# def print_column(height):
#     for _ in range(height):
#      print("#")
#
# main()


##3

# def main():
#     print_row(4)
# def print_row(width):
#  print("?" * width)
#
# main()


###4

# def main():
#     print_square(3)
# def print_square(size):
#     # For each row in square
#     for i in range(size):
#         # For each brick in row
#         for j in range(size):
#             # Print brick
#             print("#", end="")
#         print()
#
# main()


###5

# def main():
#     print_square(3)
# def print_square(size):
#     for i in range(size):
#             print("#" * size)
#
# main()


### 6

def main():
    print_square(3)
def print_square(size):
    for i in range(size):
            print_row(size)

def print_row(width):
    print("#" * width)

main()