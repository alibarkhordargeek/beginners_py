c = 0
names = []
while c < 10:
    s = input()
    c += 1
    s = s.lower()
    s = s[0].upper() + s[1:]
    names.append(s)

for i in names:
    print(i)
    
