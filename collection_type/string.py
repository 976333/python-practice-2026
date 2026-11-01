# 1) slicing

# string[start:end:step]


# --------------------------------------
# 2) string are immutable
# can not update same string
# --------------------------------------
# inbuild method for string 

# 1) string.lower()    convert into lower
# 2) string.upper()    convert in uppercase
# 3) string.title()      convert the firsst character in the upper case
# 4) string.swapcase()   convert lower to upper and upper to lower
# 5) string.strip()     remove the space from both side
# 6) string.lstrip()     remove the space from left side
# 7) string.rstrip()     remove the space from right side
# 8) string.replace()   in the space of the pass string new string added and old_string remain (multiple occurance update)
# 9) string.split()    convert into list  (default space is seprator  (we can pass like split(',')))
# 10) " ".join(list)   convert the list to string ("-".join(list)) seprator
# 11) string.find("sustring")    used to find starting index of substring (if not present so return -1)
# 12) string.index("substring")    used to find the starting index of the substring (if not present so return ValueError)
# 13) string.count("substring")    used to check how many count present 
# 14) string.startswith("substring") (boolean) if the string start with substring so return true
# 15) string.endswith("substring")   (boolean) if the string ends with substring so return True
# 16) string.isdigit()       check in the string have only digit (only positive)
# 17) string.isalpha()       check the string content only alphabets
# 18) string.isspace()       check the string contant only space
# 19) isdecimal()
# 20) isnumerical()
# 21) isalnum()
# ----------------------------------------------

# string formating

# 1) print(f"{variable_data} string_value {}")
# 2) \n        used for new line
# 3) \t        used for the tab
# 4) \"string\"    used for adding the quote in the string 
# 5) r""      used for path print      (r"C:\Users\Chaitanya\Documents")


# ----------------------------------------------

# li=[]
# a = "chaiytanya"
# list.append(a)

# # print(a[::2])
# print(list)

# c = list[0]
# c[1]='d'

# print(c)


# ------------------------------------------


# demo = "chaitanya chaitanya"

# # print(demo.title())


# # print(demo.replace('ch','deep'))

# result = demo.split()

# print(demo.find("p"))


# demo = "1a"

# print(demo.isalnum())

# path = r"C:\Users\Chaitanya\Documents"

# print(path)

# message = """
# Hello Chaitanya,Welcome to Python.
# Keep learning.
# """

# print(message)


text = "banana"

for char in text:
    print(char, text.count(char))