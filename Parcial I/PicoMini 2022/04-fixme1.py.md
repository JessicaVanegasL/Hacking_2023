# fixme1.py

## Objetivo

Fix the syntax error in this Python script to print the flag.[Download Python script](https://artifacts.picoctf.net/c/39/fixme1.py)

## Hints

* 1.- Indentation is very meaningful in Python
* 2.- To view the file in the webshell, do: `$ nano fixme1.py`
* 3.- To exit `nano`, press Ctrl and x and follow the on-screen prompts.
* 4.- The `str_xor` function does not need to be reverse engineered for this challenge.

## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ ls
Addadshashanammu.zip  codebook.txt  code.py  convertme.py  fixme1.py  runme.py
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ python3 fixme1.py
  File "fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
    ^
IndentationError: unexpected indent
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ nano fixme1.py
GNU nano 5.4                                               fixme1.py *                                                I      
import random
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5a) + chr(0x0>
  
flag = str_xor(flag_enc, 'enkidu')
print('That is correct! Here\'s your flag: ' + flag)
                                    [ line 20/22 (90%), col 1/53 (1%), char 781/835 (93%) ]
^H Help        ^O Read File   ^R Replace     ^V Paste       ^G Go To Line  ^Y Redo        M-6 Copy       ^Q Where Was
^X Exit        ^F Where Is    ^K Cut         ^T Execute     ^Z Undo        M-A Set Mark   M-] To Bracket M-Q Previous

jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ python3 fixme1.py
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_182342f7}
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ 

```

## Flag

picoCTF{1nd3nt1ty_cr1515_182342f7}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| python3 |  Permite entrar a la terminal de Python y poder correr el programa *.py* |
Se corrigió la linea 20 del programa,.

## Referencias

[Download Python script](https://artifacts.picoctf.net/c/39/fixme1.py)

