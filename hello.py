
#function is like an action or a verb that lets you do something in the program
#arguments is a n input to a function
# quando é imprimido algo na tela conhecido como side effects
############################################33
#Ask user for their name
#name = input("what's your name?").strip().title()
#print("Hello,", name)

# Remove whitespace from str and capitalize user's name
#name = name.strip().title()

#Capitalize user's name
#name = name.capitalize()
#name = name.title()

#Say hello to user
#print(f"Hello, {name}")
##################################3
# def hello(to="world"):
#     print("hello,", to)
#
# hello()
# name = input("what's your name?")
# hello(name)


def main():
    name = input("what's your name?")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()