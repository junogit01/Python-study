import itertools
from pprint import pprint
n, k = [4, 2]
def combine(n, k):
    return [list(i) for i in itertools.combinations(range(1, n+1), k)]

pprint(combine(n, k), indent=4, width=20)