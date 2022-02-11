"""import re
def to_jaden_case(string):
    # ...
    print (string)
    string=string.title()
    print (string)

quote = "How can mirrors be real if our eyes aren't real"

quote = "Mo'st trees are blue"
print(quote)
quote = quote.title()
print(quote)

l = quote.split()
print(l)
s1 = ' '.join(l)  
print(s1)"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    print(text)
    nums = [str(ord(x) - 96) for x in text.lower() if x >= 'a' and x <= 'z']
    print((nums))
    return " ".join(nums)

    print(result)

text="most treessssss are blue"
print(text);
alphabet_position(text)
