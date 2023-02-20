inp = input()
l = inp.split()
l2 = []
for i in l:
    i = int(i)
    l2.append(i)
print(max(l2) - min(l2))
