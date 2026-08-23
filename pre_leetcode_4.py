
# write a function that takes a string and a character and returns how many times that character appears in the string.
# split string into individual characters. this will give a list
# set n = 0 for the number of character appearanc
# create for loop for i in list:

text = "banana"
t = list(text)      #['b','a','n','a','n','a']
char = "a"

def count_character(t, char):
    n = 0

    for i in t:
        if i == char:
            n += 1

    return n

print(count_character(t, char))
