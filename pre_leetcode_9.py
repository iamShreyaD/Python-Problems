
# write a function that takes a string and returns the string in reverse order.
# take a string.
# define function with string.
# create loop for the string in reverse order
# in such a way that text[-1] will get appended to a list called s.
# print this list to check
# add another line to join the list to form a string.
# return this string.


text = "hello"

def reverse_string(text):
    s = []

    # for i in (4, -1, -1)
    # remember this is index not element
    for i in range(len(text)-1, -1, -1):
        s.append(text[i])
 
    string = "".join(s)

    return string

print(reverse_string(text))

        
