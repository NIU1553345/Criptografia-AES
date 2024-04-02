'''
En aquest codi es pot trobar l'algoritme AES implementat en Python. 
El codi es trobar dividit en 4 parts:
    1. Funcions auxiliars
    2. Matrius de l'algoritme
    3. Funcions de l'algoritme
    4. Main

'''



##########################################################################################
'''
Funcions auxiliar
'''
##########################################################################################



def num_to_bin(num):
    '''
    Transforma un número (ja sigui decimal o hexadecimal) a binari.

    Args:
        hexnum (int / str): Número (decimal o hexadecimal)
    Returns:
        str: Número binari
    '''
    #En el cas de que el número sigui hexadecimal cal transformar-lo a enter
    if type(num) == str:
        num = int(num, 16)

    #Transforma el número a binari, agafa apartir de la 3a posició del str perquè al ser binari surt 0b
    # i en el cas de que no tingui 8 bits, s'omplen amb 0's
    return bin((num))[2:].zfill(8)


def bin_to_hex(binnum):
    '''
    Transforma un número binari a hexadecimal.

    Args:
        binnum (str): Número binari
    Returns:
        str: Número hexadecimal
    '''
    return hex(int(binnum, 2))[2:].zfill(2)


def dec_to_hex(decnum):
    '''
    Transforma un número decimal a hexadecimal.

    Args:
        decnum (int): Número decimal
    Returns:
        str: Número hexadecimal
    '''
    return hex(decnum)[2:].zfill(2)


def xor(hexnum1, hexnum2):
    '''
    Fa la operació XOR entre dos números hexadecimals.

    Args:
        hexnum1 (str): Número hexadecimal
        hexnum2 (str): Número hexadecimal
    Returns:
        str: Resultat de la operació XOR en hexadecimal
    ''' 
    #Transforma els dos números a binari perquè sigui més fàcil fer l'operació
    bin1, bin2 = num_to_bin(hexnum1), num_to_bin(hexnum2)
    
    #Guarda el str resultant en la variable res
    res = ''

    #Recorre els dos números binaris posició a posició i fa la operació XOR en cada bit
    for i in range(8):
        if bin1[i] == bin2[i]:
            res += '0'
        else:
            res += '1'
    return bin_to_hex(res)


def xor_bin(bin1, bin2):
    '''
    Fa la operació XOR entre dos números binaris.

    Args:
        bin1 (str): Número binari
        bin2 (str): Número binari
    Returns:
        str: Resultat de la operació XOR en hexadecimal
    '''
    #Guarda el str resultant en la variable res
    res = ''
    #Recorre els dos números binaris posició a posició i fa la operació XOR en cada bit
    for i in range(len(bin1)):
        if bin1[i] == bin2[i]:
            res += '0'
        else:
            res += '1'
    return bin_to_hex(res)


def print_matrix(matrix):
    '''
    Imprimeix la matriu per pantalla perquè quedi amb forma matricial.
    
    Args:
        matrix (list): Matriu de dimensions qualsevol
    '''
    #Imprimeix cada fila de la matriu
    for i in range(len(matrix)):
        print(matrix[i])
    print()


def mul2(hexnum):
    '''
    Multiplica per 2 un número hexadecimal. Aquesta operació es correspon a desplaçar tot el nombre binari 1 cap a l'esquerra.

    Args:
        hexnum (str): Número hexadecimal
    Returns:
        str: Resultat de la multiplicació per 2 en hexadecimal
    '''
    #Cal tenir el nombre en binari
    binnum = num_to_bin(hexnum)

    #Afeguim un 0 al final que és el mateix que desplaçar tots els valors 1 cap a l'esquerra
    res = binnum + '0'

    #En cas de que estigui dins del mòdul es pasa a hexadecimal i es retorna
    if binnum[0] == '0':
        res = res[1:]
        res = bin_to_hex(res)

    #En cas contrari, que tingui un 1, s'ha de aplicar el mòdul
    else:
        #Fa el mòdul de x^8 + x^4 + x^3 + x + 1 fent un xor amb amb aquest valor
        res = xor_bin(res, "100011011")

    return (res)


def mul3(hexnum):
    '''
    Multiplica per 3 un número hexadecimal. Aquesta operació es correspon a desplaçar 
    tot el nombre binari 1 cap a l'esquerra i fer la suma (xor) amb el hexadecimal incial.

    Args:
        hexnum (str): Número hexadecimal
    Returns:
        str: Resultat de la multiplicació per 3 en hexadecimal
    '''
    #Multipliquem per dos i sumem l'hexadecimal inicial
    return xor(hexnum, (mul2(hexnum)))



