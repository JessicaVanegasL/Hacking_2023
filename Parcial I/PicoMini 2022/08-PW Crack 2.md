# PW Crack 2

## Objetivo

Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/18/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/18/level2.flag.txt.enc) in the same directory too.

## Hints

* 1.-  Does that encoding look familiar?
* 2.- The `str_xor` function does not need to be reverse engineered for this challenge.

## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ python3
Python 3.8.10 (default, Nov 14 2022, 12:59:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print(chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65))
39ce
>>> 

jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ ls
Addadshashanammu.zip  convertme.py  level1.flag.txt.enc  level2.py
codebook.txt          fixme1.py     level1.py            runme.py
code.py               fixme2.py     level2.flag.txt.enc
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ python3 level2.py
Please enter correct password for flag: 39ce
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_502ec42e}
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ 

```

## Flag

picoCTF{tr45h_51ng1ng_502ec42e}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| python3 |  Permite entrar a la terminal de Python y poder correr el programa *.py* |
El password se encuentra en el codigo ascii  y así hacemos la conversion con python3.

## Referencias

[here](https://artifacts.picoctf.net/c/18/level2.py)
[flag](https://artifacts.picoctf.net/c/18/level2.flag.txt.enc)