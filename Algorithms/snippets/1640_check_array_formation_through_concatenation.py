def can_form_array(arr, pieces):
    out = list()
    dict = {x[0]: x for x in pieces}

    for i in arr:
        out += dict.get(i, [])
    return out == arr


print(can_form_array(arr=[15, 88], pieces=[[88], [15]]))
