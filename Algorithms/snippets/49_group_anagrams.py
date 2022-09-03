from collections import defaultdict

def group_anagrams(strs):
    lookup = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(list(word)))
        lookup[key].append(word)
    return [word for word in lookup.values()]

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))