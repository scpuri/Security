# -*- coding: utf-8 -*-
# strip() remove any leading or trailing whitespace characters
import sys
import math

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = rational_to_contfrac(e, n)
    convergents = convergents_from_contfrac(frac)

    for (k,d) in convergents:
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k

            s = n - phi + 1
            for i in range(1,500):
                for j in range(1,500):
                        if i*j == n:
                                if (i - j) or (j - i) == 618:
                                        print i
                                        print j
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n

            if(discr>=0):
                t = is_perfect_square(discr)

                if t!=-1 and (s+t)%2==0:
                    return d

def rational_to_contfrac (x, y):
    ''' 
    Converts a rational x/y fraction into
    a list of partial quotients [a0, ..., an] 
    '''
    a = x//y
    if a * y == x:
        return [a]
    else:
        pquotients = rational_to_contfrac(y, x - a * y)
        pquotients.insert(0, a)
        return pquotients

def convergents_from_contfrac(frac):    
    '''
    computes the list of convergents
    using the list of partial quotients 
    '''
    convs = [];
    for i in range(len(frac)):
        convs.append(contfrac_to_rational(frac[0:i]))
    return convs

def contfrac_to_rational (frac):
    '''Converts a finite continued fraction [a0, ..., an]
     to an x/y rational.
     '''
    if len(frac) == 0:
        return (0,1)
    elif len(frac) == 1:
        return (frac[0], 1)
    else:
        remainder = frac[1:len(frac)]
        (num, denom) = contfrac_to_rational(remainder)
        # fraction is now frac[0] + 1/(num/denom), which is 
        # frac[0] + denom/num.
        return (frac[0] * num + denom, num)


def is_perfect_square(n):
    '''
    If n is a perfect square it returns sqrt(n),
    
    otherwise returns -1
    '''
    h = n & 0xF; #last hexadecimal "digit"
    
    if h > 9:
        return -1 # return immediately in 6 cases out of 16.

    # Take advantage of Boolean short-circuit evaluation
    if ( h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8 ):
        # take square root if you must
        t = isqrt(n)
        if t*t == n:
            return t
        else:
            return -1
    
    return -1

def isqrt(n):
    '''
    Calculates the integer square root
    for arbitrary large nonnegative integers
    '''
    if n < 0:
        raise ValueError('square root not defined for negative numbers')
    
    if n == 0:
        return 0
    a, b = divmod(bitlength(n), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def bitlength(x):
    '''
    Calculates the bitlength of x
    '''
    assert x >= 0
    n = 0
    while x > 0:
        n = n+1
        x = x>>1
    return n


cipherinput = sys.argv[1]
keyinput = sys.argv[2]
modulofile = sys.argv[3]
outfile = sys.argv[4]

with open(keyinput) as f:
	key = f.read().strip()
with open(cipherinput) as f:
	ciphertext = f.read().strip()
with open(modulofile) as f:
	modulo = f.read().strip()

modulo = int(modulo,16)
ciphertext = int(ciphertext,16)
key = int(key,16)

e=key
n=modulo
d = hack_RSA(e,n)
c = ciphertext
plaintext = pow(c,d,n)
plaintext = hex(plaintext).rstrip("L").lstrip("0x") or "0"

f = open(outfile, 'w')
f.write(plaintext)
f.close()
