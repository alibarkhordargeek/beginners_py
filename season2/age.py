age = int(input())
bg = 10

while age != -1:
    if age > bg:
        bg = age
    age = int(input())

print(bg)