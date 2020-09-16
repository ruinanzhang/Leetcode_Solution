# Hello World program in Python
land = [630,645,730,1100]
off =[700,845,1015,1130]
wait = 20
init = 1
count = init
max_c = init
waiting = 0
ll = len(land)
lo = len(off)
i = 0 
j = 0
while i < ll and j < lo:
    if land[i]<off[j]:
        if land[i] + wait < off[j]:
            count +=1
        else:
            waiting +=1
        i+=1
    else:
        if waiting > 0:
            waiting -=1
        elif waiting == 0:
            count -=1
        j+=1
    max_c = max(max_c,count)
while i<ll:
    count += 1
    max_c = max(max_c,count)
    i+=1
while j<lo:
    if waiting > 0:
        waiting -=1
    elif waiting == 0:
        count -=1
    max_c = max(max_c,count)
    j+=1
    
print(max_c)