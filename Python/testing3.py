def create_matrix(string):
    outer_matrix = []
    n = 0
    for i in range(4):
        inner_matrix = []
        for j in range(4):
            inner_matrix.append(ord(string[n]))
            n += 1
        outer_matrix.append(inner_matrix)
    return outer_matrix

# padding key
def pad_key(key_len, key):
    if key_len < 16:
        key += " "* (16 - key_len)
    return key

# padding encrpty string
def pad_encrp_str(encrp_str_len, encrp_str):
    if encrp_str_len > 16 and encrp_str_len < 32:
        encrp_str += " "* (32 - encrp_str_len)
    elif encrp_str_len < 16:
        encrp_str += " "* (16 - encrp_str_len)
    return encrp_str

if __name__ == "__main__":

    encrp_str = input()
    encrp_str_len = len(encrp_str)
    encrp_str = pad_encrp_str(encrp_str_len, encrp_str)

    key = input()   
    key_len = len(key)
    key = pad_key(key_len, key)
    key_matrix = create_matrix(key)

    print(key_matrix)
