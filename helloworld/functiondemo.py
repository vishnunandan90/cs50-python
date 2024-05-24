def main():
    name = input("What is your Name? ")
    hello(name)
    hello()

def hello(name="World"):
    print("Hello,",name)

main()



