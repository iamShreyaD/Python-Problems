
# write a function to check if the string is palindrome.
# take a string.
# define function palindrome(string)
# check if string = r_string


string = "madam"

def is_palindrome(string):
    a = string.lower()
    s = []

    for i in range(len(a)-1,-1,-1):
        s.append(a[i])

    reverse_string = "".join(s)

    return a == reverse_string

print(is_palindrome(string))
