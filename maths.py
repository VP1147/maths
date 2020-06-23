# Vp1147's math tests | march 2020

import math

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
	return v - math.log(n)

def Euler(c): # Calcula o número de Euler (e) pela série de Taylor
	v = 0
	for n in range(0,10**c):
		v += 1/math.factorial(n)
	return v

def sci(x): # conversor pra notação científica
    e = 0
    while x >= 10 or x < 1:
        if x < 1:
            x = x*10
            e -= 1
        elif x >= 10:
            x = x/10
            e += 1
    return x,e  # formato: x*10^e

def SnPA(a1,n,r): # Soma de 'n' termos de uma PA
    an = a1+(n-1)*r
    Sn = ((a1+an)*n)/2
    return (an,Sn) # Retorna tupla

def SnPG(a1,n,q): # Soma de 'n' termos de uma PG finita
    an = a1*(q**(n-1))
    Sn = (a1*((q**n)-1))/(q-1)
    return (an,Sn) # Retorna tupla
