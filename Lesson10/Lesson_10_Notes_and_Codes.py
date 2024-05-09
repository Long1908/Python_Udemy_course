#This lesson we are gonna talk about Functions with Outputs
#We are gonna tackle a little bit of Docstrings as well.
def format_name(f_name, l_name):
    my_full_name = f_name.title() + " " + l_name.title()  #title() makes every new word start with upper case and every other character be lower case
    return my_full_name

my_name = format_name("LONG", "nguen")
print(my_name)

#after a return in a function, whatever is below it(in the same indented level and in the same function box) will not compile

#Docstrings are the piece of text we see when we hover on a function, mostly on modules that we have imported.
def my_function():
    """This is the text you are going
    to see when you hover now the next
    time you call this function"""
my_function()

#As we can see actually with these """Something""" we can comment down multiple lines of code.
#While yes it still counts as a comment, conventionally speaking we stray away from that
#It's good to differentiate between comments and Docstrings.
#One way to make it easy to comment something is by writing our multiple lines of comment.
#And then hit ctrl + /

# dasdasdasdad
# asdadsadasd
# asdsad

#NOTE:

# Python takes user input as a string format
# by default because it treats all input as a string,
# regardless of the data type that the user intends to input.