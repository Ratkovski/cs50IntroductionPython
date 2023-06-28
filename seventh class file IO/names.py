#1

# names = []
#
# for _ in range(3):
#     names.append(input("What's your name?"))
#
# for name in sorted(names):
#     print(f"hello, {name}")

# 2

# name = input("What's your name?")
# #file = open("names.txt", "w") # write sobescreve o antigo
# file = open("names.txt", "a") #append
# file.write(f"{name}\n")
# file.close()


# 3 write
# name = input("What's your name?")
# #file = open("names.txt", "w") # write sobescreve o antigo
# with open("names.txt", "a") as file: #with supoe que ja close
#     file.write(f"{name}\n")


# 4 read line by line
with open("names.txt", "r") as file:
    for line in file:
        # print(line, end="")
        print("hello, ", line.rsplit())


# 5 read all lines
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rsplit())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")
