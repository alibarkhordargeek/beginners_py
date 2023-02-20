from math import sqrt
num = int(input())
c = 0
l = list()

while c < num:
    nm = int(input())
    n = ('%.4f' %(sqrt(nm)))
    l.append(n)
    c += 1

for nm in l:
    print(nm)
    
