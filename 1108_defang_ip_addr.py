def defang_id_addr(address):
    return address.replace('.', '[.]')


print(defang_id_addr('1.1.1.1'))