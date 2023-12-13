
s = ['a',1,'b','H']

# p = all([isinstance(i, str) for i in s])
# # print(p)
# x =  range(10)
# print(*x)
# y = {"name" : "John", "age" : 36}
# print(**y)

# def print_person_info(**kwargs):
#     print("Name:", kwargs['name'])
#     print("Age:", kwargs['age'])
#
# person_info = {"name": "John", "age": 36}
# # print_person_info(**person_info)
# # s.extend(person_info)
# # print(s)
# # print(*range(100))
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# vowels = ['a', 'e', 'i', 'o', 'u']
#
# result = [any(vowel in fruit for vowel in vowels) for fruit in fruits]
#
# print(result)
thislist = [100, 50, 65, 82, 23, 200]
# o = [50, 65, 23, 82, 100]

# min = 0
new_list = []
val = 50
for i in range(len(thislist)-1, 0, -1):
    for j in range(i):
        if thislist[i] > thislist[j]:
            thislist[i], thislist[j] = thislist[j], thislist[i]
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# val = 50
# new_list = []

# for i in range(len(thislist)):
#     min_diff = float("inf")  # Initialize with a large value
#     min_index = -1
#
#     for j in range(len(thislist)):
#         if j != i:
#             diff = abs(thislist[j] - val)
#             if diff < min_diff:
#                 min_diff = diff
#                 min_index = j
#
#     if min_index != -1:
#         new_list.append(thislist[min_index])
#         thislist.pop(min_index)
#
# print(new_list)

# thislist = [100, 50, 65, 82, 23]
# val = 50
#
# for i in range(len(thislist)):
#     min_diff = float("inf")  # Initialize with a large value
#     min_index = -1
#
#     for j in range(i, len(thislist)):
#         diff = abs(thislist[j] - val)
#         if diff < min_diff:
#             min_diff = diff
#             min_index = j
#
#     if min_index != -1:
#         # Swap the elements at positions i and min_index
#         thislist[i], thislist[min_index] = thislist[min_index], thislist[i]
#
# print(thislist)

#
# thistuple = ("apple", "banana", "cherry",[0,1,2])
# thistuple[3][1] = 44
# # print(type(*thistuple))
#
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# a,b,c = fruits[0], fruits[1], list(fruits[1:])
# print(a, b, c)
#
# d = {"a":1, "b":2, "c":3, "a":4}
# print(d)
# print({1,2}[0])
# print(2 != 1)

# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# res = json.loads(x)
# print(res, type(res))
# res2 = json.dumps(res, indent=4)
# print(res2, type(res2))

import re

#Check if the string starts with "The" and ends with "Spain":

# txt = "The rain in Spain"
# email = "pavan9322@gmail.com"
# import threading
# x = 0
# def func1():
#     global x
#     for i in range(100):
#         x += 1
#         print("func1", x)
#
# def func2():
#     global x
#     for i in range(100):
#         x -= 1
#         print("func2", x)
#
# t1 = threading.Thread(target=func1)
# t2 = threading.Thread(target=func2)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

import numpy as np
# Element-wise arithmetic
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
x = np.array([1, 2, 3, 4, 20])
addition = a + b
multiplication = a * b

# Aggregation
mean = np.mean(b)  # Mean of the array
sum_values = np.sum(b)  # Sum of the array

# Reshaping arrays
matrix = np.array([[1, 2, 3], [1, 3, 4]])
flattened = matrix.flatten()  # Flattens the matrix into a 1D array
reshaped = matrix.reshape(3, 2)  # Reshapes the matrix

# Indexing and slicing
sub_array = a[1:3]  # Slicing, gets the elements at index 1 and 2
element = matrix[0, 1]  # Indexing, gets the element at row 0, column 1
# print(addition)
#
# print(multiplication)
# print(matrix)
# print(flattened)
# print(reshaped)
import pandas as pd
# s = pd.Series([1, 2, 3, 4, 5])
# result = s.map(lambda x: x * 2)
# print(result)
# s = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
# unique_values = s.unique()
# print(unique_values)
import pandas as pd

# data1 = {'A': [1, 2], 'B': [3, 4]}
# data2 = {'A': [5, 6], 'B': [7, 8]}
# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)
# result = df1.append(df2, ignore_index=True)
# print(result)

import pandas as pd
#
# data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
# df = pd.DataFrame(data)
# result = df.apply(lambda x: x * 2)
# print(result)

# data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
# df = pd.DataFrame(data)
# result = df.aggregate(['sum', 'mean'])
# print(result)


# list1 = [1, 2, 3, 4, None, 6, None, None, 8, 9]
#
# var = None
# for i in range(len(list1)-1):
#     if list1[i] is not None:
#         print(list1[i])
#         var = list1[i]
#     else:
#         list1[i] = var
# print(list1)

# l = [44, 6, 7, 99, 10]
# print(min(l), max(l))
# missing_num = []
# for i in range(min(l), max(l)):
#     if i not in l:
#         missing_num.append(i)
# print(missing_num)

# prices = [7,1,5,3,6,4]
# Output: 5
# min_price = prices[0]
# max_price = 0
# for i in prices[1:]:
#     if i < min_price:
#         min_price = i
#     elif max_price < (i - min_price):
#         max_price = i-min_price
#
# print(max_price)

# l = [0,1,1,2,1,0,2,1,0]
#
# for i in range(len(l)-1, 0, -1):
#     for j in range(i):
#         if l[i] < l[j]:
#             l[i],l[j] = l[j],l[i]
# print(l)
#
# l = [2,5,7,4,9,10]
#
# print(sorted(l))
# print(sorted(l, reverse=True))
# print(sorted(l, key=int(4)))

# thislist = [100, 50, 65, 82, 23]
# val = 50
#
# # Define a custom key function to sort based on the absolute difference from val
# thislist.sort(key=lambda x: 4)
#
# print(thislist)


# def conver_to_upper(func):
#     def decorate(n):
#         func(n)
#         return str(n).upper()
#     return decorate
#
# @conver_to_upper
# def input_name(n):
#     print("From input")
#     print(n)
#
# print(input_name("pavan"))

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print(f"Transposed matrix: {matrix}")
    for i in range(n):
        matrix[i].reverse()
    return matrix

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
# print(rotate(mat))


def create_dict_keys_from_list():
    l = ['a', 'b', 'c']
    resdict = {}
    r = {}
    for i in l:
        if i not in resdict:
            resdict[i] = None
    print(resdict)
    print(r.fromkeys(l, None))


create_dict_keys_from_list()


