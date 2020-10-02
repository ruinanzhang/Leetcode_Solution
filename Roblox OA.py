# 1. Efficient Jar 
list = [1.01,1.99,2.5,1.5,1.01]
list.sort()
print(list)
left = 0
right = len(list)-1
count = 0
while left <= right :
    if left == right:
        count +=1
        break
    if list[left] + list[right] <= 3:
        count +=1
        left +=1
        right -=1
    elif list[left] + list[right] > 3:
        if left > 1.99:
            print(count + right - left + 1)
        else:
            count +=1
            right -=1
print(count)

# 2. Break Prison:
    # （len（最长连续数列 for h）+ 1）* （len（最长连续数列 for v）+ 1）

# 3. Slowest key press 
input = [[0,1],[0,3],[4,5],[5,6],[4,10]]

prev_time = 0
map = {}
max_time = 0
res = ""
for keypair in input:
    key = keypair[0]
    time = keypair[1]
    time_used = time - prev_time
    if time_used > max_time:
        res = key
        max_time = time_used
    prev_time = time
if res == 0:
    print('a')
else: 
    print(chr(ord('a') + res))

# 4. University Career Fair (Meeting Room)
# Greedy!
import operator
# Univeristy Career Fair
arr = [1,3,3,5,7]
dur = [2,2,1,2,1]
map = []
for i in range(len(arr)):
    map.append((arr[i], arr[i]+dur[i], dur[i]))
map = sorted(map,key=lambda x: x[1])
print(map)
aux = sorted(list(zip(arr, dur)),key=lambda p: (sum(p), p[1]))
print(aux)
ans, end_time = 0, -float('inf')
for i in map:
    arr_time = i[0]
    duration = i[2]
    if arr_time >= end_time:
        ans += 1
        end_time = arr_time+duration
print(ans)
    
    