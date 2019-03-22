import gmpy2
import math
import string
import binascii
p = gmpy2.mpz(275127860351348928173285174381581152299)
c = gmpy2.mpz(26174096085413982127350513827814096003393781011967421505411183900736523574240)
q = gmpy2.mpz(319576316814478949870590164193048041239)
mp = gmpy2.powmod(c,(p+1)/4,p)
mq = gmpy2.powmod(c,(q+1)/4,q)
yp = gmpy2.invert(p,q)
yq = gmpy2.invert(q,p)
r = gmpy2.t_mod((yp*p*mq + yq*q*mp),p*q)
s = gmpy2.t_mod((yp*p*mq - yq*q*mp),p*q)
_r = p*q - r
_s = p*q - s
print hex(r)
print hex(s)
print hex(_r)
print hex(_s)
flag = binascii.unhexlify(hex(int(_s))[27:-1])
print(flag)
