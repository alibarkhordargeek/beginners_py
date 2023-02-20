age = int(input())
bg = 9
bg2 = 0

while age != -1:
    if age > bg:
        bg2 = bg
        bg = age
    age = int(input())

print(bg, bg2)