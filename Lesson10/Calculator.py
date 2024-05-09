def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
num1 = input('Enter first number: ')
while not num1.isnumeric():
    print("Your enter was not a number. Please try again.")
    num1 = input('Enter first number: ')
num1 = float(num1)
do_Calculation = True
while do_Calculation:
    my_operation = input('Enter operation (+, -, *, /): ')
    while my_operation not in ["+", "-", "*", "/"]:
        print('Invalid operation. Please try again.')
        my_operation = input('Enter operation (+, -, *, /) : ')
    num2 = input('Enter second number: ')
    while not num2.isnumeric():
        print("Your enter was not a number. Please try again.")
        num2 = input('Enter second number: ')
    num2 = float(num2)
    function = operations[my_operation] #-->WOOOOOOOOOOOOW
    result = function(num1, num2) #--> WOOOOOOOOOOW. This helps us not use if and else so many times.
    print(f"Your result is: {result}")
    calculate = input("Would you like to continue? (y/n)")
    while calculate not in ["y", "n"]:
        print('Invalid option. Please try again.')
        calculate = input("Would you like to continue? (y/n)")
    if calculate == 'y':
        do_Calculation = True
        num1 = result
    else:
        do_Calculation = False


print('Thank you for using my calculator!')