#########
# Trees #
#########

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

######################
# Required questions #
######################

def replace_leaf(t, old, new):
    """Returns a new tree where every leaf value equal to old has
    been replaced with new.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('loki')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        loki
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    if label(t)==old and is_leaf(t):
        new_label=new
    else:
        new_label=label(t)
    return tree(new_label,[replace_leaf(b,old,new) for b in branches(t)])
    # From Guohang Ma
    if is_leaf(t) and label(t)==old:
        return tree(new)
    return tree(label(t),[replace_leaf(b,old,new) for b in branches(t)])
# Mobiles

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    assert is_side(left), "left must be a side"
    assert is_side(right), "right must be a side"
    return ['mobile', left, right]

def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    """Select the left side of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]

def right(m):
    """Select the right side of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    assert is_mobile(mobile_or_weight) or is_weight(mobile_or_weight)
    return ['side', length, mobile_or_weight]

def is_side(s):
    """Return whether s is a side."""
    return type(s) == list and len(s) == 3 and s[0] == 'side'

def length(s):
    """Select the length of a side."""
    assert is_side(s), "must call length on a side"
    return s[1]

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    assert is_side(s), "must call end on a side"
    return s[2]

def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    return ["weight",size]

def size(w):
    """Select the size of a weight."""
    assert is_weight(w), 'must call size on a weight'
    return w[1]

def is_weight(w):
    """Whether w is a weight."""
    return type(w) == list and len(w) == 2 and w[0] == 'weight'

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)

def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a weight"
        return total_weight(end(left(m))) + total_weight(end(right(m)))

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    if is_weight(m):
        return True
    elif length(left(m))*total_weight(end(left(m)))!=length(right(m))*total_weight(end(right(m))):
        return False
    else:
        return balanced(end(left(m))) and balanced(end(right(m)))

    # from guohangma
    if is_weight(m):
        return True
    else:
        left_end,right_end=end(left(m)),end(right(m))
        torque_left=length(left(m))*total_weight(left_end)
        torque_right=length(right(m))*total_weight(right_end)
        return torque_left==torque_right and balanced(left_end) and balanced(right_end)
def totals_tree(m):
    """Return a tree representing the mobile with its total weight at the root.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    """
    if is_weight(m):
        return tree(total_weight(m))
    return tree(total_weight(m),[totals_tree(end(left(m))),totals_tree(end(right(m)))])

    # The PDF solution
    if if_weight(m):
        return tree(size(m))
    else:
        branches=[totals_tree(end(f(m))) for f in [left,right]]
        return tree(sum([label(b) for b in branches]),branches)
# Mutable functions in Python

def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    dict_for_string={}
    def specific_string(s):
        nonlocal dict_for_string  # not need it
        if s in dict_for_string:
            dict_for_string[s]+=1
        else:
            dict_for_string[s]=1
        return dict_for_string[s]
    return specific_string

#The PDF solution
    m={}
    def counter(key):
        m[key] = m.get(key,0)+1
        return m[key]
    return counter

#The solution 2
    def counter(s):
        if not s in m:
            m[s]=0
        m[s]+=1
        return m[s]
    return counter
def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    t=0
    k=1
    def fib():
        nonlocal t, k
        rv = t    # It is magic don't touch it !!!
        t, k=k, t+k
        return rv
    return fib
def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    """
    wrong_password_list=[]
    def withdraw(amount,typed_password):
        nonlocal balance,wrong_password_list
        if len(wrong_password_list)==3:
            a=str(wrong_password_list[0])
            b=str(wrong_password_list[1])
            c=str(wrong_password_list[2])             # There is stupid
            return "Your account is locked. Attempts: ['"+a+"', '"+b+"', '"+c+"']"    #It's magic ,don't touth it
        if typed_password!= password:
            wrong_password_list+=[typed_password]
            return 'Incorrect password'
        else:
            if amount>balance:
                return 'Insufficient funds'
            balance-=amount
            return balance
    return withdraw
    """
    # The PDF solution
    attempts=[]
    def withdraw(amount,password_attempt):
        nonlocal balance
        if len(attempts)==3:
            return 'Your account is locked. Attempts: '+str(attempts)
        if password_attempt != password:
            attempts.append(password_attempt)
            return 'Incorrect password'
        if amount > balance :
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    test=withdraw(0,old_password)
    if type(test)==str:
        return test
    else:
        def new_withdraw(amount,password):
            if password==new_password:
                password=old_password
            return withdraw(amount,password)
    return new_withdraw
# Generators

def generate_paths(t, x):
    """Yields all possible paths from the root of t to a node with the label x
    as a list.

    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> print_tree(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]
    >>> t2 = tree(0, [tree(2, [t1])])
    >>> print_tree(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    # It's too hard for me to figure it out
    # The Lazy Algorithm maybe useful here
    if label(t)==x:
        yield [x]
    for b in branches(t):
        for path in generate_paths(b,x):
            yield [label(t)]+path
    # I spend a lot of time here

###################
# Extra Questions #
###################



def str_interval(x):
        return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]
def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]
def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x)*lower_bound(y)
    p2 = lower_bound(x)*upper_bound(y)
    p3 = upper_bound(x)*lower_bound(y)
    p4 = upper_bound(x)*upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    "*** YOUR CODE HERE ***"
    lower=lower_bound(x)-upper_bound(y)
    upper=upper_bound(x)-lower_bound(y)
    return interval(lower,upper)

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    "*** YOUR CODE HERE ***"
    assert lower_bound(y)*upper_bound(y)>0 ,"Can't span a interval that span 0"
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(2, 1) # Replace this line!
    r2 = interval(1, 5) # Replace this line!
    return r1, r2

def multiple_references_explanation():
    return """The multiple reference problem...""" "because div_interval(r1,r1)!=1 and sub_interval(r1,r1)!=0"
# The PDF solution:
""" The multiple reference problem exists. The ture value within a particular interval is fixed (though unknown). Nestted
combinations that refer to the same interval twice may  in intervals that are larger than they should be.

Consider the case of i*i ,where i is an interval from -1 to 1. No value within this interval, when squared ,will give a negetive
result. However our mul_interval function will allow us to choose 1 from the first reference to i and -1 for the second ,giving an
errorneous lower bound of -1.

Hence, a program like par2 is better than par1 because it never combines the same interval more than once.
"""
def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    def f(t):
        return a*t*t+b*t+c
    left_end_point=lower_bound(x)
    right_end_point=upper_bound(x)
    middle_point=-b/(2*a)
    v1=f(left_end_point)
    v2=f(right_end_point)
    v3=f(middle_point)       # Here can replaced by a map function, let it more concise
    if middle_point>left_end_point and middle_point<right_end_point:
        return interval(min(v1,v2,v3),max(v1,v2,v3))
    else:
        return interval(min(v1,v2),max(v1,v2))

# The guohangma's solution
    f=lambda x: a*x*x + b*x +c
    extreme=-b/(2*a)
    l,u,e=map(f,(lower_bound(x),upper_bound(x),extreme))
    if extreme>lower_bound(x) and extreme<upper_bound(x):
        return interval(min(l,u,e),max(l,u,e))
    else:
        return interval(min(l,u),max(l,u))
