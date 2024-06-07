import hashlib
from typing import Optional, Tuple

def uab_md5(message: str, num_bits: int) -> Optional[int]:
    if 1 <= num_bits <= 128:
        hash_hexa = hashlib.md5(message.encode()).hexdigest()
        hash_bin = bin(int(hash_hexa, 16))[2:].zfill(128)
        return int(hash_bin[:num_bits], 2)
    return None

print("1r: ",uab_md5("hello", 16) ) 
print
def second_preimage(message: str, num_bits: int) -> Optional[Tuple[str, int]]:
    primera_imatge = uab_md5(message, num_bits)
    for i in range(1000000):
        segona_imatge = uab_md5(str(i), num_bits)
        if primera_imatge == segona_imatge:
            return (str(i), i)
    return None

print("2n: ",second_preimage("hello", 16))

print(uab_md5("hello", 16) ) 
print(uab_md5("hello81259", 16)) 

def collision(num_bits: int) -> Optional[Tuple[str, str, int]]:
    hashes = {}
    for i in range(1000000):
        message1 = str(i)
        hash1 = uab_md5(message1, num_bits)
        if hash1 in hashes:
            return (message1, hashes[hash1], i)
        hashes[hash1] = message1
    return None

print(collision(32))

for i in range (8, 96, 8):
    print(i, "bits:")
    print("second preimage: ", second_preimage("hello", i))
    print("collision: ", collision(i))
    