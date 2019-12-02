# Compulsory Task 1

num = 0 # used for initial calculation where 0 is needed
num1 = 0 # used to start initial loop
count = 0 # used as a counter for the dennominator for the average calculation

# While the num1 does not equal -1 this loop will run (it is initiall a 0 therefore it will start)
while num1 != -1:
    num1 = int(input("Please enter a number:")) # Prompts user to enter a number
    if num1 != -1: # If the number is not -1 the loop will run
        num = num + num1 # This will add each consecutive number entered and num will have a new value
        count +=1 # Used to update the counter everytime a successfull number was entered
print (num/count) # This will print out once the loop breaks
    
    
    



