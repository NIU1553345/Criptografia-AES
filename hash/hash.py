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
    for i in range(1000000):
        segona_imatge = uab_md5(str(i), num_bits)
        if primera_imatge == segona_imatge:
            return (str(i), i)
    return (None, None)

# print("2n: ",second_preimage("hello", 16))

# print(uab_md5("hello", 16) ) 
# print(uab_md5("hello81259", 16)) 

def collision(num_bits: int) -> Optional[Tuple[str, str, int]]:
    hashes = {}
    for i in range(1000000):
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

        print(i, "bits:")
        start_time_feble = time.perf_counter()

        print("second preimage: ", second_preimage("hello", i))
        _, iteracions_feble =  second_preimage("hello", i)

        elapsed_time_feble = time.perf_counter() - start_time_feble
        print("Elapsed time second preimage: ", elapsed_time_feble)

        start_time_forta = time.perf_counter()

        print("collision: ", collision(i))
        _, _, iteracions_forta = collision(i)

        elapsed_time_forta = time.perf_counter() - start_time_forta
        print("Elapsed time collision: ", elapsed_time_forta)
    
        resultats.append((i, elapsed_time_feble, iteracions_feble, elapsed_time_forta, iteracions_forta))

    df_results = pd.DataFrame(resultats, columns=["Bits", "Temps Col·lisió Feble", "Iteracions Col·lisió Feble", "Temps Col·lisió Forta", "Iteracions Col·lisió Forta"])
    
    print(df_results)

    # Gràfica de temps: mostra el temps que es triga per obtenir un resultat en funci´o del nombre de bits en cada cas.
    plt.plot(df_results["Bits"], df_results["Temps Col·lisió Feble"], label="Col·lisió Feble")
    plt.plot(df_results["Bits"], df_results["Temps Col·lisió Forta"], label="Col·lisió Forta")
    plt.xlabel("Bits")
    plt.ylabel("Temps")
    plt.legend()
    plt.show()

    #  Gràfica de iteracions: mostra el nombre de iteracions o valors que s’han hagut de generar en funci´o del nombre de bits per cada cas.
    plt.plot(df_results["Bits"], df_results["Iteracions Col·lisió Feble"], label="Col·lisió Feble")
    plt.plot(df_results["Bits"], df_results["Iteracions Col·lisió Forta"], label="Col·lisió Forta")
    plt.xlabel("Bits")
    plt.ylabel("Iteracions")
    plt.legend()
    plt.show()

    return df_results



def exercici4B(df_results):

    def iteracions_teoriques_fortes(bits):
        return int(math.ceil(2 ** (bits / 2)))

    def iteracions_teoriques_febles(bits):
        return math.ceil(2 ** bits)

    for i in range(1,25):
        print("feble", i, iteracions_teoriques_febles(i))
        print("forta", i, iteracions_teoriques_fortes(i))

        #Afegueix una columna a la taula amb el nombre de iteracions teòriques que s’haurien de fer per obtenir un resultat en funció del nombre de bits.
        df_results.loc[df_results.Bits == i, "Iteracions Teòriques Feble"] = iteracions_teoriques_febles(i)
        df_results.loc[df_results.Bits == i, "Iteracions Teòriques Forta"] = iteracions_teoriques_fortes(i)

    print(df_results)

    # Gràfica de comparació del nombre de iteracions reals i teòriques per la col·lisió feble.
    plt.plot(df_results["Bits"], df_results["Iteracions Col·lisió Feble"], label="Iteracions Reals")
    plt.plot(df_results["Bits"], df_results["Iteracions Teòriques Feble"], label="Iteracions Teòriques")
    plt.plot(df_results["Bits"], df_results["Iteracions Col·lisió Forta"], label="Iteracions Reals")
    plt.plot(df_results["Bits"], df_results["Iteracions Teòriques Forta"], label="Iteracions Teòriques")
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


# exercici_4A()

df_results = exercici_4A()

exercici4B(df_results)