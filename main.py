print("Replit Login System")
print()

name = ""
password = ""
boole = False


def password():
    name = input("What is your username?: ")
    password = input("what is your password?: ")
    if name == "david" and password == "baldies4life":
        print()
        print("Welcome to Replit!")
        global boole
        boole = True
    else:
        print()
        print(
            "Whoops! I don't recognize that username or password. Try again!")


while not boole:
    password()
