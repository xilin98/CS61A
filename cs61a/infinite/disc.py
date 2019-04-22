def gen_all_items(lst):
    """
    >>> nums=[[1,2],[3,4],[[5,6]]]
    >>> num_iters= [iter(l) for l in nums]
    >>> list(gen_all_items(num_iters))
    [1, 2, 3, 4, [5, 6]]
    """
    for i in lst:
        yield from i
