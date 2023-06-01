### 1

# i = 3
# while i != 0:
#     print("meow")
#     i = i - 1


### 2

# i = 0
# while i < 3:
#     print("meow")
#     #i = i + 1
#     i += 1

### 3

# for i in [1,2,3]:
#     print("meow")

# ### 4

# for i in range(3):
#     print("meow")

### 5
#
# for _ in [1,2,3]:
#     print("meow")

### 6

#print("meow\n" * 3, end="")

### 7

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break
#
# for _ in range(n):
#     print("meow")

### 8

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n ?"))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()