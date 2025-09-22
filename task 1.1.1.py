def finps(s):
    try:
        a = float(input('вещественное число ' + s+' ' ))
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
def det(Xout, a, t, tvs):
    dt = Xout*a*(t-tvs)
    return dt
Xvs = finp('Xвс')
Xp = finp('Xп')
Xpo = finp('Xпог')
alphas1 = 0.000168
alphas2 = 0.000158
Xout = max((Xp - Xpo), 0)
dt1 = det(Xout, alphas1, Xp, Xvs)
dt2 = det(Xout, alphas2, Xp, Xvs)
t1 = Xp + dt1
t2 = Xp + dt2
print('Для a = 0.000168, dt=', dt1, '; t =', t1)
print('Для a = 0.000158, dt=', dt2, '; t =', t2)
lastkey()