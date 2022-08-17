"""
"""
#declared using 'x'or "x"
#multiline string """x""" or '''x'''
#x= """Oranges
#ARE ORANGE IN
#COLOUR
"""

print(x)
y= "hello, world!   "#Strings in python are arrays that represents unicode chracter
print(y)
print(len(y))# we can access the character from the string by []
print("the" in y)
print("meet" in y)# in function gives boolean result ,check certain value inside a srting
print(y[5])# char positions
#for a in y: #loop through a string
 #   print(a)
print(y[2:5])#slice a string:take certain part of the string to print only that
print(y[:12])
print(y[5:])
print(y[-5:-2])#negative indexing  prints orl
print(y.upper())#modify string using .upper
print(y.lower())
print(y.strip())#remove white spaces by default it removes white spaces character
print(y.replace("h", "y"))#replace a certain string
print(y.split(","))#split a string
#string concatenation
a="Hello"
b="World"

print(a+b)# without space in between
print(a+" "+b)
#string methods
s =  " \n \t hello\n".strip("\n")#it prints in new line because leading white space
x = "\n \t hello\n" .strip("\n")

print(s)

print(x)
x = "www.example.com".strip("cmow")#pass multiple characterto the srip method
print(x)#example
s = "  hello  ".lstrip()# removes only leading white spaces and we still have trailing white space
x = " hello ".rstrip()#removes trailing white spaces
print(x)

print(s)
#removeprefix and removesuffix
s = 'Arthur: three!'.lstrip('Arthur: ')
print(s)

s = 'Arthur: three!'.removeprefix('Arthur: ')
print(s)

x = 'Helloworld'.removesuffix('world: ')
print(x)
x = 'sring methods in python'.replace(' ', '-')# white spaces are replased by -
s = 'string methods in python'.replace(' ','')#removes all white spaces
print(x)
print(s)
#re.sub ,regular expression method,used to replace a more complex pattern with a substring
#removes multiple white space character
import re
s = "string    methodes in python"

s2 = s.replace(' ','-')
s3 = re.sub("\s." , "-", s)

print(s2)
print(s3)
#split function returns the list of the words in the string
s = "string methods in python".split(' ',maxsplit=1)#by default seperated by ,only one max split
s = "string methods in python".rsplit(' ',maxsplit=1)
print(s)
#.join method
list_of_strings = ['sring', 'methods', 'in', 'python']
s = "-".join(list_of_strings)#list of string joined to one string with-
print(s) 
s = "python is awesome!".upper()
print(s)

x = "PYTHON IS AWESOME!".lower()
print(x)

y = "python is high level lang".capitalize()#only first character capitalizes
print(y)
print("PYTHON IS AWESOME!".islower())
print("python is awesome!".islower())

print("PYTHON IS AWESOME".isupper())
print("python is awesome".isupper())
#isalnum() numbers as well as alphabets
#s = "123" true for numeric and alnum
#s = "python123" true for alnum
#s = "python-123"false for all
s = "pyhton"
print(s.isalpha(), s.isnumeric(), s.isalnum())
#count() number of non overlapping occurences of the substring if not founds substrings prints 0
n = "hello world".count("o")
print(n)
#find():return the first lowest string
s = "Machine learning"
idx = s.find("a", 2)
idx1 = s.find("aa")
print(idx)
print(idx1)
print(s[idx:])
#rfind() start to search from right side
s = "Machine learning"
idx = s.rfind('a')

print(idx)
print(s[idx:])
#startwith and endswith
print("Patrick".startswith("P"))
print("Patrick".endswith("ck"))
#partition() splits the string
s = "Python is awesome!"

parts = s.partition("is")
print(parts)
parts = s.partition("was")

print(parts)
#center(),ljust(),rjust(): to formate string in a certain way
s = "Python is awesome!"
x = "Python is awesome!"
y = "Python is awesome!"
#s = s.center(30, "-")
x = s.ljust(30, "#")
y = s.rjust(30, "*")
#print(s)
print(x)
print(y)"""
#f-strings it is not a method,faster,easier to formate string
num = 1
language = "Python"
s = f"{language} is  the number {num*1} in programmming!"
print(s)
#swapcase() it will swap the all uppercase and lowercase
s = "HELLO world"
s = s.swapcase()
print(s)
#zfill
s = "42".zfill(5)
print(s)

s = "-42".zfill(5)
print(s)

s = "+42".zfill(10)
print(s)





