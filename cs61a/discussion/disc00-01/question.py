def wears_jacket(temp,raining):
    """
    >>> wears_jacket(90,False)
    False
    >>> wears_jacket(40,False)
    True
    >>> wears_jacket(100,True)
    True
    """
    return temp<60 or raining
def handle_overflow(s1,s2):
    """
    >>> handle_overflow(27,15)
    No overflow
    >>> handle_overflow(35,29)
    Move to Section 2:1
    >>> handle_overflow(20,32)
    Move to Section 1:10
    >>> handle_overflow(35,30)
    No space left in either section
    """
    if s1<30 and s2<30 :
        print('No overflow')
    elif s1<30 and s2>30:
        rema=30-s1
        print("Move to Section 1:",rema,sep='')
    elif s1>30 and s2<30:
        rema=30-s2
        print('Move to Section 2:',rema,sep='')
    else :
        print("No space left in either section")
def square(x):
    return x*x

def so_slow(num):
    x=num
    while x>0:
        x=x+1
    return x/0

from math import sqrt
def is_prime(n,i=2):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    while i<sqrt(n):
        if n%i==0:
            return False
        else :
            i=i+1
    return True
def keep_ints(cond,n,i=1):
    """print out all integers 1...i..n where cond(i) is True

    >>> def is_even(x):
    ...    # Even number have remainder 0
    ...    return x % 2==0
    >>> keep_ints(is_even,5)
    2
    4
    """
    while i<=n:
        if cond(i):
            print(i)
        i=i+1
def keep_ints1(n):
    """Return a function which takes one parameter cond and prints out 
    all intefers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...    #Even numbers have remainder 0 when diveded by 2.
    ...    return x%2==0
    >>> keep_ints1(5)(is_even)
    2
    4
    """
    def inner(cond,i=1):
        while i<=n:
            if cond(i):
                print(i)
            i=i+1
    return inner
