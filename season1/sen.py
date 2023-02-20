sen = int(input())

if 0 < sen < 6:
    print('khordsal')
elif 6 <= sen < 10:
    print('koodak')
elif 10 <= sen < 14:
    print('nojavan')
elif 14 <= sen < 24:
    print('javan')
elif 24 <= sen < 40:
    print('bozorgsal')
elif 40 <= sen:
    print('miansal')