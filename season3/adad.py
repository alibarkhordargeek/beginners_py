s = input()
s2 = ''

for let in s:
    if let == '1':
        s2 += '+' + let

for let in s:
    if let == '2':
        s2 += '+' + let

for let in s:
    if let == '3':
        s2 += '+' + let

s2 = s2[1:]
print(s2)

        
