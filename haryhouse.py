name = input("waht is your name ?")

match name:
    case "Harry":
        print("Griffendor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")