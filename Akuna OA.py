# 1. Account Validation 
input = "BADF00D5"
first_2 = input[:2]
hex_numbers = input[2:]
decimals = int(hex_numbers,16)
count = 0
for num in str(decimals):
    count += int(num)
hex_count = str(hex(count).split('x')[-1]).upper()
if hex_count == first_2 :
    print("Valid")
else:
    print("Not Valid")

# 2. Destination Calculation
input1 = "C0FFEE1C:CHI:NYC:714"
input2 = "0FF1CE18:LA:SEATTLE:961"
input3 = "COFFEE1C:NYC:LA:2448"
inputs = []
inputs.append(input1)
inputs.append(input2)
inputs.append(input3)
print(inputs)
total_des = 0
passenger = {}
city = {}
total_res = []
import operator
def getDesCal(input,total):
    res = input.split(":")
    curr_p = res[0]
    curr_city1 = res[1]
    curr_city2 = res[2]
    curr_miles = res[3]
    city[curr_city1] = city.get(curr_city1,0) + 1
    city[curr_city2] = city.get(curr_city2,0) + 1
    passenger[curr_p] = int(passenger.get(curr_p,0)) + int(curr_miles)
    total += int(curr_miles)
    sorted_passenger = sorted(passenger.items(), key=operator.itemgetter(1),reverse=True)
    sorted_city = sorted(city.items(), key=operator.itemgetter(1),reverse=True)
    res = str(total) +":"+ sorted_passenger[0][0] + ":" +sorted_city[0][0]
    return total,res
total,res1 = getDesCal(input1,total_des) 
total_res.append(res1)

total,res2 = getDesCal(input2,total)
total_res.append(res2)

total,res3 = getDesCal(input3,total)
total_res.append(res3)

print(total_res)

# 3. Longest Distance 
# from math import acos,sin,cos,radians
import math
R = 3963
info1 = "LOC:CHI:41.836944:-87.684722"
info2 = "LOC:NYC:40.7127:-74.0059"
info3 = "TRIP:COFFEE1C:CHI:NYC"

def get_info(info):
    info_s = info.split(":")
    return info_s[1],float(info_s[2]),float(info_s[3])

c1,lat1,lon1 = get_info(info1)
o1 = math.radians(lat1)
k1 = math.radians(lon1)
c2,lat2,lon2 = get_info(info2)
o2 = math.radians(lat2)
k2 = math.radians(lon2)
print(c1,o1,k1)
print(c2,o2,k2 )

dif = abs(k1-k2)
print(dif)
a = math.sin(o1) * math.sin(o2)
b = math.cos(o1)*math.cos(o2)*math.cos(dif)
print(math.sin(o1) * math.sin(o2))
print((math.cos(o1)*math.cos(o2)*math.cos(dif)))
print(a+b)
c = a + b
print(math.acos(c))

delta = math.acos((math.sin(o1) * math.sin(o2) )+ (math.cos(o1)*math.cos(o2)*math.cos(dif)))
print(delta)
d= R*delta
print(int(d))


