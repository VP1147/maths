def DivUtils(dd,ds,x=0,c=0): # dd - Dividendo | ds - Divisor
	while (x+ds) <= dd:
		c+=1
		x+=ds
	r = dd-x
	return c,r