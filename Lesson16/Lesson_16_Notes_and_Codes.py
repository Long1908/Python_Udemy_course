#In this lesson we are going to talk about OOP.
#What is Object Oriented Programming
    # Basically it is dividing the code to smaller chunks and put them in differet
    # programming files. Those programming files then we can connect into one big
    # project. That is how we divide our code into logical files so we can easily
    # search, refracture, expand and so on and so forth

#The one thing about OOP is that we can have different Classes.
#Classes are structures that are the blueprint or foundation of Objects
#that have similiar attributes, functionality and etc.
# For Example: Let's say we have a Class 'Student'. Now we can create
# people such as Henry, Betty, ... that all are students

#In the past we have seen how we import modules, that are basically
# other python files that we include in our code, to get their functionality.
#That will be the premise of how we divide our code to different files and then
# combine them, by simply importing them

import example_module
print(example_module.example_variable)
#NOTE: notice how to use the variable that is saved in the 'example_module' we
#      specify what module/file we are talking about and then we can tap in the content
#      content of that file.

#when we import modules and then specify what we want to use from that module
# we will see each name what it represents. For example functions and methods will be
# represented as f, classes we will see are c
# and variables are v.

#Let's see how we can create an object.
#For this we will use a premade module called turtle
import turtle
#To create a an object from a class from this module, we essentially create a variable
# in our starting file, and then we specify it be constructed with the "blue print" of the class
# For example: if we had class called Cars()
#               Then we will create a car like Audi = Cars().
#               Essentially Audi is now created as a structure of data taht represents some kind of
#               attributes and functionality that the class Cars() have.
#In our case for the turtle
my_turtle = turtle.Turtle()
#Again as above, we need to specify which module are we talking about and then we can tap in the
#content of said module.
#another way to do it is to specify a single thing from a module
# Let's say we don't want to use the whole turtle module but we want to use only a specific class.
# we can do so by writing:
# from turtle import Turtle.
# that way now we can write my_turtle = Turtle() without specifying what module are we talking about.
# and we can import not one but many different things from a single module
from turtle import Turtle, Screen
my_screen = Screen()
#now we can tap in the Object and change it's attributes that are ofcourse the corresponding attributes that
# the blueprint of the class.
my_screen.canvheight #as we can see we tap an attribute from the class by typing dot (.)
print(my_screen.canvheight)
#in addition we can also tap in from the object not only the attributes but the methods as well
my_turtle.shape("turtle")
my_turtle.color("green")
my_turtle.forward(100)
my_screen.exitonclick()
#In the top 4 lines that we have just written, we can see that we used two different objects to
# work together. As we can see we gave my_turtle attributes and some kind of functionality.
# and then we displayed that in our object my_screen


#Now we have already seen how we can import modules, but that is only cause these modules are
# ready to use after we download PyCharm. In reality there are many many Python codes that we cannot
# access, unless we download the Packages. And installing Packages is not like importing modules.
# All the Packages that we can download we can access through this page: https://pypi.org/
# How to download a package:
#     1. go to Files
#     2. go to Settings
#     3. Go to the Project:<Name_of_the_project>
#     4. Go to Project Interpeter
#     5. Click on the plus sign (+)
#     6. On the bar for searching write down the name of the package that is in PyPi
#     7. Click install
#     8. After we have installed it, we can import it. In this case we have already installed the package PrettyTable
from prettytable import PrettyTable
# if we want to see the source code of any imported module, we can click on the line where we implemented the module
#     1. right click on it
#     2. click on Go To
#     3. click on Implementation
# PyPi with the name of the packages, have a documentation of what we can do with the module and how to do it.
table = PrettyTable()
print(table)
# we will continue showing this new package functionality in a new file called pokemon_table