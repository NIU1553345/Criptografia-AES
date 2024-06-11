certificatprofe = "carlos.borrego@uab.cat%profesor%ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDBh03TNOYQzyE6FgGn6gIdh1WBUsXax2kz57KvM7joCOASQJd8fo3Uc848i6ulQ8buvCbeEIzJtxo0WJNOPdQpMNQ9KzRwA0Q3wYdqlw35EZaXQ3oLBWA6iY40t56JZBiKMN7/v+BSLqs886a/tGZzHfzKtdaFpn8+PtZLrHnIWQ==%"
clau_pubCA = "%CA-UAB%ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAlw0VcSQVWZhgYMvGqLjueutYCIX2YxWrtH1YO3JdDVEObclxIbKfX1YfXJ6N4QVYMUAxb+/0TXTrDSF13YE2kA2SqJ6si1LrrCPm4dbYgsrOLCvKfuYwtiICsFdjwpgixQ/kJQMAInNil/psK7MxvSS7Dfv8T88+49yYujMIrj6VN9O5Huc5baCPZRC8x6q/OGc55RlO/80="
data_expedicio = "%11/06/2027"
certificatdavid2= "David.MartiF@autonoma.cat%alumne%ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDCDqUezfYL9n7zPg6j98nozhW7HilmrEWJxPQz4nU8jllL2m1k4RsGOJMBEErBXzm+KvgbFUVg5Zn0esOxBO9aUMngOzuanQYaHNcjTLXJE14mlcYcnSUwOP9j801Nr4aZ6dTmq2qs2XntYicumYHdrYyOHgKdz7ZPcgJEBQrgjw==%CA-UAB%ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAlw0VcSQVWZhgYMvGqLjueutYCIX2YxWrtH1YO3JdDVEObclxIbKfX1YfXJ6N4QVYMUAxb+/0TXTrDSF13YE2kA2SqJ6si1LrrCPm4dbYgsrOLCvKfuYwtiICsFdjwpgixQ/kJQMAInNil/psK7MxvSS7Dfv8T88+49yYujMIrj6VN9O5Huc5baCPZRC8x6q/OGc55RlO/80=%11/06/2027%BOTugSdynlqPa982o8zQASpuPbCUUC1ElYa3ORnK5bsvWweLA3XAvAs6NNpijfnK86Ojb+316jtdi0nHEzCOlS65YTnz6xa+tJMIhlgaXZXR/ICNx9+muX1K28C6VLnhpLivTdDALWI4IjHBU7yCbkANuxKkQef6UEqbgtOutdaByXlisX2E+eVTfzQj1GR57vlmHj085w=="

from base64 import b64encode, b64decode
from sign_message import PrunedSHA256Hash, PRUNED_HASH_SIZE, RSA_KEY_SIZE


# Hash the message to sign
 
h = PrunedSHA256Hash().new(str(certificatprofe+clau_pubCA+data_expedicio).encode('utf-8'))
print(h.hexdigest())

# Try to get a certificate with my name with the same hash

for i in range(100000000):
    prehash = 'David.MartiF@autonoma.cat%'
    posthash = '%ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDCDqUezfYL9n7zPg6j98nozhW7HilmrEWJxPQz4nU8jllL2m1k4RsGOJMBEErBXzm+KvgbFUVg5Zn0esOxBO9aUMngOzuanQYaHNcjTLXJE14mlcYcnSUwOP9j801Nr4aZ6dTmq2qs2XntYicumYHdrYyOHgKdz7ZPcgJEBQrgjw==%CA-UAB%ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAlw0VcSQVWZhgYMvGqLjueutYCIX2YxWrtH1YO3JdDVEObclxIbKfX1YfXJ6N4QVYMUAxb+/0TXTrDSF13YE2kA2SqJ6si1LrrCPm4dbYgsrOLCvKfuYwtiICsFdjwpgixQ/kJQMAInNil/psK7MxvSS7Dfv8T88+49yYujMIrj6VN9O5Huc5baCPZRC8x6q/OGc55RlO/80=%11/06/2027'
    hash = PrunedSHA256Hash().new((prehash + str(i) + posthash).encode('utf-8'))
    if hash.hexdigest() == h.hexdigest():
        print("i: ", i)
        print("hash:", hash.hexdigest())
        print("certificat:", prehash + str(i) + posthash)
        break
