# dict = {}

# name = input("Enter your name: ")
# language = input("Enter your fav language: ")

# dict.update({name : language})

# print(dict)

def entry():
    dict = {}
    while True:
        name = input("Enter name: ")
        language = input("Enter their fav language: ")
        dict.update({name : language})

        option = input("Do you want to enter more value? (y/n): ").lower()

        if option == "n":
            print(dict.items())
            break
            
entry()
