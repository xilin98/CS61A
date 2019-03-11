def cube(k):
    return pow(k,3)

def summation(n,term):
    """Sum the first n term of sequence

    >>> summation(5,cube)
    225
    """
    total,k=0,1
    while k<=n:
        total,k = total + term(k) , k+1
    return total
def make_adder(n):
    """return a function that takes one argument and returns k+n.
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k+n
    return adder


