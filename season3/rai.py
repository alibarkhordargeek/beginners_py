num = int(input())
c = 0
l = list()
while c < num:
    vote = input()
    l.append(vote)
    c += 1

votes = dict()
for vt in l:
    votes[vt] = votes.get(vt, 0) + 1

for each in list(votes.keys()):
    print('%s %i' %(each, votes[each]))
    
    
