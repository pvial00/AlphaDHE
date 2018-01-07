# AlphaDHE - DiffieHellman Ephemeral for A-Z ciphers
Note: Requires MASHHASH and pycrypto to be installed.

Uses 1024 bit primes by default.  The alpha.py script allows two parties to develop a shared secret by exchanging values.  The resulting secret key is hashed using MASH to create a key of desired size. (Default is 16 letters, maximum is 32)

# Script usage:

Initiator: python alpha.py init
Other party: python alpha.py
