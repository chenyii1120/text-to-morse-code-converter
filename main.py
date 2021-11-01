"""
convert between Morse Code and Plain Text

Author: Joseph Chen
"""

import morse_code as mc

while True:
    mode = input("Please choose which mode you want to use: \n\t 1) Text to Morse Code \n\t 2) Morse Code to Text \n")
    if mode == "1" or mode == "2":
        user_input = input("Please type in the content you want to convert: \n")
        break
    else:
        print("Invalid input, try again.")


def text_to_morse(text):
    result = ""

    # traverse all the characters in user's input
    for char in text:
        try:
            result += (mc.m_code[char.upper()] + " ")
        # if char is not in the dictionary, add a space
        except KeyError:
            result += " "

    print(f"Text: {text}\nMorse Code: {result}")


def morse_to_text(text):
    result = ""

    # split user input to string to look up
    temp = text.split(" ")
    # generate a order list with dictionary's keys/values
    mc_char = list(mc.m_code.keys())
    mc_code = list(mc.m_code.values())

    # traverse all the characters in user's input
    for char in temp:
        if char == "":
            result += " "
        else:
            index = mc_code.index(char)
            result += mc_char[index]

    print(f"Morse Code: {text}\nText: {result}")


if mode == "1":
    text_to_morse(user_input)
elif mode == "2":
    morse_to_text(user_input)

# for debug
## HELLO
## .... . .-.. .-.. ---
