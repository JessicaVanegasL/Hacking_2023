# PW Crack 3

## Objetivo

Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/23/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/23/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/23/level3.hash.bin) in the same directory too.There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

## Hints

* 1.-  To view the level3.hash.bin file in the webshell, do: `$ bvi level3.hash.bin`
* 2.- To exit `bvi` type `:q` and press enter.
* 3.- The `str_xor` function does not need to be reverse engineered for this challenge.


## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ ls
Addadshashanammu.zip  fixme1.py            level2.flag.txt.enc  level3.py
codebook.txt          fixme2.py            level2.py            runme.py
code.py               level1.flag.txt.enc  level3.flag.txt.enc
convertme.py          level1.py            level3.hash.bin
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ python3 level3.py
Please enter correct password for flag: 6997
That password is incorrect
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ python3 level3.py
Please enter correct password for flag: 3ac8
That password is incorrect
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ python3 level3.py
Please enter correct password for flag: f0ac
That password is incorrect
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ python3 level3.py
Please enter correct password for flag: 4b17
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_2b072a90}
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ 

```

## Flag

picoCTF{m45h_fl1ng1ng_2b072a90}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| python3 |  Permite entrar a la terminal de Python y poder correr el programa *.py* |
El hash contiene todas las posibles contraseñas, se va probando de una por una hasta encontrar la correcta, es este caso fue **4b17**.

## Referencias

 [here](https://artifacts.picoctf.net/c/23/level3.py)
 [flag](https://artifacts.picoctf.net/c/23/level3.flag.txt.enc)
 [hash](https://artifacts.picoctf.net/c/23/level3.hash.bin)