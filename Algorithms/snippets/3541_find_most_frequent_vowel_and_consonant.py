from collections import Counter

def max_freq_sum(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = Counter(s)

    v_dict = [v for k, v in counter.items() if k in vowels]
    c_dict = [v for k, v in counter.items() if k not in vowels]

    if not v_dict: v_dict.append(0)
    if not c_dict: c_dict.append(0)

    return max(v_dict) + max(c_dict) if len(s) != 0 else 0


print(max_freq_sum("aeiaeia"))