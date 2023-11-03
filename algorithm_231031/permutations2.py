import itertools
from pprint import pprint

nums = [1, 2, 3]
def permute(nums):
    return [list(i) for i in itertools.permutations(nums)]

pprint(permute(nums), indent=4, width=50)