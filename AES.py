# Matriu de sub_bytes
Sbox = [
            0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
            0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
            0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
            0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
            0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
            0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
            0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
            0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
            0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
            0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
            0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
            0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
            0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
            ]
mixmod = [100011011]


#
def hex_to_bin(hexnum):
    if type(hexnum) == str:
        hexnum = (int(hexnum, 16))
    return bin((hexnum))[2:].zfill(8)

def bin_to_hex(binnum):
    return hex(int(binnum, 2))[2:].zfill(2)

def hex_to_dec(hexnum):
    if type(hexnum) == str:
        hexnum = int(hexnum, 16)
    return (hexnum)

def dec_to_hex(decnum):
    return hex(decnum)[2:].zfill(2)

def sub_bytes(matrix):
    for i in range(4):
        for j in range(4):
            matrix[i][j] = hex(Sbox[int(matrix[i][j], 16)])[2:].zfill(2)
    return matrix

def add_round_key(matrix, key):
    for i in range(4):
        for j in range(4):
            matrix[i][j] = xor(matrix[i][j], key[i][j])
    return matrix

def shift_rows(matrix):
    for i in range(4):
        for j in range(i):
            matrix[i].append(matrix[i].pop(0))
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print()

def mul2(hexnum):
    binnum = hex_to_bin(hexnum)
    res = binnum + '0'
    if binnum[0] == '0':
        res = res[1:]
        res = bin_to_hex(res)
    if binnum[0] != '0':
        res = xor_bin(res, "100011011")

    return (res)
def mul3(hexnum):
    return xor(hexnum, (mul2(hexnum)))

def xor(hexnum1, hexnum2):
    bin1, bin2 = hex_to_bin(hexnum1), hex_to_bin(hexnum2)
    #XOR bin1 and bin2
    res = ''
    for i in range(8):
        if bin1[i] == bin2[i]:
            res += '0'
        else:
            res += '1'
    return bin_to_hex(res)

def xor_bin(bin1, bin2):
    #XOR bin1 and bin2
    res = ''
    for i in range(max(len(bin1), len(bin2))):
        if bin1[i] == bin2[i]:
            res += '0'
        else:
            res += '1'
    return bin_to_hex(res)

mix_matrix = [[2,3,1,1], [1,2,3,1], [1,1,2,3], [3,1,1,2]]

def matxcolumna(column):
    res = ['00', '00', '00', '00']
    for i in range(4):
        total = 0x00
        for j in range(4):
            if mix_matrix[i][j] == 1:
                total = xor(total, (column[j]))
            elif mix_matrix[i][j] == 2:
                total = xor(total, mul2(column[j]))
            elif mix_matrix[i][j] == 3:
                total = xor(total, mul3(column[j]))            

        res[i] = total
    return res


def mix_columns(matrix):
    res = []
    column = []
    for i in range(4):
        column = []
        for j in range(4):
            column.append(matrix[j][i])
        res.append(matxcolumna(column))
    #Trasnspose the matrix res
    res = [[res[j][i] for j in range(len(res))] for i in range(len(res[0]))]
    return res
        
#key_expansion for matrix 4x4

Rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]

for i in range(len(Rcon)):
    Rcon[i] = dec_to_hex(Rcon[i])



def key_expansion(key):
    #Transpose key
    key = [[key[j][i] for j in range(len(key))] for i in range(len(key[0]))]
    for i in range(4, 44):
        if i % 4 == 0:
            #RotWord
            temp = key[i-1].copy()
            temp.append(temp.pop(0))
            #SubWord
            for j in range(4):
                temp[j] = hex(Sbox[int(temp[j], 16)])[2:].zfill(2)
            #Rcon
            temp[0] = xor(temp[0], Rcon[int(i/4) - 1])
            key.append([])
            for j in range(4):
                key[i].append(xor(key[i-4][j], temp[j]))
        else:
            key.append([])
            for j in range(4):
                key[i].append(xor(key[i-4][j], key[i-1][j]))      
    return key   




input_matrix = [[0x32, 0x88, 0x31, 0xe0], [0x43, 0x5a, 0x31, 0x37], [0xf6, 0x30, 0x98, 0x07], [0xa8, 0x8d, 0xa2, 0x34]]
key_matrix = [[0x2b, 0x28, 0xab, 0x09], [0x7e, 0xae, 0xf7, 0xcf], [0x15, 0xd2, 0x15, 0x4f], [0x16, 0xa6, 0x88, 0x3c]]

for i in range(4):
    for j in range(4):
        input_matrix[i][j] = dec_to_hex(input_matrix[i][j])
        key_matrix[i][j] = dec_to_hex(key_matrix[i][j])


# sum the values of the matrix with the key matrix

# xor input and key matrix
m1 = add_round_key(input_matrix, key_matrix)


print_matrix(m1)

print("Key Expansion", key_expansion(key_matrix))

key_matrix = key_expansion(key_matrix)
print_matrix(key_matrix)
for i in range(1,11):
    print("Round", i)

    m1 = sub_bytes(m1)
    print("Sub Bytes")
    print_matrix(m1)

    print("Shift Rows")
    m1 = shift_rows(m1)
    print_matrix(m1)

    if i != 10:
        print("Mix Columns")
        m1 = mix_columns(m1)
        print_matrix(m1)
    #Calcular key matrix per aquella round
    round_key = key_matrix[i*4: (i+1)*4]
    round_key = [[round_key[j][i] for j in range(len(round_key))] for i in range(len(round_key[0]))]
    m1 = add_round_key(m1, round_key)
    print("Add Round Key")
    print_matrix(m1)

print_matrix(m1)