#import libraries

import random
import math

p =int(input("Input primary #1=> "))
q =int(input("Input primary #2=> "))

r=p*q
phiN = (p - 1) * (q - 1)
coprimes = []

def k_gen(r):
    for k in range(3,r):
        if math.gcd(k,r)==1:
            coprimes.append(k)

    return coprimes
coprimes=k_gen(phiN)
ran=random.choice(coprimes)


def gen_g(ran,phiN,coprimes):
    for g in coprimes:
        if(g*ran) % phiN ==1:
            return g
    return none
f=gen_g(ran,phiN, coprimes)

print('Public key=>: '+str(ran)+','+ str(r))

print('Private key=>: '+str(f)+','+ str(r))

manual = int(input("Enter text for encryption=> "))
c =(manual**ran)%r
print('Ciphertext=> '+ str(c))

manual= print(input("Your plain text for encryption "))
manual=(c**f)%r
print('Your plain text for decryption'+ str(manual))
