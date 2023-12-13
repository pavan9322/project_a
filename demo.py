# a = 'abcdefsadalskdkaslmd'
#
# str_to_check = set(a)
# res = {}.fromkeys(str_to_check, 0)
# for i in str_to_check:
#     if i in res:
#         res[i] = a.count(i)
#
# print(res)

# arr = [4, 3, 6, 2, 1, 1, 12]
# numberMap = {}
# max = len(arr)
# for i in arr:
#     if not i in numberMap:
#         numberMap[i] = True
#     else:
#         print("Repeating =", i)
# for i in range(1, max + 1):
#     if i not in numberMap:
#         print("Missing =", i)
nums = [2,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1]
res = nums[0] # Initialization
counter = 0 # Counter
# for i in range(len(nums)):
#     if counter == 0:
#         res = nums[i]
#         counter = 1
#     elif res == nums[i]:
#         counter += 1
#     else:
#         counter -= 1
# print(res)
# count_map = {}.fromkeys(nums,0)
count_map ={}
for i in nums:
    if i not in count_map:
        count_map[i] = 1
    else:
        count_map[i] += 1
print(count_map)

max = 0
res = 0
for i,v in count_map.items():
    if max < v:
        max = v
        res = i
print(f"Maximum:{res}")