##########################################################################################
'''
Matrius de l'algoritme
'''
##########################################################################################



#Sbox que encara que es pugui veure com hexadecimal, es tracta de una llista de 256 enters 
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


#Cada valor és un tipus de multiplicació per tant ens convé tenir-ho en enter
mix_matrix = [[2,3,1,1], [1,2,3,1], [1,1,2,3], [3,1,1,2]]


#Rcon és una llista de enters que s'utilitza per la key expansion però en aquest cas si que cal tenir-la en hexadecimal
Rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
#Cada de Rcon element el transformem a hexadecimal
for i in range(len(Rcon)):
    Rcon[i] = dec_to_hex(Rcon[i])



##########################################################################################
'''
Funcions de l'algoritme
'''
##########################################################################################



def add_round_key(matrix, key):
    '''
    Fa l'operació xor per cada element de la matriu amb la clau

    Args:
        matrix (list): Matriu 4x4 d'elements hexadecimals
        key (list): Matriu 4x4 d'elements hexadecimals
    Returns:
        matrix (list): Matriu 4x4 d'elements hexadecimals resultants de l'operació
    '''
    #Recorre tots els elements de cada matriu i fa l'operació xor amb el seu corresponent en l'altre
    for i in range(4):
        for j in range(4):
            matrix[i][j] = xor(matrix[i][j], key[i][j])
    return matrix


def key_expansion(key):
    '''
    Fa l'expansió de la clau per poder fer les rondes de l'algoritme amb la clau corresponent.

    Args:
        key (list): Matriu 4x4 d'elements hexadecimals
    Returns:
        key (list): Matriu 44x4 d'elements hexadecimals
    '''
    #Transposa la matriu per poder fer les operacions més fàcilment amb les columnes com a files
    key = [[key[j][i] for j in range(len(key))] for i in range(len(key[0]))]
    
    #Bucle de 4 a 44 perquè ja tenim les 4 primeres columnes de la clau i volem les 40 següents on cada 4 iteracions serà una no va ronda (4 elements * 10 rondes)
    for i in range(4, 44):

        #En el cas de que sigui la primera columna de la ronda (RotWord)
        if i % 4 == 0:

            #Ell primer elemnt pasa a ser l'últim
            temp = key[i-1].copy()
            temp.append(temp.pop(0))

            #Aquest array s'ha de substituir per la Sbox
            for j in range(4):
                temp[j] = hex(Sbox[int(temp[j], 16)])[2:].zfill(2)
            
            #Aquest array (només el primer element) s'ha de fer un xor amb el Rcon corresponent a la ronda
            temp[0] = xor(temp[0], Rcon[int(i/4) - 1])
            key.append([])

            #La columna resultant s'afegueix a la matriu de la clau
            for j in range(4):
                key[i].append(xor(key[i-4][j], temp[j]))
        
        #En el cas de no sigui la primera columna de la ronda
        else:

            #Es fa un xor amb la columna que li correspondria en la ronda anterior
            key.append([])
            for j in range(4):
                #Es busca el calor que li pertoca en la clau de la ronda anterior
                key[i].append(xor(key[i-4][j], key[i-1][j]))      
    return key   


def sub_bytes(matrix):
    '''
    Substitueix cada valor de la matriu per el valor que li correspongui en la Sbox.

    Args:
        matrix (list): Matriu 4x4 amb elements en hexadecimals
    Returns:
        matrix: Matriu 4x4 amb els valors substituits amb elements en hexadecimals
    '''
    #Dos bucles de 4 per recorrer tota la matriu
    for i in range(4):
        for j in range(4):
            #Busca en la Sbox el valor que li correspon per l'ement de la posició de la matriu i el substitueix
            matrix[i][j] = hex(Sbox[int(matrix[i][j], 16)])[2:].zfill(2)
    return matrix


def shift_rows(matrix):
    '''
    Desplaça les posicions de les files de la matriu segons la ronda que sigui (1a fila 0, 2a fila 1, 3a fila 2, 4a fila 3).
    
    Args:
        matrix (list): Matriu 4x4 amb elements en hexadecimals
    Returns:
        matrix: Matriu 4x4 amb les files desplaçades amb elements en hexadecimals
    '''
    #No cal recorre totes les posicions de la matriu
    for i in range(4):
        #Depenent de la fila que li toqui despaça "i" cops la fila
        for j in range(i):
            matrix[i].append(matrix[i].pop(0))
    return matrix


