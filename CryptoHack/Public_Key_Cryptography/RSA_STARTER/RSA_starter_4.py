#The private key d is used to decrypt ciphertexts created with the corresponding public key (it's also used to "sign" a message but we'll get to that later).
#In RSA the private key is the modular multiplicative inverse of the exponent e modulo the totient of N
#d = e^-1 mod φ (n) standard typos
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
fx = (p-1)*(q-1)
print(pow(e,-1,fx))

