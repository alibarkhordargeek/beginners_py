a = input()
players  = input()
l = players.split()
l2 = []
l3 = []

for i in l:
    i = int(i)
    l2.append(i)
for ply in l2:
    if ply < 3:
        l3.append(ply)

team = len(l3) // 3
print(team)
