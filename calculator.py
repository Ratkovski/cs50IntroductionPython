#x = input("What's x? ")
# y = input("What's y? ")

# z = int(x) + int(y)
#
# print(z)
#####################################
# x = float(input("What's x? "))
# y = float(input("What's y? "))
#
# #z = round(x + y)
# #print(f"{z:,}")
#
# #z = round(x / y, 2)
# z = round(x / y)
#
# print(f"{z:.2f}")

#####################

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    #return  n * n
    return pow(n,2)

main()

