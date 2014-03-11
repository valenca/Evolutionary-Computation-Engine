import matplotlib.pyplot as pl
from random import sample
from math import sin

def display(f,x):
	y=[f(i) for i in x]
	y1=[derive(f,i) for i in x]
	pl.plot(x,y)
	#pl.plot(x,y1)
	pl.axis([x[0],x[-1],min(y)-0.5,max(y)+0.5])
	pl.axhline(0, color='black')
	pl.axvline(0, color='black')
	pl.show()

def drange(start, stop, step):
	x = start
	while True:
		if x >= stop: return
		yield x
		x += step

def f1(x): return (x**3)-(2*x)+2
def f2(x): return (x**2)+(2*x)+1
def f3(x): return 1/(1+(x**2))
def f4(x): return sin(x)/x
def f5(x): return (2*sin(x))+(sin(2*x))
def f6(x): return 1-(x**2)
def derive(f,x,d=0.0001): return (f(x+d)-f(x))/d

def ascendingGrad(f,x,a,t,s):
	l=[[],[]]
	for i in range(t):
		if(abs(derive(f,s))<0.0000001): break
		s=s+(a*derive(f,s))
		l[0].append(s);l[1].append(f(s))
	pl.plot(l[0],l[1],sample(['r','g','b','c','m','y','k'],1)[0]+'.')
	return s
	
def ascendingGradRR(f,x,a,n,t):
	s=sample(x,n)
	b=sample(x,1)[0]
	for i in range(n):
		h=ascendingGrad(f,x,a,t,s[i])
		if f(h)>f(b): b=h
	return "   x: "+str(round(b,5))+"\nf(x): "+str(round(f(b),5))

if __name__ == "__main__":
	x=list(drange(-30,30,0.001))
	f=f4
	print(ascendingGradRR(f,x,0.1,1,100))
	display(f,x)
