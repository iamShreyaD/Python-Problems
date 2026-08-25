
# given a string, find the first character that appears only once.
# return the index of the first character.
# take the string.
# for loop to loop through each character of the string.
# set the count of each letter in the string as value for the letter as key.
# the first result with "letter": 1 will be yielded
# the index of the key can be found easily from the string.


text = "leetcode"

def first_unique_character(text):
    frequency = {}

    for i in range(len(text)):
