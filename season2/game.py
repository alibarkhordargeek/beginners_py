from random import randint
mx = 99
mn = 1
gs = randint(mn, mx)

print(gs)
res = input()

while res != 'd':
    if res == 'k':
        mx = gs - 1
    elif res == 'b':
        mn = gs + 1
    gs = randint(mn, mx)
    print(gs)
    res = input()