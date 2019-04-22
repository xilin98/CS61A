def ensure_consistency(fn):
    """Return a function that calls fn on its argument,
    returns fn's return value, and return None if fn's
    return value si diffirent from any of its previous return
    values for those same argument .Also return None if
    more than 20 calls are made.

    >>> def consistency(x):
    ...     return x
    ...
    >>> lst=[1, 2, 3]
    >>> def inconsistent(x):
    ...     return x+lst.pop()
    ...
    >>> a = ensure_consistency(consistency)
    >>> a(5)
    5
    >>> a(5)
    5
    >>> a(6)
    6
    >>> a(6)
    6
    >>> b = ensure_consistency(inconsistent)
    >>> b(5)
    8
    >>> b(5)
    None
    >>> b(6)
    7
    """
    n=20
    z={}
    def helper(x):
        nonlocal n
        n-=1
        if n<0:
            return print(None)
        val= fn(x)
        if x not in z:
            z[x]=[val]
        if z[x]==[val]:
            return val
        else:
            z[x]=z[x]+[val]
            return print(None)
    return helper
