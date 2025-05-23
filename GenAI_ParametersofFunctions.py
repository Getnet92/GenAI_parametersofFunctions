# Task 1
def greet_user(name):#function that takes in a name variable and displays a greetings message with that name
    print("Greetings " + str(name) + " how are you doing today?")

def add_numbers(x,y):#function that takes in 2 ints as a parameter and returns their sum
    return (x+y)

userName = str(input("What is your name: "))#prompts user for name
greet_user(userName)#calling function and passing user input as parameter
num1 = int(input("Enter two numgers to add: "))#prompting for 1st number
num2 = int(input("And now the second number: "))# prompting for 2nd number

print("The sum of "+ str(num1) + " and " + str(num2) + " is " + str(add_numbers(num1,num2)))#prints the returned value form the add numbers function by passing the 2 user inputs and casting that to string to concat

# Task 2
def describe_pet(pet_name, animal_type = "dog"):# function with 2 parameters and one of them has a default of "dog"
    print("I have a " + str(animal_type) + " named " + str(pet_name)  + ". ",end = " ") # print statement with the 2 parameters


describe_pet("Mia") # testing the function with a pet_name since the animal_type already has a default variable


# Task 3
def make_sandwich(*ingredients):#funtion that allows positional arguments because of the * 
    print("Making a sandwich with the following ingredients: ", end = "")
    for i in ingredients:#creating a loop to print out each element of the list with a "-" followed by the element
        print("-" + str(i),end = " ")

make_sandwich("Steak") # test
make_sandwich("Lettuce", "Tomato", "Cheese","Bacon", "Ketchup", "Bread") # test

print(" ")

# Task 4
def factorial(x):
    if x == 0:
        return 1
    else:
        return (x * factorial(x - 1))
    
def fibonacci(y):# logic based on sample output( the 6th factorial being 8)
    if y == 0:# base case
        return 0
    elif y == 1: # base case
        return 1
    else:
        return fibonacci(y-1)+ fibonacci(y-2)#update condition
fact = int(input("What number do you want the factorial to? ")) # prompting to get number to return factorial
print("This is the factorial of " + str(fact) + ": " + str(factorial(fact)))
f = int(input("what number do you want to do the fibonachi of: "))   #prompt to recieve number to calculate nth fibonnacci sequence number
print("This is the fibonachi of  " + str(f)+ " " + str(fibonacci(f)))

