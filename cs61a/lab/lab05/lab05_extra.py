""" Optional questions for Lab 05 """

from lab05 import *

# Shakespeare and Dictionaries
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
# My stupid solution:

    table = {}
    prev = '.'
    table[prev]=[tokens[0]]
    for word in tokens:
        if word not in table:
            table[word]=[]
            for i in range(len(tokens)-1):
                if tokens[i]==word:
                    table[word]+=[tokens[i+1]]
    return table
    """
# The PDF solution is so clever:
    table={}
    prev='.'
    for word in tokens:
        if prev not in table:
            table[prev]=[]
        table[prev]+=[word]
        prev=word
    return table
    """
def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'
    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        result+=word+' '
        word=random.choice(table[word])
    return result.strip() + word

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Uncomment the following two lines
#tokens = shakespeare_tokens()
#table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)

# Q6
def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    spout=[tree(i) for i in vals]
    if is_leaf(t):
        return tree(label(t),spout)
    else:
        return tree(label(t),[sprout_leaves(b) for b in branches(t)])
# Q7
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    # I saw the solution and wasted a lot of time ,but finish it at last whatever,don't be afraid next time
    if not t1:
        return t2
    if not t2:
        return t1
    corresponding_branches1=branches(t1)
    corresponding_branches2=branches(t2)
    if len(branches(t1)) > len(branches(t2)):
        corresponding_branches2 += [None for i in range(len(corresponding_branches2),len(corresponding_branches1))]
    elif len(corresponding_branches2)>len(corresponding_branches1):
        corresponding_branches1 += [None for i in range(len(corresponding_branches1),len(corresponding_branches2))]
    return tree((label(t1)+label(t2)),[add_trees(b1,b2) for b1,b2 in zip(corresponding_branches1,corresponding_branches2)])

    """
    if not  t1:
        return t2
    if not t2:
        return t1
    new_label=label(t1)+label(t2)
    t1_children,t2_children = branches(t1) , branches(t2)
    length_t1, length_t2 = len(t1_children),len(t2_children)
    if length_t1<length_t2:
        t1_children += [None for _ in range(length_t1, length_t2)]
    elif len(t1_children)>len(t2_children):
        t2_children += [None for _ in range(length_t2, length_t1)]
    return tree(new_label, [add_trees(child1,child2) for child1,child2 in zip(t1_children,t2_children)])
    """
