data = [1, 4, 45, 6, 3, 10, 8, 3, 7, 6]
target = 13
t = {9: 0, 6: 1, -35: 2, 4: 3, 0: 4, 2: 5}
def two_sum():
    res = {}
    for i in range(0, len(data)):
        temp = target - data[i]
        if temp in res:
            print(res[temp], i)
        else:
            res[data[i]] = i

# two_sum()


def three_sum():
    res = set()
    for i in range(0, len(data)):
        s = set()
        diff = target - data[i]
        for j in range(i+1, len(data)):
            two_sum_diff = diff - data[j]
            if two_sum_diff in s:
                res.add((data[i], data[j], two_sum_diff))
                # return [data[i], data[j], two_sum_diff]
            else:
                s.add(data[j])
    return res

print(three_sum())


def longestPalindrome(s):
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    longest_sub_str = ""
    for i in range(len(s)):
        center = expand_around_center(s, i, i)
        in_btwn = expand_around_center(s, i, i + 1)
        longest_sub_str = max(longest_sub_str, center, in_btwn, key=len)
    return longest_sub_str


# print(longestPalindrome("aabac"))

def rev_str():
    s = "abcde"
    res = ""
    for i in range(len(s)-1, -1, -1):
        print(s[i])
        # res += s[i]
    print(res)

# rev_str()

def sort012( a, arr_size):
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return a


# Python3 program to find a triplet using Hashing
# returns true if there is triplet with sum equal
# to 'sum' present in A[]. Also, prints the triplet
def find3Numbers(A, arr_size, sum):
    for i in range(0, arr_size - 1):
        # Find pair in subarray A[i + 1..n-1]
        # with sum equal to sum - A[i]
        s = set()
        res = []
        curr_sum = sum - A[i]
        for j in range(i + 1, arr_size):
            if (curr_sum - A[j]) in s:
                print("Triplet is", A[i],
                      ", ", A[j], ", ", curr_sum - A[j])
                res.append([A[i],A[j], curr_sum-A[j]])
                # return True
            s.add(A[j])

    # return False


# Driver program to test above function
A = [-1,0,1,2,-1,-4]
sum = 0
arr_size = len(A)
find3Numbers(A, arr_size, sum)
