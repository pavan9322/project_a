#
# def decorate_add(func):
#     def inner_func(a,b):
#         # res = func(a,b)
#         # return res
#         # print(res)
#         return func(a,b)
#     return decorate_add
#
# @decorate_add
# def add(a,b):
#     return a+b
#
# add(2,5)
#
#
#
#
# # print i/o
#


# class A:
#     def M1(self):
#         print('Hi')
# class B:
#     def M1(self):
#         print('Bye')
# class C(A,B):
#     pass
# c=C()
# c.M1()


# s1='{{}}{}'   #valid
#
# s2='{{}}{' # invalid
#
# '}{'  # invalid
#
#
# def check_valid_string(s):
#     count = 0
#     if (len(s) % 2 == 0):
#         for i in s:
#             if i == '{':
#                 count += 1
#             elif i == '}'
#
#     else:
#         pass

# s=879
# largest = 987
# smallest = 789
# #approach 1
# print(sorted(list(str(s)), reverse=True))
# print(sorted(list(str(s))))

l= [6,9,4,6,0,2]
# l= [2,0,6,4,9,6]

# for i in range(len(l)-1,0,-1):
#     print()

# if len(l) % 2 == 0:
#     for i in range(0, len(l)//2):
#         print(i)
#         l[i],l[-i] = l[-i], l[i]
#
# print(l)

# for i in l:
#     l.append(l.pop())
# print(l)

s = [4,6,9,0,1,2,44]

# l = 0
# n = len(s) - 1
# index = 0
#
# for i in range(1, n):
#     while l < n:
#         if s[i] < s[i+1]:
#             s.insert(l, s[i])
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize the algorithm by checking if any swaps are made
        swapped = False

        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps were made in this pass, the list is already sorted
        if not swapped:
            break

# Sample list of numbers
numbers = [5, 2, 9, 1, 5, 6]

# Sorting the list using Bubble Sort
bubble_sort(s)

print("Sorted list (ascending) using Bubble Sort:", s)













