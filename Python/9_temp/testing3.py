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

def rotate_matrix(matrix):
    matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3], matrix[1][3], matrix[2][3], matrix[3][3], matrix[3][2], matrix[3][1], matrix[3][0], matrix[2][0], matrix[1][0] = matrix[0][1], matrix[0][2], matrix[0][3], matrix[1][3], matrix[2][3], matrix[3][3], matrix[3][2], matrix[3][1], matrix[3][0], matrix[2][0], matrix[1][0], matrix[0][0]
    matrix[1][1], matrix[1][2], matrix[2][2], matrix[2][1] = matrix[2][1], matrix[1][1], matrix[1][2], matrix[2][2] 
    return matrix

def res_matrix(key_matrix, key_matrix_r, encrp_matrix):
    outer_matrix = []
    for i in range(4):
        inner_matrix = []
        for j in range(4):
            inner_matrix.append( encrp_matrix[i][j] ^ key_matrix_r[i][j] ^ key_matrix[i][j] ^ 4 )
        outer_matrix.append(inner_matrix)
    return outer_matrix

if __name__ == "__main__":

    encrp_str = input()
    encrp_str_len = len(encrp_str)
    encrp_str = pad_encrp_str(encrp_str_len, encrp_str)

    key = input()   
    key_len = len(key)
    key = pad_key(key_len, key)
    key_matrix = create_matrix(key)
    key_matrix_r = rotate_matrix(key_matrix)

    if encrp_str_len < 16:
        encrp_matrix = create_matrix(encrp_str)
        res_matrix = res_matrix(key_matrix, key_matrix_r, encrp_matrix)
        print(res_matrix)
        result = ""
        for rows in res_matrix:
            for data in rows:
                result += chr(data)
        print(result)
    
    elif encrp_str_len > 16:
        encrp_matrix1 = create_matrix(encrp_str[:16])
        encrp_matrix2 = create_matrix(encrp_str[16:])
        
        res_matrix1 = res_matrix(key_matrix, key_matrix_r, encrp_matrix1)
        res_matrix2 = res_matrix(key_matrix, key_matrix_r, encrp_matrix2)

        result = ""
        for rows in res_matrix1:
            for data in rows:
                result += chr(data)
        for rows in res_matrix2:
            for data in rows:
                result += chr(data)
        
        print(result)