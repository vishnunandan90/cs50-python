# Taking inout from user
name = input("What is your Name? ")
# Stripping the white spaces and capitalizing the first letter of the name.
# Similarly there are other functions like lower(), upper(), title() etc.
name  = name.strip().capitalize()

#Formatted string, notice the f before the string
print(f"hello, {name}")
# Using the + operator
print("hello, " + name)
# Using the sep (separator, by default it is ' ') and end (by default it is '\n') parameters
print("hello, " + name, end="?????")
print("hello,", name, sep=" ")

# Splitting the name into first and last name
first,last = name.split(" ")
print("hello, " + first )
