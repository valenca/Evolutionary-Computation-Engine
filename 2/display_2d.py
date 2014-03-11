"""Visualization 2D."""

__author__ = 'Ernesto Costa'
__date__ = 'February 2014'

from  math import sqrt, sin, cos, pi
import matplotlib.pyplot as plt

def display(f, x_min, x_max, delta=0.001):
    """Compute valuesw and display."""
    x = list(drange(x_min, x_max,delta))
    y = [f(i) for i in x]
    plt.title(f.__name__)
    plt.grid(True)
    plt.xlabel('X')
    plt.ylabel('Y= '+f.__name__ + '(X)')
    plt.plot(x,y, 'r')
    plt.show()
    
def display_data(data):
    """Plot the data"""
    x = list(range(len(data)))
    plt.grid(True)
    plt.plot(x,data, 'r')
    plt.show()   
 
  
def drange(start,stop,step=0.1):
    """ range for floats."""
    number = start
    while number < stop:
        yield number
        number += step
        
def f1(x):
    """max=3 at x=-1 in [-2,2]."""
    return x**3 - 2*x + 2

def f2(x):
    """ min = 0,. [-4,2]."""
    return x**2 + 2 * x + 1

def f3(x):
    """max = 1 at x=0. [-2,2]"""
    return 1 / (1 + x**2)

def f4(x):
    """Oscilates. Max = 1."""
    return sin(x)/x

def f5(x):
    """Max at x= pi/3, Min at x= 5*pi/3."""
    return 2* sin(x) + sin(2*x)

def f6(x):
    """Max = 1"""
    return 1 - x**2

def michalewicz(x):
    """
    domain = [[-1,2]]
    x= 1.85 -> max = 2.85
    """
    return  x * sin(10 * pi * x) + 1.0


if __name__ == '__main__':
    display(michalewicz,-1,2)
    display(f5,-10,10)
