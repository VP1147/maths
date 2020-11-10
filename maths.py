# Vp1147's math tests | march 2020

import math as m

def DivUtils(dd,ds,x=0,c=0): # dd - Dividendo | ds - Divisor
	while (x+ds) <= dd:
		c+=1
		x+=ds
	r = dd-x
	return c,r

def EulerMasche(c): # Calcula a constante de Euler-Mascheroni
	v = 0
	for n in range(1,10**c):
		v += 1/n
	return v - m.log(n)

def Euler(c): # Calcula o número de Euler (e) pela série de Taylor
	v = 0
	for n in range(0,10**c):
		v += 1/m.factorial(n)
	return v

def sci(x): # conversor pra notação científica.
    e = 0
    while x >= 10 or x < 1:
        if x < 1:
            x = x*10
            e -= 1
        elif x >= 10:
            x = x/10
            e += 1
    return x,e  # formato: x*10^e

def SnPA(a1,n,r): # Soma de 'n' termos de uma PA.
    an = a1+(n-1)*r
    Sn = ((a1+an)*n)/2
    return (an,Sn) # Retorna tupla.

def SnPG(a1,n,q): # Soma de 'n' termos de uma PG finita.
    an = a1*(q**(n-1))
    Sn = (a1*((q**n)-1))/(q-1)
    return (an,Sn) # Retorna tupla.

def root(x,n):  # Recebe 'n' e 'x', retorna
                # a raíz de índice 'n' de 'x'.
    return x**(1./n)

def Tartaglia(a,b,c,d): # Resolve equações cúbicas gerais
                        # ax³ + bx² + cx + d pelo método
                        # de de Cardano-Tartaglia. Retorna
                        # os complexos 'x1', 'x2', 'x3'.

    p,q = (c/a)-(b**2/3*a**2), (d/a)-((b*c)/3*a**2)+((2*b**3)/(27*a**3))

    t1 = -(b/(3*a))
    t2,t3 = root((-(q/2))+root((q**2/4)+(p**3/27),2),3), root((-(q/2))-root((q**2/4)+(p**3/27),2),3)
    t4,t5 = ((-1/2)+((root(-1,2)*root(3,2))/2)), ((-1/2)-((root(-1,2)*root(3,2))/2))

    x1 = t1+t2+t3
    x2 = t1+t4*t2+t5*t3
    x3 = t1+t5*t2+t4*t3
    return x1, x2, x3

