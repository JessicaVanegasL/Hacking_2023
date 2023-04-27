# Mind your Ps and Qs

## Objetivo

In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/2604f8b51a5cc62d38a3736938f19cef/values)

## Hints

Bits are expensive, I used only a little bit over 100 to save money

## Solución

```
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto]
└─$ ls -la                     
total 12
drwxr-xr-x 2 kali kali 4096 Apr 26 23:05 .
drwxr-xr-x 3 kali kali 4096 Apr 26 23:05 ..
-rw-r--r-- 1 kali kali  206 Apr 26 23:05 values
                                                                                                                        
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto]
└─$ cat values
Decrypt my super sick RSA:
c: 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n: 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e: 65537       
```

- python
```  
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto]
└─$ python3       
Python 3.11.2 (main, Feb 12 2023, 00:48:52) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from Crypto.Util.number import long_to_bytes
>>> from Crypto.Util.number import inverse
>>> c=861270243527190895777142537838333832920579264010533029282104230006461420086153423
>>> e=65537 
>>> p=1955175890537890492055221842734816092141
>>> q=670577792467509699665091201633524389157003
>>> p
1955175890537890492055221842734816092141
>>> q
670577792467509699665091201633524389157003
>>> n=p*q
>>> n
1311097532562595991877980619849724606784164430105441327897358800116889057763413423
>>> tn = (p-1)*(q-1)
>>> tn
1311097532562595991877980619849724606783491897137083280307201653693412798558164280
>>> d= inverse(e,tn)
>>> m=pow(c,d,n)
>>> m
13016382529449106065927291425342535437996222135352905256639573959002849415739773
>>> long_to_bytes(m)
b'picoCTF{sma11_N_n0_g0od_13686679}'
>>> 
```
## Flag

picoCTF{sma11_N_n0_g0od_13686679}

## Notas adicionales

Herramienta de ataques múltiples RSA: descifrar datos de clave pública débil e intentar recuperar clave privada. La herramienta recorrerá cada ataque seleccionado para una clave pública determinada. La seguridad de RSA se basa en la complejidad del problema de factorización de enteros.

## Referencias

[factordb](http://factordb.com/)
[rsactftool](https://github.com/RsaCtfTool/RsaCtfTool)