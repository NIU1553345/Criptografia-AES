import hashlib
from typing import Optional, Tuple

def uab_md5_explica(message: str, num_bits: int) -> Optional[int]:
    print("message: ", message)
    message1 = message.encode()
    print("message encoded: ", message1)
    message2 = hashlib.md5(message1)
    print("message hashed: ", message2)
    message3 = message2.hexdigest()
    print("message hexdigest: ", message3)
    message4 = message3[:num_bits // 4]
    print("message truncated: ", message4)
    message5 = int(message4, 16)
    print("message int: ", message5)
    return message5

def uab_md5(message: str, num_bits: int) -> Optional[int]:
    return int(hashlib.md5(message.encode()).hexdigest()[:num_bits // 4], 16)

print(uab_md5("hello", 23) ) # 907060870

def second_preimage_md5(message: str, num_bits: int) -> Optional[str]:
    primera_imatge = uab_md5(message, num_bits)
    for i in range(1000000):
        segona_imatge = uab_md5(message + str(i), num_bits)
        if primera_imatge == segona_imatge:
            return message + str(i)
    return None

print(second_preimage_md5("hello", 16))

print(uab_md5("hello", 16) ) 
print(uab_md5("hello81259", 16)) 

def collision_md5(num_bits: int) -> Tuple[str, str]:
    hashes = {}
    for i in range(1000000):
        message1 = str(i)
        hash1 = uab_md5(message1, num_bits)
        if hash1 in hashes:
            return message1, hashes[hash1], hash1
        hashes[hash1] = message1
    return None, None, None

print(collision_md5(32))

for i in range (8, 96, 8):
    print(i, "bits:")
    print("second preimage: ", second_preimage_md5("hello", i))
    print("collision: ", collision_md5(i))
    