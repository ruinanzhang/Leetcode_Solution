# Q1. GoodTuples
input = [4, 4, 6, 1, 2, 2, 2, 3]
# 3 possiblilities:
# 1.  i = i -1 != i+1
# 2.  i = i+1 != i-1
# 3.  i-1 = i +1 ! =i
def getGoodTuples(arr):
    count = 0
    for i in range(1, len(arr)-1):
        if arr[i-1] == arr[i+1] and arr[i-1] != arr[i]:
            count += 1
        elif arr[i-1] == arr[i] and arr[i] != arr[i+1]:
            count += 1
        elif arr[i+1] == arr[i] and arr[i] != arr[i-1]:
            count += 1
    return count

res = getGoodTuples(input)
# -----------------------------------------------------------------------------------
# Q2. Divisor Substrings
def divisorSubStr(n, k):
    count = 0
    subset = []
    for i in range(len(n)+1-k):
        sub = n[i:i+k]
        if sub not in subset and int(n) % int(sub) == 0:
            count += 1
            subset.append(sub)
    return count

# -----------------------------------------------------------------------------------
# Q3.constructorNames

def consName(s, t):
    dict_s = collections.Counter(s)
    dict_t = collections.Counter(t)
    # First check if dict_s and dict_t have same keys
    # Second remove same key value paris from s and t dicts
    if dict_s.keys() != dict_t.keys() or len(s) != len(t):
        return False
    for key in dict_s.keys():
        if dict_s[key] != dict_t[key]:
            for key_to_swap, val_to_swap in dict_s.items():
                if val_to_swap == dict_t[key]:
                    dict_s[key], dict_s[key_to_swap] = dict_s[key_to_swap], dict_s[key]
                    break
            if dict_s[key] != dict_t[key]:
                return False
        dict_s[key] = 0
    return True

# -----------------------------------------------------------------------------------
# Q4.digitAnagrams
import collections
input = [25,35,872,228,53,278,872]
   
def digitAnagrams(list):
    res = []
    for number in list:
        res.append("".join(sorted(str(number))))
    res_dict = collections.Counter(res)
    count = 0
    for key, value in res_dict.items():
        if value > 1:
            count += (value*(value-1))//2
    return count       
result = digitAnagrams(input)

# -----------------------------------------------------------------------------------
# Q5.Reduce the number:
input = "1111122222"
k = 3
def reduceNumber(number,k):
    if len(number) <= k:
        return number
    if len(number) > k:
        res = []
        i = 0
        while i < len(number):
            res.append(str(sum(int(x) for x in number[i:i+k])))
            i = i+k
        print(res)
        string = "".join(res)
        print(string)
        return reduceNumber(string,k)
result = reduceNumber(input,k)
print(result)

# -----------------------------------------------------------------------------------
# Q6.3 divisor from 0 to n
input = "303"
def threeDiv(input):
    n = len(input) 
    count = 0
    for i in range(1,n+1):
        print("i is",i)
        j = 0
        while j<= n-i:
            if i==1 or (i!=1 and input[j]!="0"):
                curr = int(input[j:j+i])
                print("curr is", curr)
                if curr % 3 == 0:
                    count+=1
            j=j+1
    return count
print(threeDiv(input))            