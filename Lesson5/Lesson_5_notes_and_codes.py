#How to create a for loop:
fruits = ["Apples", "Pears", "Oranges", "Bananas"] #Lets say we want to have a list of items we want to go through one by one
#we start out with a key name called 'for' and then we assign a single word for a single item name. In this case fruit.
#then we specify 'in' and we say what kind of list are we going through step by step
for fruit in fruits:
    print(fruit) #notice that we are giving the single item "fruit" (WITHOUT THE -s IN THE END)
    print(fruit + " Pie") #we can also do changes with each element we loop through
    print(fruits) #this will print out the whole List for the length of the List times

#Essentially how we would know asically the loop is:
#for i in list:
#   do something
#where i given like this is 0 by default and we just go through each element of list one by one

#EXTRA: split() function can split a String into a list
#EXTRA: sum() sums out the elements of an array.

#instead of looping through array and let's say we just want to loop from one lower bound to upper bound we can use the range(a, b) function
for i in range(0, 10):
    print(i)
#what this will do is that we are giving the loop not a list but a range to work upon. And what is important, is that in this range we include the lower bound but exclude the upper bound
#so basically i < upper bound, or in this case i < 10

#for i in range(10, 20) is just like we starting from index 10 and we go all the way up to but not included 20.
#like: for(int i = 10, i < 20, i++)

#we can also use range(a, b, c) which a stands for lower bound, b is upper bound and c is the incrementation value
for i in range(1, 20, 2):
    print(i)
#so in this example it works the same way as (for int i = 0, i <20, i += 2)
