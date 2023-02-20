s = input()
s = s.lower()
s2 = s

for let in s:
    if let == 'a':
        x = s2.find('a')
        s2 = s2[:x] + s2[x+1:]
    elif let == 'i':
        x = s2.find('i')
        s2 = s2[:x] + s2[x+1:]
    elif let == 'u':
        x = s2.find('u')
        s2 = s2[:x] + s2[x+1:]
    elif let == 'o':
        x = s2.find('o')
        s2 = s2[:x] + s2[x+1:]
    elif let == 'e':
        x = s2.find('e')
        s2 = s2[:x] + s2[x+1:]


s3 = ''
for let in s2:
    s3 += '.' + let

print(s3)
        
