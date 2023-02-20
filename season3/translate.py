num = int(input())
c = 0
li = list()
tran = dict()
while c < num:
    s = input()
    l = s.split()
    li.append(l)
    c += 1

for i in li:
    tran[i[0]] = i[1]

sent = input()
l2 = sent.split()
for i in range(0, len(l2)):
    for j in list(tran.keys()):
        if l2[i] == j:
            l2[i] = tran[j]

print(' '.join(l2))

