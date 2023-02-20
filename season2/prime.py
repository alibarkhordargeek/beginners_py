a = int(input())
for i in range(2, a):
    tst = 0
    x = a % i
    if x == 0:
        tst = 1
        print('not prime')
        break

if tst == 0:
    print('prime')