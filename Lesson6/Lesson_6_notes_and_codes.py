#Creating a function is done by using the special form 'def'. After 'def' we write the desire name of our function.
#After that we write brackets, and inside the brackets we can have something or nothing.
#The point of the brackets is that we can have arguments to work inside the function.
#So we can imagine a function is it's own block of code where things there work in it's own enviroment and we expect it to throw somekind of answer at us.
#the function however will not do anything by it self and if want to use it, we need to call it.
#What is important is that we should call it with the right ammount of arguments that it created it.
def my_function(): #Define the function
    print("Hello")
    print("World")

my_function() # Call the function

# we talked about the for loops in the previous module,
# on this module we are going to talk about the while loop.
# The while loop has similiar structure to the for loop
# But it doesn't have a beginning and end. It just have a
# condition. Condition, that until it is met, it will
# keep on doing its' body.