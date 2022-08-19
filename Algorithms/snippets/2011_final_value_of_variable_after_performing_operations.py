def final_value_after_operations(operations):
    return sum(map(lambda x: 1 if "++" in x else -1, operations))


print(final_value_after_operations(["--X", "X++", "X++"]))
