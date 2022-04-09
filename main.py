def no(a, b):
    print('do nothing', a, b)
    return 'not none'

print('hekko')
a = 1; b = 2; print(a, b)
a = 5
if a == 5:
    print('Ура!')
a = int(input())
if a < 0:
    print('false')
elif a == 0:
    print('false')
else:
    print('true')
buf = no('s', 5)
print(buf)