def sum_nature(n):
    """ compute the sum of natural numbers up to n

    >>> sum_nature(100)
    5050
    """
    total,k=0,1
    while k<=n:
        total,k=total+k,k+1
    return total
def sum_cub(n):
    """ compute the sum of the cubes of natural number up to n

    >>> sum_cub(100)
    25502500
    """
    total,k=0,1
    while k<=n:
        total,k=total+k*k*k,k+1
    return total
def sum_pi(n):
    """ compute the sum of terms in the series whichc converges to pi very slowly

    >>> sum_pi(100)
    3.1365926848388144
    """
    total,k=0,1
    while k<=n:
        total,k=total+8/((4*k-3)*(4*k-1)),k+1
    return total
def summation(n,term):
    total,k=0,1
    while k<=n:
        total,k=total+term(k),k+1
    return total

def cube(x):
    return x*x*x

def sum_cubes(n):
    return summation(n,cube)

result = sum_cubes(3)

""" Generlization"""
from math import pi,sqrt

def area(r,shape_constant):
    assert r>0, 'A length must be positive'
    return r*r*shape_constant

def area_square(r):
    return area(r,1)

def area_circle(r):
    return area(r,pi)

def are_hexagon(r):
    return area(r,3*sqrt(3)/2)

def improve(update,close,guess=1):
    while not close(guess):
        guess=update(guess)
    return guess

def golden_update(guess):
    return 1/guess +1

def square_close_to_successor(guess):
    return approx_eq(guess*guess,guess+1)

def approx_eq(x,y,tolerance=1e-15):
    return abs(x-y)<tolerance

