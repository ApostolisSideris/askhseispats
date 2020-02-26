open_file = open("test.txt","r") # instead of this file you can open any other .txt file that you want.
punctuations = '''!()-{}[];:'",\<>/.?@#$%^&*_`~''' # this string contains all the punctuations that we need to substract from our text file.
s = open_file.read()
no_punct = ""
for char in s: # this loop if the character is a punctuation or not.
    if char not in punctuations:
        no_punct = no_punct + char
def string_try(word_len, no_punct):
    string = []
    text = str.split(" ")
    for x in text:
        if len(x) > word_len:
            string.append(x)
    return string
if len(s) > 0 : # checks if there is a text into our file if not it prints that there is no text in this file.
    word_len = 3
    str = no_punct
    test = string_try(word_len, str)
    for x in range(len(test)):
        print(test[x][1:-1] + test[x][-1:] + test[x][:1] + "ay") #prints each word taking the first letter and adding it to the end with ay.
else:
    print("This file is empty.")
open_file.close()