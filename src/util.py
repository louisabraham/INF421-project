"""
Useful functions for other modules.
"""


import sys

try:
    from tqdm import tqdm

    def progress_bar(iterable, total=None):
        return tqdm(iterable, total=total)

except ImportError:
    from time import time

    print('Missing tqdm module, alternative logging system activated')
    print('You can install tqdm with `python3 -m pip install tqdm`')

    def progress_bar(iterable, total=None):
        if total is None:
            total = len(iterable)

        dbt = time()
        for i, line in zip(range(total), iterable):
            yield line
            if (i - 1) * 100 // total < i * 100 // total:
                print('\r%u%%' % (i * 100 // total), end='', file=sys.stderr)
        print('\r100%', file=sys.stderr)

        print('Finished in %u seconds' % (time() - dbt), file=sys.stderr)


from functools import wraps
from collections import Hashable
from time import time


def memoize_generator(f):
    """
    Note this original decorator.
    We took the id to identify non-hashables
    objects (like the graph).
    """
    @wraps(f)
    def g(*args):
        targs = tuple(a if isinstance(a, Hashable) else id(a)
                      for a in args)
        if not targs in g.mem:
            ans = f(*args)
            next(ans)
            g.mem[targs] = ans
        return g.mem[targs]
    g.mem = {}

    def clean():
        for i in g.mem:
            g.mem[i].close()
        g.mem = {}
    g.clean = clean

    return g


def timeit(f):
    """
    Decorator to time functions
    """
    @wraps(f)
    def tf(*args, **kwargs):
        d = time()
        ans = f(*args, **kwargs)
        if timeit.activated:
            print('%s seconds' % (time() - d), file=sys.stderr)
        return ans

    return tf

timeit.activated = False
