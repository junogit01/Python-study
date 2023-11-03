import collections

def group_anagrams(strs:list[str]) -> list[list[str]]:
    anagrams = collections.defaultdict(list)
    for i in strs:
        anagrams["".join(sorted(i))].append(i)
    return list(anagrams.values())

group_anagrams(["eat","tea","tan","ate","nat","bat"])