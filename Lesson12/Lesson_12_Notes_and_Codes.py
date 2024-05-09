#On this lesson we are going to talk about scope
#Namely we are gonna talk about the difference between Global and Local scope

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}") ##This will print 2 enemies

increase_enemies()
print(f"enemies inside function: {enemies}") #This will however print 1 enemy
#That is because the the 'enemies' variable in the function is Local scope
#Meaning that it cannot be seen by funcitons or variables outside the scope

#Global functions is what we define outside and every function or block of code can access
#We can be aware of the scope of the variable, by the lebel of the identation

#There is a difference however between Python and other programming languages like C++
#The difference is that special form such as 'if', 'for' and etc. do notcount as creating a local scope
#Only creating a function counts as creating a new scope.
#So if we create a variable within an if or for we can access that variable

if True:
    enemy_multiplier = enemies
print(f"enemy multiplier: {enemy_multiplier * 2}")

#But if we define a variable within a function
#Then that variable is local only for the function
#NOTE: How we explicitly said that the if is True. Why?
#Because if that line is not True then we don't go into the if statement body
#Which means that the variable "enemy_multiplier" will not be created.
#Which means that it will return error when we try to access that variable.
#THIS IS VERY IMPORTANT THE LAST THREE LINES ABOVE

def my_function():
    my_variable = 2

#print(f"my variable = {my_variable}") #this has an error


#How we can access change the global variables in functions?
#If we look at the code below

my_num = 1
print(my_num)
# def my_add_one():
#     my_num += 1
#This will return error, cause the line my_num += 1 is searching for variables WITHIN the scope.7
#Notice that doesn't mean we cannot access the global scope, it just says that we cannot change it
#in the conventional way.
#However we can do this

def my_add_one_v2():
    global my_num
    my_num += 1
my_add_one_v2()
print(my_num)
#The code above will change the code.
#NOTE: However it is practically accepted that we should not change golbal scopes
#Cause that can break our code that access that global variable in multiple funtions

#Another way to change our global variables is by returning it.

def my_add_one_v3():
    return my_num + 1
my_num = my_add_one_v3()
print(my_num)

#In Python there is not special form 'constant' that can fixate a value toa variable
#What instead is used, is Python provides us a Capitalized naming convention method.
#Any variable written in the Upper case is considered as a Constant in Python.
#CONSIDERED, practically it can be changed, but let say if we work in a project with a team,
#we DO NOT change that variable.
