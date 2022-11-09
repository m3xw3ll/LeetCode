def fair_candy_swap(alice_sizes, bob_sizes):
    diff = (sum(alice_sizes) - sum(bob_sizes)) // 2
    alice_set = set(alice_sizes)

    for candy in bob_sizes:
        if candy + diff in alice_set:
            return [candy+diff, candy]


print(fair_candy_swap(alice_sizes=[1, 2], bob_sizes=[2, 3]))
