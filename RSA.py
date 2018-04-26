import math
def RSA_Gen_key(e, public, private):
    p = 823
    q = 409
    n = p * q
    phi = (p-1) * (q-1)
    #p and q are random primes
    d = 1 % phi / e
    public.append(n)
    public.append(e)
    private.append(d) 
    private.append(n)


def RSA_Encryption(public, m):
    c = (m ** public[1]) % public[0]
    return c
    #c = m^e mod n
    
def RSA_Decryption(private, c):
    m = (c ** private[0]) % public[1]
    #m = c^d mod n



public = []
private = []

    
    
    
    
