# BOB SELL STOCK
gain = [7, -3, -10, 4, 2, 8, -2, 4, -5, -2]


def get_max_profit(gain):
    sub_sum = 0
    max_p = 0
    curr_p = 0
    for i in range(len(gain)):
        if sub_sum < 0:
            sub_sum = 0
        if gain[i]+sub_sum > max_p:
            max_p = gain[i]+sub_sum
        sub_sum += gain[i]
    return max_p


print(get_max_profit(gain))

# BOB SHOPPING CART
vw = [[5, 4], [3, 2], [10, 8], [4, 8]]
def get_most_value(vw):
    value = [0]
    paths = []

    def helper(vw, w, v, path):
        if w > 10:
            return
        if v > value[-1]:
            value.append(v)
        if not vw:
            return
        for i in range(len(vw)):
            path.append(vw[i][0])
            helper(vw[i+1:], w+vw[i][1], v+vw[i][0], path)
            path.pop()
    helper(vw, 0, 0, [])
get_most_value(vw)
print(value[-1])

# Compress Number extra space:
class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        curr = ""
        index = 0
        while index < len(chars):
            if index == 0:
                curr = chars[index]
                count +=1
                
            elif chars[index] == chars[index-1]:
                count +=1
               
            else:
                res.append(str(count))
                count = 1
                res.append(str(chars[index]))
            index +=1
        return res

# Beautiful string:
import collections
string = "nanakonagounagouna"
counter = collections.Counter(string)
largest = 26
ind = 0
max_beauty = 0
for key, value in counter.items():
    max_beauty += (largest-ind)*value
    ind +=1
print(max_beauty)

#Mth 

# if int(s[i-1:i+1]) <=26 and int(s[i-1:i+1])>=1