
#Demo of a simple function that returns a value

def main():
    x = int(input("What is X? "))
    print("Square of", x, "is", square(x))

def square(x):
    return x*x

main()