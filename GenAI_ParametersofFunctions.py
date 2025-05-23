def greet_user(name):#function that takes in a name variable and displays a greetings message with that name
    print("Greetings " + str(name) + " how are you doing today?")

def add_numbers(x,y):#function that takes in 2 ints as a parameter and returns their sum
    return (x+y)

userName = str(input("What is your name: "))#prompts user for name
greet_user(userName)#calling function and passing user input as parameter
num1 = int(input("Enter two numgers to add: "))#prompting for 1st number
num2 = int(input("And now the second number: "))# prompting for 2nd number

print("The sum of "+ str(num1) + " and " + str(num2) + " is " + str(add_numbers(num1,num2)))#prints the returned value form the add numbers function by passing the 2 user inputs and casting that to string to concat