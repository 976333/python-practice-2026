# Set → unique values + no indexing + mutable collection
# --------------------------------------------------------------------------------------------------------
# set methods 
# --------------------------------------------------------------------------------------------------------

# 1) .add(element)  used to add the value
# 2) .update([list of elemnt])    add multiple element in set
# 3) .remove(element)   remove the spacific element  (if element not present print keyerror)
# 4) .discard(element)    remove the specific element (if not present noting will happen )
# 5) .clear()             remove aall element 
# 6) .del()               clear and delete the variable 
# --------------------------------------------------------------------------------------------------------
# set operator
# 1) result =set01.union(set02)     combine the element remove duplicate                                   (A|B)......union
# 2) result =set01.intersection(set02) combine the element and return only thoes element present in both   (A & B).....intersection
# 3) result =set01.differnce(set02)    not  match elelemnt from set01                                      (A-B)......difference
# 4) result =set02.intersection(set01) not  match elelemnt from set02                                      (B-A).......difference
# 5) print(A.symmetric_difference(B))    return only thoes element not match                               (A ^ B).....symmetric_difference
# 6) issubset()
# 7) issuperset()
# 8) isdisjoint()   no comman elelemnt 
# --------------------------------------------------------------------------------------------------------

demo = {10,20,23,23,40,40}
demo2 = {10,200}
# print(deomo)

# deomo.add("f")

# print(deomo)

# demo.remove(23)
# print(demo)

# demo.discard(23)

# print(demo)
# demo.pop()

# print(demo)


# for i in demo:
#     print(i)

result =demo2^(demo)

print(result)