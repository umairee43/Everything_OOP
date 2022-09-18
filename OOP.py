import re


text = input("Enter something Random")
list = re.findall("[a-z]" , text)
print(list)