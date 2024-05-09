# We are gonna talk about Python Dictionaries and Nesting
#How we create our dictionary:
# We start of by creating curly brackets and everything inside those curly brackets
# are the content of our dictionary
# If we want to have a set of dictionaries, then we separate them with comas (,)
# Example:
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
} #This is how we create a dictionary. And yes we assign the dictionary to a variable

#And how we call the dictionary:
print(programming_dictionary["Bug"])#The difference between the list and dictinary is
#that we call the list by the index of the element we want to call.
#In dictionary we call by 'key'.
#So basically dictionary is a set of 'keys' and 'values'

#and we can add elements to our dictionaries
programming_dictionary["List"] = "The action of doing something over and over again."
print(programming_dictionary["List"])

#we can create an empty dictionary
empty_dictionary = {}

#we can change a key in the dictionary

programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary["Bug"])

#and we can also loop through a dictionary
for key in programming_dictionary:
    print(key) #will print out the key
    print(programming_dictionary[key]) #will print out the value of the key

#we can wipe a dictionary
print(programming_dictionary) #the dictionary has something
programming_dictionary = {}
print(programming_dictionary) #the dictionary has nothing

#Let's talk about Nesting now
#Till now, in our dictionaries, we have been putting only simple keys and values
#But in dictionaries, we can add keys and for that key we can assign a list or another dictionary
#Same thing that we can imagine we do when we put a a list within a list.

travel_log = {
    "France": ["Paris," "Lille", "Dijon"],
    "Germany": {
        "Cities": ["Cologne", "Freiburg", "Dortmund"],
        "Days_visited": [14, 10, 1],
    }
}

#we can also have a list that each elemenent is a dictionary:
#   [{
#       Key1: Value,
#       Key2: Value,
#   },
#   {
#       Key1: Value,
#       Key2: Value,
#   }]
