import hashlib
from typing import Optional, Tuple
import time
import matplotlib.pyplot as plt
import pandas as pd
import math

def uab_md5(message: str, num_bits: int) -> Optional[int]:
    if 1 <= num_bits <= 128:
        hash_hexa = hashlib.md5(message.encode()).hexdigest()
        hash_bin = bin(int(hash_hexa, 16))[2:].zfill(128)
        return int(hash_bin[:num_bits], 2)
    return None

# print("1r: ",uab_md5("hello", 16) ) 
# print

def second_preimage(message: str, num_bits: int) -> Optional[Tuple[str, int]]:
    primera_imatge = uab_md5(message, num_bits)
    for i in range(100000000):
        segona_imatge = uab_md5(str(i), num_bits)
        if primera_imatge == segona_imatge:
            return (str(i), i)
    return (None, None)

# print("2n: ",second_preimage("hello", 16))

# print(uab_md5("hello", 16) ) 
# print(uab_md5("hello81259", 16)) 

def collision(num_bits: int) -> Optional[Tuple[str, str, int]]:
    hashes = {}
    for i in range(100000000):
        message1 = str(i)
        hash1 = uab_md5(message1, num_bits)
        if hash1 in hashes:
            return (message1, hashes[hash1], i)
        hashes[hash1] = message1
    return (None, None, None)

# print(collision(32))

def exercici_4A():

    resultats = []

    for i in range (1, 25):
        start_time_feble = time.perf_counter()
        _, iteracions_feble =  second_preimage("hello", i)
        elapsed_time_feble = time.perf_counter() - start_time_feble

        start_time_forta = time.perf_counter()
        _, _, iteracions_forta = collision(i)
        elapsed_time_forta = time.perf_counter() - start_time_forta
    
        resultats.append((i, elapsed_time_feble, iteracions_feble, elapsed_time_forta, iteracions_forta))

    df_results = pd.DataFrame(resultats, columns=["Bits", "Temps Col·lisió Feble", "Iteracions Col·lisió Feble", "Temps Col·lisió Forta", "Iteracions Col·lisió Forta"])
    
    print(df_results)
##################################################################### 
    plt.plot(df_results["Bits"], df_results["Temps Col·lisió Feble"], label="Col·lisió Feble")
    plt.plot(df_results["Bits"], df_results["Temps Col·lisió Forta"], label="Col·lisió Forta")
    plt.xlabel("Bits")
    plt.ylabel("Temps")
    plt.title("Temps per acabar l'execució en funció del nombre de bits")
    plt.legend()
    plt.show()

    plt.plot(df_results["Bits"], df_results["Iteracions Col·lisió Feble"], label="Col·lisió Feble")
    plt.plot(df_results["Bits"], df_results["Iteracions Col·lisió Forta"], label="Col·lisió Forta")
    plt.xlabel("Bits")
    plt.ylabel("Iteracions")
    plt.title("Iteracions per obtenir la col·lisió en funció del nombre de bits") 
    plt.legend()
    plt.show()

    return df_results



def exercici4B(df_results):

    def iteracions_teoriques_fortes(bits):
        return math.ceil(2 ** (bits / 2))

    def iteracions_teoriques_febles(bits):
        return math.ceil(2 ** bits)

    for i in range(1,25):
        print("feble", i, iteracions_teoriques_febles(i))
        print("forta", i, iteracions_teoriques_fortes(i))

        #Afegueix una columna a la taula amb el nombre de iteracions teòriques que s’haurien de fer per obtenir un resultat en funció del nombre de bits.
        df_results.loc[df_results.Bits == i, "Iteracions Teòriques Feble"] = iteracions_teoriques_febles(i)
        df_results.loc[df_results.Bits == i, "Iteracions Teòriques Forta"] = iteracions_teoriques_fortes(i)

    print(df_results)
##################################################################### 
    # Gràfica de comparació del nombre de iteracions reals i teòriques per la col·lisió feble.
    plt.plot(df_results["Bits"], df_results["Iteracions Col·lisió Feble"], label="Iteracions Reals")
    plt.plot(df_results["Bits"], df_results["Iteracions Teòriques Feble"], label="Iteracions Teòriques")
    plt.xlabel("Bits")
    plt.ylabel("Iteracions")
    plt.title("Comparació de iteracions Reals amb Teòriques de les col·lision Febles")
    plt.legend()
    plt.show()

    # Gràfica de comparació del nombre de iteracions reals i teòriques per la col·lisió forta.
    plt.plot(df_results["Bits"], df_results["Iteracions Col·lisió Forta"], label="Iteracions Reals")
    plt.plot(df_results["Bits"], df_results["Iteracions Teòriques Forta"], label="Iteracions Teòriques")
    plt.xlabel("Bits")
    plt.ylabel("Iteracions")
    plt.title("Comparació de iteracions Reals amb Teòriques de les col·lision Fortes")
    plt.legend()
    plt.show()

    return df_results



df_results = exercici_4A()

exercici4B(df_results)



# Tests complementaris per conprovar que les funcions funcionen correctament
import unittest
class TestLab1(unittest.TestCase):
    def test_uab_md5(self):
        test_vectors_ok = (
            ["hola", 100, 381757249806289069081790873225],
            ["hola", 1, 0],
            ["dfk3874", 68, 229291433845740375560],
            ["dfk3874", 64, 14330714615358773472],
            ["Alexandria", 128, 221630910082124901698625759824682079437],
            ["Alexandria", 129, None],
            ["Alexandria", 0, None]
            )
        for t in test_vectors_ok:
            my_value = uab_md5(t[0], t[1])
            self.assertEqual(my_value, t[2])

    def test_second_preimage(self):
        msg = "find a second preimage"
        for n in range(1, 15):
            new_msg, _ = second_preimage(msg, n)
            self.assertEqual(uab_md5(new_msg, n), uab_md5(msg, n))
            self.assertNotEqual(new_msg, msg)

    def test_collision(self):
        for n in range(1, 15):
            msg1, msg2, _ = collision(n)
            self.assertEqual(uab_md5(msg1, n), uab_md5(msg2, n))
            self.assertNotEqual(msg1, msg2)

# unittest.main(argv=[''], verbosity=2, exit=False, buffer=True)