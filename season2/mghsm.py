c = 0
Nmgh = 2
theNum = 0

while c < 20:
    mgh = 0
    num = int(input())
    for i in range(1, num+1):
        x = num % i
        if x == 0:
            mgh += 1
    if mgh >= Nmgh:
        Nmgh = mgh
        theNum = num
    c += 1

print(theNum, Nmgh)