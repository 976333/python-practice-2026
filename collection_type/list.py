# -----------------------------------------------------------------
#  for the perform crud operation
# -------------------------------------------------------
# 1) append()       for add the element also in nested list
# 2) extend()       add the element invijusaly at time multiple
# 3) insert(index,value) add on perticular possition 
# 4) remove()       first ocrance of element remove if not present trhough value error 
# 5) pop(index)     remove the element on index and return the value (if index not pass remove last element)
# 6) clear()        remove all element in list 
# --------------------------------------------
# for searching
# -----------------------------------------------------------------

# 1) list.index(value)   return the index of element if (not present return index not present )(for duplicate return first occurance)
# 2) list.count(value)   check the how many time present value count (if not return 0)
# 3) list.sort()      (not need to store in variable )used to sort the element in the assending order ( small to high) (reverse=True   for high to low )(can not direct print firts need to sort then print)(change in the current list )
# 4) sorted(list)     make new list (store in the other variable)
# 5) list.reverse()   reverse the origanal string
# ---------------------------------------------
# list operator 
# -----------------------------------------------------------------
# 1) list.copy()      shallow copy for change the refernce of same list 
# 2) list01 + list02    concatinate operator + in list 
# 3) list*3             repeat the list multiple time 
# -----------------------------------------------
# membership operator 

# 1) in      check the present value in the list (return type is boolean)
# 2) not in  check the value not present 
# 3) is        check the value reffernce to the same variavle 
# 4) not is    if not so return true
# ----------------------------------------------------------------
# enumerator 

# for index, value in enumerate(list)  - used for the looping and print value and index
# ----------------------------------------------------------------
# list comprehention 

# [expression for item in iterable if condition]

# new_list=[i*2 for i in old_list]  (firts we write what operation need to perform then looping on old list)
# ----------------------------------------------------------------
# nested list

# matrix[[],[],[]]

# indidual elemnt = matrix[0][1]...... row 0 and column 1

# ----------------------------------------------------------------
# built in function    

# (all function support to the same datatype element)

# 1) len(list) return length
# 2) min(list) return smallest value in list 
# 3) max(list) return max value
# 4) sum(list) return sum of all element 
# 5) any(list) return true if any value is other than 0 (any one is true)
# 6) all(list) return true if all element other than 0 
# ----------------------------------------------------------------


# num = [10,20,30]
# num.append(40)

# print(num)


# num = list((1,2,4,5))
# print(num)

# name = list("python")  # convert into char list 
# print(name)

# for i in name:
#     if(i=='t'):
#         print(i)

# slicing

# print(name[1:])

# copy = name[::-1]
# print(copy)

# add element at the last 

# num = [10,20,30,40,10,20]

# num.append([40,50])  # wont to inserthe multiplae element in nested list

# print(num)

# num.extend([100,200,300]) # add indivitual

# print(num)

# num.insert(1,1000)

# print(num)

# num.remove(200)

# print(num)

# -------------------------------

# numbers = [10, 20, 30, 40]

# # x = numbers.pop()

# # print(x)

# # print(numbers)


# numbers.clear()

# print(numbers)


# ------------------------------------------


# searching 

num = [10,20,30,40,30]


# print(num.index(100))


# print(num.count(50))

# num.sort(reverse=True)

# new_list= sorted(num)

# print(num)
# print(new_list)


# num.reverse()

# print(num[::-1])



# -------------------------------------------

a = [10,20,30]

# b=a
# print(b)
# print(a)

# b[0]=100
# print(a) # bbecause the a and be refer to same list 

# for the change refernce used shallow copy

# b = a.copy()

# b[0]=100

# print(a)
# print(b+a)

# print(a*3)

# ---------------------------------------------------


# for i ,v in enumerate(num):
#     if i >=2 and v>=20:
#         print(i,v)


#-------------------------------------------------


# # list comprehension

# num_1 =[10,20,30,40,50]

# num_2 =[]

# # for i in num_1:
# #     num_2.append(i*2)

# # print(num_2)

# num_2 = [i*2 for i in num_1]

# print(num_2)


# --------------------------------------------------


# nested list 

# matrix =[[1,2,3],[4,5,6],[7,8,9]]

# for i in range(0,len(matrix)):
#     matrix[i][len(matrix[i])-1]=0

# print(matrix)


# --------------------------------------



# list upcasting

number = [10,20,30,40]

# a, b, *c = number

# print(a)
# print(b)
# print(c)


# ------------------------------------

# build in function 

num = ['a','b']


# print(min(num))

# print(any(num))

# print(all(num))


# num.extend(['a','b','c'])
# print(num)

# print(num.pop(0))
# print(num)


num = [10,15,20,25,30,40 ,40,10]

# result = [i for i in num if i>20] 

# print(result)

