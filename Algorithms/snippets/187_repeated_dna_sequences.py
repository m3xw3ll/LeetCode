def find_repeated_dna_sequences(s):
    seen = set()
    out = set()
    for i in range(0, len(s) - 9):
        if s[i:i+10] in seen:
            out.add(s[i:i+10])
        seen.add(s[i:i+10])
    return list(out)


print(find_repeated_dna_sequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))