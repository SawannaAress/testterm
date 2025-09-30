def finps(s):
    try:
        a = float(input('вещественное число: ' + s+' ' ))
        err = 0
    except ValueError:
        print('Неверный формат,', s, 'xx.xx')
        a = -1
        err = -1
    return a, err
def finp(s):
    err = -1
    while err == -1:
        a, err = finps(s)
    return a
def lastkey():
    input('для закрытия нажмите enter')
    return
def rtask():
    try:
        f = open('task text.txt', 'r', encoding='utf-8')
        for s in f:
            print(s, end='')
        f.close()
        print('')
    except FileNotFoundError:
        print('файл с условием не найден')
        return

def chan(t, delta):
    t1 = t + delta
    return t1
def veri(t1, t2, delta):
    if abs(t1-t2)<= delta:
        a = 1
        print (t1, 'совпадает в пределах погрешности +-', delta, 'c', t2)
    else:
        a = 0
        print (t1, 'не совпадает в пределах погрешности +-', delta, 'c', t2)
    return a
def bord(l, r, t):
    if t<=r and t>=l:
        print ('показание технического термометра', t, 'в пределах от', l, 'до', r)
    else:
        print('показание технического термометра', t, 'НЕ в пределах от', l, 'до', r)
rtask()
Xn = finp('Xн')
Xb = finp('Xв')
Xp1 = finp('Xп1')
Xp2 = finp('Xп2')
delta = finp('delta')
delta1 = finp('поправка технического термометра')
delta2 = finp('поправка лабораторного термометра')
print('')
t1 = chan(Xp1, delta1)
print('t1 = Xп1 + (', delta1, ') =', t1, '( технический с поправкой', delta1, ')')
t2 = chan(Xp2, delta2)
print('t2 = Xп2 + (', delta2, ') =', t2, '( лабораторный с поправкой', delta2, ')')
a = veri (t1, t2, delta)
bord(Xn, Xb, Xp1)
lastkey()