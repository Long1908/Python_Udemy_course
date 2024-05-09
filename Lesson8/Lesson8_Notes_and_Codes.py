#In this will lesson we talk about functions that can accept input.
#And then we are gonna talk about the difference between arguments and parameters.

#basic how creating a function with parameters and then
#calling the function with arguments.
def my_greeting(name):
    print(f"Hello {name}")

my_greeting("Long")
#we can have different functions with 1, 2, ... ,n parameters
#important is that we match the number of arguments when we call a function
#also, other than matching the number of arguments, we have to match
#the order of the arguments with the parameters. It's called Positional argument.
#That however can be fixed by doing this

def my_function(a, b, c):
    print(a, b, c)

my_function(b = 2, c = 3, a = 1) #This way the function will know each argument which parameter is for
#if we it was like this: my_function(2, 3, 1), Then it is gonna parse the arguments one by one to the order of the parameters

