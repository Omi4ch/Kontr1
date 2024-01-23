class MyError (Exception):
    pass

def decorator (f):
    def obertka (t, V1, V2):
        f(V1, V2, t)
        S = (V2**2 - V1**2)/(2*((V2 - V1)/t))
        print (S)
    return obertka

@decorator
def f (V1, V2, t):
    a = (V2 - V1)/t
    print (a)

try:
    V2 = int(input ())
    V1 = int(input ())
    t = int(input ())
    if (t < 0):
        raise MyError ('t должно быть больше 0')
    f(V1, V2, t)
except ValueError:
    print ('Надо цифры')
except MyError:
    print ('t должно быть > 0')