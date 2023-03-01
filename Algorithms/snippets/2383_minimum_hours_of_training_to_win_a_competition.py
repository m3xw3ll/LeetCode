def min_number_of_hours(initial_energy, initial_experience, energy, experience):
    needed_energy = sum(energy) - initial_energy + 1
    needed_exp = 0
    hours = 0
    for exp in experience:
        if initial_experience <= exp:
            needed_exp += exp - initial_experience + 1
            initial_experience = exp + 1
        initial_experience += exp

    hours += needed_energy if needed_energy > 0 else 0
    hours += needed_exp if needed_exp > 0 else 0
    return hours


print(min_number_of_hours(initial_energy = 1, initial_experience = 1, energy = [1, 1, 1, 1], experience = [1, 1, 1, 50]))