def matxcolumna(column):
    '''
    Funció auxiliar de la funció mix_matrix per fer les operacions que li pertoquen a la columna. Realitza una multiplicació de matrius de 4x1 * 4x4
    
    Args:
        column (list): Llista de 4 elements hexadecimals
    Returns:
        res (list): Llista de 4 elements hexadecimals
    '''
    #Creem un vector de 4 posicions que serbirà de columan pel resultat
    res = ['', '', '', '']

    #Recorre tota la columna i fa un sumatori en la variable total per acabar amb el resultat que li pertoqui de la multiplicació del columna per la matriu
    for i in range(4):
        total = 0
        for j in range(4):
            if mix_matrix[i][j] == 1:
                total = xor(total, (column[j]))
            elif mix_matrix[i][j] == 2:
                total = xor(total, mul2(column[j]))
            elif mix_matrix[i][j] == 3:
                total = xor(total, mul3(column[j]))            
        
        #Al final de cada valor de la columna es guarda en l'array final
        res[i] = total
    return res


def mix_columns(matrix):
    '''
    Multiplica cada columna de la matriu per la matriu mix_matrix (es troba en l'apartat de matrius).

    Args:
        matrix (list): Matriu 4x4 amb elements en hexadecimals
    Returns:
        res (list): Matriu 4x4 amb elements en hexadecimals
    '''
    res = []
    column = []
    #Recorre tota la matriu, per guardar columna per columna, i multiplicar-la per matriu mix_matrix
    for i in range(4):
        column = []
        for j in range(4):
            column.append(matrix[j][i])
        
        #Guarda la columna resultant de la operació en la matriu "res"
        res.append(matxcolumna(column))
    
    #Transposa la matriu resultant perquè la hem transposat anteriorment al guardar columna a columna
    res = [[res[j][i] for j in range(len(res))] for i in range(len(res[0]))]
    return res
        


##########################################################################################
'''
Main
'''
##########################################################################################


#Inicialitzem tant la matriu que volem codificar com la clau en hexadecimals però que python enten com a enters
input_matrix = [[0x32, 0x88, 0x31, 0xe0], [0x43, 0x5a, 0x31, 0x37], [0xf6, 0x30, 0x98, 0x07], [0xa8, 0x8d, 0xa2, 0x34]]
key_matrix = [[0x2b, 0x28, 0xab, 0x09], [0x7e, 0xae, 0xf7, 0xcf], [0x15, 0xd2, 0x15, 0x4f], [0x16, 0xa6, 0x88, 0x3c]]

#Com volem aquestes matrius amb els valors en hexadecimals transformem element a element a hexadecimal
for i in range(4):
    for j in range(4):
        input_matrix[i][j] = dec_to_hex(input_matrix[i][j])
        key_matrix[i][j] = dec_to_hex(key_matrix[i][j])

#Per veure la matriu de partida per pantalla
print("Initial Matrix")
print_matrix(input_matrix)

#Comença la ronda 0 amb la primera operació que és "add_round_key" amb la clau inicial
print("Round 0:")
matrix = add_round_key(input_matrix, key_matrix)
print("Add Round Key")
print_matrix(matrix)

#Calcula l'exansió de la clau i la guarda en la variable per poder-la utilitzar en futures iteracions
key_matrix = key_expansion(key_matrix)
print("Extended key")
print_matrix(key_matrix)

#Comença un bucle del 10 iteracions on es farà tota l'encriptació per acabar amb la matriu encriptada final
for i in range(1,11):
    print("Round", i)

    #Sempre comença fent el "sub bytes"
    matrix = sub_bytes(matrix)
    print("Sub Bytes")
    print_matrix(matrix)

    #Seguidament sempre fa "shift rows"
    print("Shift Rows")
    matrix = shift_rows(matrix)
    print_matrix(matrix)

    #Nomès en el cas de que no estigui en la decena ronda es fa "mix columns"
    if i != 10:
        print("Mix Columns")
        matrix = mix_columns(matrix)
        print_matrix(matrix)

    #Agafar només la part de la clau que pertoca per aquella round
    round_key = key_matrix[i*4: (i+1)*4]

    #La transposa
    round_key = [[round_key[j][i] for j in range(len(round_key))] for i in range(len(round_key[0]))]
    
    #Aplica el "round_key" 
    matrix = add_round_key(matrix, round_key)
    print("Add Round Key")
    print_matrix(matrix)

#Mostra per pantalla la matriu final
print("Matriu final!")
print_matrix(matrix)

