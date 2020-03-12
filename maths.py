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