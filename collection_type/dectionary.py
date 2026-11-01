# add or the update multipale value 
# dec_name.update({key:value})

# ------------------------------------------------
# dectionary methods 

# 1) .get(key)      -> gte value safely (if not exists return None)
# 2) keys()         -> return all key in dectionry of list 
# 3) values()       -> return all values in dictionry of list
# 4) items()          -> get key value pairs
# 5) update()         -> add/update data (multiple value)  (dec_name.update({key:value})
# 6) pop(key)          -> remove specific key 
# 7) popitem()         -> remove last pair
# 8) clear()           -> remove evrything 
# 9) setdefault()      -> get/create key 
# 10) copy()           -> copy dictionary
# ----------------------------------------------------------------

student = {
    "name": ["Chaitanya","valmik"],
    "age": 22,
    "dept":"computer",
    "marks": 85
}
# if student["name"]=="Chaitanya":
#     print("sahi hai ")
# print(student.get("city","pune"))
# student["marks"])

# print(student)

# demo =student.pop("age")
# print(demo)
# print(student.popitem())




# numbers = [1, 2, 2, 3, 3, 3, 4]
# frequency = {}

# for num in numbers:

#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1

# print(frequency)



demo_string = [1,3,4,5]


print(demo_string *2)