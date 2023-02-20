cou = int(input())
c = 0
lis = []
while c < cou:
    lptp = input()
    l = lptp.split()
    l2 = []
    for i in l:
        i = int(i)
        l2.append(i)
    lis.append(l2)
    c += 1

x = 0
for i in lis:
    for j in lis:
        if i[0] < j[0]:
            if i[1] > j[1]:
                x += 1

if x == 0:
    print('poor irsa')
else:
    print('happy irsa')

