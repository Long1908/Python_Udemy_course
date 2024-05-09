def encrypt(text, shift, alphabet):
    for i in range(len(text)):
        index_in_alphabet = alphabet.index(text[i])
        pos = (index_in_alphabet + shift) % len(alphabet)
        text_list = list(text)
        text_list[i] = alphabet[pos]
        text = ''.join(text_list)
    return text

def decrypt(text, shift, alphabet):
    for i in range(len(text)):
        index_in_alphabet = alphabet.index(text[i])
        pos = (index_in_alphabet - shift) % len(alphabet)
        text_list = list(text)
        text_list[i] = alphabet[pos]
        text = ''.join(text_list)
    return text

cyphering = True
print("Welcome to your Ceasar_Cypher. Quick note on how things are going to work.\nWhen you write 'encode', the shift is gonna move to the right --->.\nWhen you write 'decode', the shift is gonna move to the left <---.\nLet's begin!")
while cyphering:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction != 'encode' and direction != 'decode':
        print("I am sorry, but the command that you have put is not supported.")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypted_text = encrypt(text, shift, alphabet)
        print(f"Your new text is: {encrypted_text}.")
    elif direction == 'decode':
        decrypted_text = decrypt(text, shift, alphabet)
        print(f"Your new text it : {decrypted_text}.")
    working = input("Do you want to encrypt again? (y/n) ").lower()
    while working != 'y' and working != 'n':
        print("I am sorry, but the command that you have put is not supported.")
        working = input("Do you want to encrypt again? (y/n) ").lower()
    if working == 'n':
        cyphering = False
        print("Thank you for using Caesar_Cypher!")

#NOTES:
#I
#In Python, strings are immutable objects, meaning their values cannot be changed after they are created.
#When you pass a string into a function and modify it inside the function, you are actually creating a new string object
#with the modified value, rather than modifying the original string.
#That is why we are gonna see:
#   1)How we create a text_list where we save each letter of the text, and later after we changed our text_list. We parse it into our text variable.
#       This work cause we are not changing th string we are giving it a new value.
#   2)After the functions have ended though, our text does not change yet again cause once again a string is immutable.
#       So in order to save our encryption, we save it in a new variable.

#II
#How we fix if the user is giving us a bigger number than the alphabet length is using little logic and math.
#We imagine that the list is not just a line, but actually a circle. If we get the modul division, then we will get the position, no matter how big the number is.
#P.S i thought about it i am proud :)

#III
# index() get an argument and searches the index of the element in the list.
# list() works in a string where it splits all the characters into different elements
# join() will get the elements of a list and create a string out of all of them and append them to a string.

#IV
#If we want to clean our code technically speaking we can combine the encode() and decode() functions.
#We also need to make it so we check the text that we parse. Cause it can have random unusable symbols.