# SRA

## Objetivo

I just recently learnt about the SRA public key cryptosystem... or wait, was it supposed to be RSA? Hmmm, I should probably check...

Additional details will be available after launching your challenge instance.

## Hints

## Solución

```
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ nc saturn.picoctf.net 58812      
anger = 18103876486322895188405225550377652449200759227430404746549961612518829773737
envy = 27236959284551198369327564686000255534354512389887543944673260524379263783573
vainglory?
> b
b
Hubris!
                                                                                                                    
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ ls -la                     
total 12
drwxr-xr-x 2 kali kali 4096 May 13 00:47 .
drwxr-xr-x 3 kali kali 4096 Apr 30 18:17 ..
-rw-r--r-- 1 kali kali  630 May 13 00:47 chal.py
                                                                                                                    
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ python3 chal.py 
anger = 48343641038157415547760252923124429184824616455109461547972447741690103658849
envy = 49951460051839559691173970624977173470578395632052286861805921952780002003137
vainglory?
> 
Hubris!
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ nano ex.py
                                                                                                                    
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ python3 ex.py
[+] Opening connection to saturn.picoctf.net on port 55608: Done
36008319414392335094301564957159711451846999219482811868324217893094823570298
39166994714476986293862372412025376043577291645936406129327105987230998451185
Done
EmEoMuY2pcIhkgJG
b'EmEoMuY2pcIhkgJG\r\n'
b'Conquered!\r\n'
b'picoCTF{7h053_51n5_4r3_n0_m0r3_dd808298}\r\n'
[*] Closed connection to saturn.picoctf.net port 55608

```

```
from sage.all import *

from pwn import *

from gmpy2 import is_prime

from string import ascii_letters, digits

from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse

  

r = remote('saturn.picoctf.net',55608)

  

def is_printable(text):

    alphabet = ascii_letters + digits

    for i in text:

        if i not in alphabet:

            return False

    return True

  

e = 65537

r.recvuntil(b'anger = ')

c = int(r.recvline().strip().decode())

r.recvuntil(b'envy = ')

d = int(r.recvline().strip().decode())

r.recvline()

print(c)

print(d)

  

K = divisors(d*e - 1)

print("Done")

  

list_prime = []

for k in K:

    pp = ((d*e - 1)//k) + 1

  

    if is_prime(pp) and int(pp).bit_length() == 128:

        list_prime.append(pp)

  

list_text = []

for p in list_prime:

    for q in list_prime:

        try:

            if inverse(e, (p - 1) * (q - 1)) == d:

                n = p*q

                list_text.append(long_to_bytes(int(pow(c, d, n))))

        except:

            pass

  
  

list_text = set(list_text)

  

for text in list_text:

    try:

        text = text.decode()

        if is_printable(text):

            print(text)

            r.recvuntil(b'> ')

            r.sendline(text.encode())

            print(r.recvline())

            print(r.recvline())

            print(r.recvline())

            break

    except:

        continue

r.close()
```



## Flag

picoCTF{7h053_51n5_4r3_n0_m0r3_dd808298}

## Notas adicionales

RSA es un algoritmo de cifrado/descifrado asimétrico relativamente simple (la clave de cifrado y la clave de descifrado son diferentes).
Implemente el algoritmo descrito anteriormente para encriptar una secuencia generada aleatoriamente de 16 letras y dígitos ascii. Luego imprime `d`( `anger`) y `ciphertext`( `envy`) y nos hace ingresar el texto sin formato. Si obtenemos el texto sin formato correcto, obtenemos la bandera.

## Referencias

[rsa](https://en.wikipedia.org/wiki/RSA_(cryptosystem))