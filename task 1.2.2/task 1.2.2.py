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
def calctn(betta, dt):
    print('формула для уравнения: dP = (Pн * betta * (tк - tн))/(1 + betta*tн)')
    print('преобразуем ее и получим формулу для tн:  1 + betta*tн = (Pн * betta * dt)/dP)')
    print('отсюда tн = ((Pн * betta * dt)/dP - 1)/betta')
    print('с учетом того, что Pк = Pн*n, dP = Pк-Pн = Pн * (n-1): tн = ((betta*dt)/(n-1) - 1)/betta')
    tn = ((betta*dt)/(n-1)-1)/betta
    print('tн =', tn)
    return tn

def calctk (betta, tn, n):
    print('Из Pк = n*Pн = Pн * (1 + betta*tк)/(1 + betta*tн) получим:')
    print('n = (1 + betta*tк)/(1 + betta*tн)')
    print('отсюда tк = ((n*(1 + betta*tн)) - 1)/betta')
    tk = ((n*(1+betta*tn)) - 1)/betta
    print('tк =', tk)
    return tk
def multP (Pn, n):
    Pk = Pn * n
    print('ранее нигде не было указано значение Pk = n*Pн, оно равно:', Pk)
    return Pk
rtask()
dt = finp('dt')
n = finp('n')
Pn = finp('Pн')
betta = finp('betta')
print('')
tn = calctn(betta, dt)
tk = calctk(betta, tn, n)
Pk = multP(Pn, n)
print('')
lastkey()