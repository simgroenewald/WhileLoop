# Compulsory Task 2

# Initialise variables as empty strings
classList = "" 
name = ""


# While loop that runs as long as the string entered is not stop
while name != "STOP":
    name = input("Enter student name:") # Prompts user to enter a name and stores it as a variable
    name = name.upper() # Changes the string to uppercase
    if name != "STOP": # If statement to determine if stop was entered
        classList = classList + "\n" + name # If name is not stop it is added to the class list string
print(classList)

