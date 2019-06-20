class Tree:
    def __init__(self,label,branches=()):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches=branches
    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(self.label)
    def __is_leaf(self):
        return not self.branches
def make_max_finder():
    """
    >>> m = make_max_finder()
    >>> m([5,7,6])
    7
    >>> m([1,2,3])
    7
    >>> m([9])
    9
    >>> m2 = make_max_finder()
    >>> m2([1])
    1
    """
    max_num=0
    def finder(lst):
        nonlocal max_num
        max_num=max(max(lst),max_num)
        return max_num
    return finder

def filter_tree(t, fn):
    """
    >>> t = Tree(1, [Tree(2), Tree(3,[Tree(4)]),Tree(6,[Tree(7)])])
    >>>filter_tree(t,lambda x: x%2!=0)
    >>> t
    Tree(1,[Tree(3)])
    >>> t2 = Tree(2, [Tree(3), Tree(4), Tree(5)])
    >>> filter_tree(t2, lambda x: x !=2)
    >>> t2
    Tree(2)
    """
    
