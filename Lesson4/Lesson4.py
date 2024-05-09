import random
import my_module

#imports and how they work. Imports are called 'Python Module'
print(my_module.pi) #after importing our other .pi file, we can then use it

#random whole integer including the lower and upper bound
random_integer = random.randint(1, 10)
print(random_integer)

#random float number, but in this case does not include the bottom or upper bound
random_float = random.random()
print(random_float)

#a good way to increase the both of the bounds of a random.random is by simply multiplying the bounds
random_float2 = random.random() * 5 # this will give everying between 0  and 5, not including 0 and 5
print(random_float2)

#Data structures are a good way to group and store data, that have commonality and it doesn't make sense to store them individually
#First Data structures we can use is List that is basically Arrays for other programming languages
fruits = ["Cheery", "Apples", "Bananas", "Oranges"]
#Then we can easily access them such as we access each letter of a string
print(fruits[0]) #of course be careful of not going out of bound of the list. So the index of the list always start from 0 and then goes to the (length of the list - 1)
#what is powerful about this List data structure is that we can also count from minus indexes and essentially it will start giving us items backwards.
print(fruits[-1])
#we can also change an item of a list
fruits[0] = "Dragon Fruit"
print(fruits)
#we can also add a lot an item to our List using the .append('item')
fruits.append("Durian")
print(fruits)
#we can extend our current list with rather one element, with another existing list
fruits.extend(["Fruit1", "Fruit2"])
print(fruits)
#and we can also get the length of the list by using the len(function)
print(len(fruits))

#we can have nested lists as well
vegetables = ["Potatoes", "Tomatoes", "Cucumbers","Onions"]
my_nested = [fruits, vegetables]
print(my_nested)
#and we can access each individual element of some of these nested list by specifying which list do we need and which element do we need
print(my_nested[0][2]) #Bananas
print(my_nested[1][2]) #Cucumbers