
# identify if two strings are anagrams.
# take two strings.
# define the function with two parameters.
# create two dictionaries.
# get one for loop for each of the two strings to get their frequencies.

s = "anagram"
t = "nagaram"

def is_anagram(s, t):
    f = {}
    g = {}

    for char in s:
        if char in f:
            f[char] += 1
        else:
            f[char] = 1

    for char in t:
        if char in g:
            g[char] += 1
        else: 
            g[char] = 1

    return f == g

print(is_anagram(s,t))
