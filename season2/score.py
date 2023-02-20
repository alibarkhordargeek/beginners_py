c = 0
sum = 0
wn = 0
while c < 3:
    scr = int(input())
    sum += scr
    if scr == 3:
        wn +=1
    c += 1

print(sum, wn)