#how to create a class.
#We do that by using the key word class and then give a name
class User:
    pass #This makes so that the class or any block not empty so that the code works fine

#Although the class User right now has no attributes or functionality, we can still add attributes to it and it will still work
#First we create our object:
user1 = User()
#And then we can add attributes to this class and it will work fine.
user1.id = 1
user1.name = "Long"

print(user1.name)
print(user1.id)
#But what if we have to create a second user. And then a third and then more
user2 = User()
user2.id = 2
user2.username = "Someone"
#This is a completely valid but as we can see, we assign name for user1 and then username for user2
#This can lead to confusion and overall we can have lots of more mistakes made
#And the least, it is tedious and painful to keep writing and add attributes like this
#So how can we make it easier
#We do that by knowing what a Constructor is. In programming we know that as initializing as well.
# In python we create Constructors with the special form called __init__. It has two underscore infront and behind the name so it means it is a special method
# NOTE: Everytime we create and Object, then the __init__ method will always initialize.
# Inside the __init__ function we will always have 'self' as a parameter and after that we can specify as many parameters as we want
# SO it will look something like this: def __init__(self, <par1>, <par2>, ...)
# Inside the __init__ function block we will assign the parameters so it will look like this
# def __init__(self, a, b, c)
#     self.a = a
#     self.b = b
#     self.c = c
# and then when we create and object we can initialize the objects with some variables.
# my_object = <class_name>(my_a, my_b, my_c)
# the upper line of code works as we do this
# my_object.a = my_a
# my_object.b = my_b
# my_object.c = my_c


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Long", 23)
print(f"{person1.name} is {person1.age}")
#Mind that initializing attributes like originally wont work.
# person2 = Person()
# person2.name = "Someone"
# person2.aage = 23
# print(f"{person2.name} is {person2.aage}")

# In python we can set default values as well
# for example we can have something like this
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.followers = 0
# making self.followers = 0 is completely legit and it just means that it won't take any parsing, instead it will just take default initialization when the object is created.
#and then we can print or work with that default attribute.


#in classes we can define methods as well.
class MySocialMedia:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.followers = 0

    def get_follower(self):
        print(f"{self.name} got a follower")
        self.followers += 1


my_social_media_user = MySocialMedia("Long", 23)
print(f"{my_social_media_user.name} is {my_social_media_user.age} and has {my_social_media_user.followers} followers.")
my_social_media_user.get_follower()
print(f"{my_social_media_user.name} is {my_social_media_user.age} and has {my_social_media_user.followers} followers.")

#as we can see the from the method we need to specify which followers are we adding on to
#so that is why for a parameter of the method we declare 'self'
#self by it self means that when we talk about an object, when being called then it will change ITSELF
#actually: ALL METHODS in fact NEED TO HAVE A PARAMETER, unlike functions.
