def can_construct(ransom_note, magazine):
    for char in ransom_note:
        if ransom_note.count(char) > magazine.count(char):
            return False
    return True


print(can_construct('a', 'b'))
