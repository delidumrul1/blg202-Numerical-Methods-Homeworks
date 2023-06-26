import numpy as np


def f(x):
    return 4*np.log(x)-x

def f_prime(x):
    return 4/float(x)-1


def newtons_method(x_0,ite_num):
    x_current=x_0
    x_next=x_0
    print("%10s%30s%30s%30s%30s" % ('iteration','x_current','f(x_current)','f_prime(x_current)','|x_current - x_next|'))
    for i in range(ite_num):
        x_next=x_current-f(x_current)/f_prime(x_current)
        print("%10d%30.15f%30.15f%30.15f%30.15f" % (i+1,x_current,f(x_current),f_prime(x_current),abs(x_current - x_next)))
        x_current=x_next



def secant_method(x_0,x_1,ite_num):
    x_previous=x_0
    x_current=x_1
    x_next=x_1
    print("%10s%30s%30s%30s%30s" % ('iteration','x_current','f(x_current)','f_prime(x_current)','|x_current - x_next|'))
    for i in range(ite_num):
        x_next = x_current - (f(x_current)*(x_current-x_previous)) / (f(x_current)-f(x_previous))
        print("%10d%30.15f%30.15f%30.15f%30.15f" % (i+1,x_current,f(x_current),f_prime(x_current),abs(x_current - x_next)))
        x_previous=x_current
        x_current=x_next





newtons_method(1,6)
secant_method(2,1,6)
    
    