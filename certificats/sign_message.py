from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode

PRUNED_HASH_SIZE = 2  # bytes
RSA_KEY_SIZE = 1024


class PrunedSHA256Hash(SHA256.SHA256Hash):

    def new(self, data=None):
        return PrunedSHA256Hash(data)

    def digest(self):
        full_hash = super().digest()
        pruned_hash = full_hash[:PRUNED_HASH_SIZE] + b'\x00' * (len(full_hash) - PRUNED_HASH_SIZE)
        return pruned_hash


if __name__ == '__main__':

    # Generate a RSA key
    student_key = RSA.generate(RSA_KEY_SIZE)
    # print(student_key.export_key().decode('utf-8'))

    # Export the public key
    # student_pub_key = student_key.publickey()
    # print(student_pub_key.export_key().decode('utf-8'))

    # Hash the message to sign
    str_to_sign = "s"   
    h = PrunedSHA256Hash().new(str_to_sign.encode('utf-8'))

    # Sign the hash of the message and get b64 encoded signature
    signer = PKCS1_v1_5.new(student_key)
    signature = b64encode(signer.sign(h)).decode('utf-8')

    # Print results
    print(f"\tString to sign:\t\t\t\t\t\t{str_to_sign}")
    print(f"\tHash of the string (SHA256 pruned):\t{h.hexdigest()}")
    print(f"\tSignature:\t\t\t\t\t\t\t{signature}")

    print(f"Public key: {student_key.publickey().export_key(format = 'OpenSSH').decode('utf-8')}")
    print(f"Private key: {student_key.export_key().decode('utf-8')}")