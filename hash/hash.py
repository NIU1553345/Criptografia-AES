import hashlib
from typing import Optional, Tuple
import time
import matplotlib.pyplot as plt
import pandas as pd
import math

def uab_md5(message: str, num_bits: int) -> Optional[int]:
    # Comprova que el nombre de bits estigui entre 1 i 128
    if 1 <= num_bits <= 128:
        # Calcula el hash MD5 de l'string i el converteix a binari
        hash_hexa = hashlib.md5(message.encode()).hexdigest()
        hash_bin = bin(int(hash_hexa, 16))[2:].zfill(128)
        # Retorna els primers num_bits del hash binari i el passa a enter
        return int(hash_bin[:num_bits], 2)
    return None

# print("1r: ",uab_md5("hello", 16) ) 

def second_preimage(message: str, num_bits: int) -> Optional[Tuple[str, int]]:
    # Calcula el hash MD5 de l'string i el guarda com a primera imatge de referència
    primera_imatge = uab_md5(message, num_bits)
    # Comprova si hi ha alguna segona imatge que coincideixi amb la primera en 100000000 iteracions com a màxim
    for i in range(100000000):
        # Calcula el hash MD5 de l'enter i el compara amb la primera imatge
        segona_imatge = uab_md5(str(i), num_bits)
        if primera_imatge == segona_imatge:
            # Retorna l'enter i el seu hash si coincideixen
            return (str(i), i)
    # Retorna None si no s'ha trobat cap segona imatge
    return (None, None)

# print("2n: ",second_preimage("hello", 16))


def collision(num_bits: int) -> Optional[Tuple[str, str, int]]:
    # Crea un diccionari per emmagatzemar els hashes i els missatges corresponents
    hashes = {}
    # Comprova si hi ha alguna col·lisió en 100000000 iteracions com a màxim
    for i in range(100000000):
        message1 = str(i)
        # Calcula el hash MD5 de l'enter i el guarda com a primera imatge de referència
        hash1 = uab_md5(message1, num_bits)
        # Comprova si el hash ja existeix al diccionari
        if hash1 in hashes:
            # En el cas de que existeixi, retorna el missatge i el nombre d'iteracions
            return (message1, hashes[hash1], i)
        # Si no existeix, guarda el hash i el missatge al diccionari
        hashes[hash1] = message1
    # Retorna None si no s'ha trobat cap col·lisió
    return (None, None, None)

# print(collision(32))

def exercici_4A():

    # Crea una llista per emmagatzemar els resultats
    resultats = []

    # Comprova el temps d'execució i el nombre d'iteracions per obtenir una col·lisió feble i forta en funció del nombre de bits
    for i in range (1, 25):
        # Comprova el temps d'execució i el nombre d'iteracions per obtenir una col·lisió feble
        start_time_feble = time.perf_counter()
        _, iteracions_feble =  second_preimage("hello", i)
        elapsed_time_feble = time.perf_counter() - start_time_feble

        # Comprova el temps d'execució i el nombre d'iteracions per obtenir una col·lisió forta
        start_time_forta = time.perf_counter()
        _, _, iteracions_forta = collision(i)
        elapsed_time_forta = time.perf_counter() - start_time_forta

        # Afegeix els resultats a la llista on cada fila és una tupla amb el nombre de bits, el temps d'execució i el nombre d'iteracions
        resultats.append((i, elapsed_time_feble, iteracions_feble, elapsed_time_forta, iteracions_forta))

    # Crea un DataFrame amb els resultats per mostrar-los per pantalla amb pandas
    df_results = pd.DataFrame(resultats, columns=["Bits", "Temps Col·lisió Feble", "Iteracions Col·lisió Feble", "Temps Col·lisió Forta", "Iteracions Col·lisió Forta"])
    
    # Mostra els resultats per pantalla
    print(df_results)
##################################################################### 

    # Gràfica de comparació del temps d'execució per obtenir la col·lisió feble i forta en funció del nombre de bits
    plt.plot(df_results["Bits"], df_results["Temps Col·lisió Feble"], label="Col·lisió Feble")
    plt.plot(df_results["Bits"], df_results["Temps Col·lisió Forta"], label="Col·lisió Forta")
    plt.xlabel("Bits")
    plt.ylabel("Temps")
    plt.title("Temps per acabar l'execució en funció del nombre de bits")
    plt.legend()
    plt.show()

    # Gràfica de comparació del nombre d'iteracions per obtenir la col·lisió feble i forta en funció del nombre de bits
    plt.plot(df_results["Bits"], df_results["Iteracions Col·lisió Feble"], label="Col·lisió Feble")
    plt.plot(df_results["Bits"], df_results["Iteracions Col·lisió Forta"], label="Col·lisió Forta")
    plt.xlabel("Bits")
    plt.ylabel("Iteracions")
    plt.title("Iteracions per obtenir la col·lisió en funció del nombre de bits") 
    plt.legend()
    plt.show()

    return df_results



def exercici4B(df_results):

    # Funció per calcular el nombre de iteracions teòriques que s’haurien de fer per obtenir un resultat en funció del nombre de bits per les col·lisions fortes
    def iteracions_teoriques_fortes(bits):
        return math.ceil(2 ** (bits / 2))

    # Funció per calcular el nombre de iteracions teòriques que s’haurien de fer per obtenir un resultat en funció del nombre de bits per les col·lisions febles
    def iteracions_teoriques_febles(bits):
        return math.ceil(2 ** bits)

    for i in range(1,25):
        # print("feble", i, iteracions_teoriques_febles(i))
        # print("forta", i, iteracions_teoriques_fortes(i))

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



# df_results = exercici_4A()

# exercici4B(df_results)


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