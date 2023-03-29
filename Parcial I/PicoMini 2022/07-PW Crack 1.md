# PW Crack 1

## Objetivo

Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/52/level1.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/52/level1.flag.txt.enc) in the same directory too.

## Hints

* 1.- To view the file in the webshell, do: `$ nano level1.py`
* 2.- To exit `nano`, press Ctrl and x and follow the on-screen prompts.
* 3.- The `str_xor` function does not need to be reverse engineered for this challenge.

## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ ls
Addadshashanammu.zip  code.py       fixme1.py  level1.flag.txt.enc  runme.py
codebook.txt          convertme.py  fixme2.py  level1.py
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ python3 level1.py
Please enter correct password for flag: 1e1a
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_fa343060}
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ 
```

## Flag

picoCTF{545h_r1ng1ng_fa343060}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| python3 |  Permite entrar a la terminal de Python y poder correr el programa *.py* |
El password se encontraba en el codigo fuente.

## Referencias

 [here](https://artifacts.picoctf.net/c/52/level1.py)
 [flag](https://artifacts.picoctf.net/c/52/level1.flag.txt.enc)