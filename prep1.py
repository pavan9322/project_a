def sum_nums():
    nums = [1,4,7,4,22,4,6,9]
    sum = 0
    for i in nums:
        sum += i
    return sum

def string_rev():
    s = "pavan"
    res = ""
    for i in range(len(s) - 1, -1, -1):
        res += s[i]
    print(res)


def remove_duplicates():
    nums = [1, 4, 7, 4, 22, 4, 6, 9]
    lookup = []
    duplicates = []
    for i in nums:
        if i not in lookup:
            lookup.append(i)
        else:
            if i not in duplicates:
                duplicates.append(i)
    print(lookup, duplicates)


# remove_duplicates()

def sort_dict_by_val():
    res = {}
    d = {'apple': 15, 'banana': 10, 'cherry': 20}
    val = []
    for i in d.values():
        val.append(i)
    print(val)
    for i in range(len(val) - 1, 0, -1):
        for j in range(i):
            if val[i] < val[j]:
                val[i],val[j] = val[j], val[i]
    for i in val:
        for k,v in d.items():
            if i == v:
                res[k] = i
    print(res)


# sort_dict_by_val()

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Instance created")
        else:
            print("Cannot create another instance")
        return cls._instance


# Singleton()
# Singleton()

def else_in_forloop():
    for i in range(5):
        print(i)
        # if i == 3:
        #     break
    else:
        print("Loop finished")

# else_in_forloop()

def merge_dict():
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    merged = {**d1, **d2}
    print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}


# merge_dict()

def filter_palindrom():
    words = ["radar", "python", "level", "world"]
    res = []
    for i in words:
        if i == i[::-1]:
            res.append(i)
    print(res)


# filter_palindrom()
nested_list = [1, [2, 3, [4, 5]], 6]
def flatten_list(l):
    res = []
    for i in l:
        if isinstance(i, list):
            res.extend(flatten_list(i))
        else:
            res.append(i)
    return res

# print(flatten_list(nested_list))


def common_element_from_list():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    common = []
    for i in list1:
        if i in list2:
            common.append(i)
    print(common)


# common_element_from_list()


def merge_dict():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}

    for k,v in dict2.items():
        if k in dict1.keys():
            dict1[k] = dict2[k]
        else:
            dict1[k] = v
    print(dict1)


# merge_dict()

def most_repeated_chars():
    strin = "aabbbcdddde"
    lookup_dict = {}.fromkeys(strin, 0)
    for i in strin:
        if i in lookup_dict:
            lookup_dict[i] += 1
    print(lookup_dict)
    x = dict(sorted(lookup_dict.items(), key=lambda item: item[1]))
    for k,v in x.items():
        if max(x.values()) == v:
            print(k)

# most_repeated_chars()


def identify_non_repeat_chars():
    strin = "abcdef"
    lookup = []
    for i in strin:
        if i not in lookup:
            lookup.append(i)
    if "".join(lookup) == strin:
        return True
    else:
        return False

# print(identify_non_repeat_chars())

# most_repeated_chars()

def move_zeros_to_end():
    numbers = [0, 5, 0, 1, 2, 0, 4, 0, 5, 6, 0]
    i = 0
    zero_count = numbers.count(0)
    count = 0
    while i < len(numbers):
        if count == zero_count:
            break
        if numbers[i] == 0:
            numbers.pop(i)
            numbers.append(0)
            i = 0
            count += 1
        else:
            i += 1
    print(numbers)


def valid_parenthesis():
    brackets = "{[]}"
    mapping = {")": "(", "}": "{", "]": "["}
    res = []
    for i in brackets:
        if i in mapping:
            if res and mapping[i] == res[-1]:
                res.pop()
            else:
                return False
        else:
            res.append(i)
    return True if not res else False

# print(valid_parenthesis())


def reverse_string_without_reversing_non_alphabets():
    s = "ab@cd#ef$gh"
    lookup = {}
    valid_alphabets = []
    for i in s:
        if not i.isalpha():
            lookup[i] = s.index(i)
        else:
            valid_alphabets.append(i)
    res = valid_alphabets[::-1]
    for k,v in lookup.items():
        res.insert(v,k)
    print("".join(res))

# reverse_string_without_reversing_non_alphabets()


def identify_first_non_rep_chars():
    s = "swiss"
    lookup = {}.fromkeys(s, 0)
    for i in s:
        if i in lookup:
            lookup[i] += 1
    print(lookup)
    res = []
    for k,v in lookup.items():
        if v == 1:
           res.append(k)
    print(res[0])

# identify_first_non_rep_chars()

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print(f"Transposed matrix: {matrix}")
    for i in range(n):
        matrix[i].reverse()
    return matrix

# mat = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
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


# create_dict_keys_from_list()