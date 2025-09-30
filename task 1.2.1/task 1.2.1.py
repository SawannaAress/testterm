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
def testval():
    ver = input('Необходимо вывести проверочные значения? y/n ')
    if ver == 'y':
        a = 1
    else:
        a = 0
    return a
def calPn (P, betta, tk, tn):
    print ('dP = Pк - Pн = (Pн * betta * (tк - tн))/(1+betta*tн)')
    print('отсюда:')
    print('Pн = (dP * (1+betta*tн))/(betta*(tк - tн))')
    Pn = (P * (1+betta*tn))/(betta*(tk-tn))
    print('указанное давление устанавливается при t = Xнп =', tn)
    print('Pн =', Pn)
    return Pn
def calP1 (Pn, betta, t1, tn):
    print('Из: Pк = Pн*(1+betta*tк)/(1+betta*tн)')
    print('найдем искомую P, как Pк при tк = t1 =', t1)
    P1 = Pn*(1+betta*t1)/(1+betta*tn)
    print('P1 =', P1)
    return P1
rtask()
t1 =finp('t1')
Xnp = finp('Xнп')
Xvp = finp('Xвп')
P = finp('P')
betta = finp('betta')
a = testval()
print('')
Pnp = calPn(P, betta, Xvp, Xnp)
P1 = calP1(Pnp, betta, t1, Xnp)
if a == 1:
    Pktest = Pnp*(1+betta*(Xvp))/(1+betta*Xnp)
    print('по формуле для Pк, Pк=', Pktest)
    print('Отсюда dP =', Pktest - Pnp)
print('')
print('Те же расчеты для t+273, если betta для К:')
t11 = t1+273
Xnp1 = Xnp+273
Xvp1 = Xvp+273
Pnp1 = calPn(P, betta, Xvp1, Xnp1)
P11 = calP1(Pnp1, betta, t11, Xnp1)
if a == 1:
    Pktest1 = Pnp1*(1+betta*(Xvp1))/(1+betta*Xnp1)
    print('По формуле для Pк: =', Pktest1)
    print ('Отсюда dP =', Pktest1-Pnp1)
lastkey()
