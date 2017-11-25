import gmpy

def int2string(i):
    ihex = hex(i)[2:-1]
    if len(ihex) % 2 != 0:
            ihex = '0' + ihex
    return ihex.decode('hex')

nthroot = lambda a, r: int(gmpy.root(a, r)[0])
modinv = lambda a, m: int(gmpy.invert(a, m))
egcd = lambda x, y: map(int, gmpy.gcdext(x, y))
