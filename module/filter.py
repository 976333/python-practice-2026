# numbers = [1, 2, 3, 4, 5, 6]

# result = map(lambda x: x % 2 == 0, numbers)

# print(list(result))



a = [1, 2, 3]
b = [10, 20, 30]

result = map(lambda x, y: x + y, a, b)

print(list(result))