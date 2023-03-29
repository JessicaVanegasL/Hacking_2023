# fixme2.py

## Objetivo

Fix the syntax error in the Python script to print the flag.[Download Python script](https://artifacts.picoctf.net/c/65/fixme2.py)

## Hints

* 1.- Are equality and assignment the same symbol?
* 2.- To view the file in the webshell, do: `$ nano fixme2.py`
* 3.- To exit `nano`, press Ctrl and x and follow the on-screen prompts.
* 4.- The `str_xor` function does not need to be reverse engineered for this challenge.

## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ ls
Addadshashanammu.zip  code.py       fixme1.py  runme.py
codebook.txt          convertme.py  fixme2.py
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ python3 fixme2.py
  File "fixme2.py", line 22
    if flag = "":
            ^
SyntaxError: invalid syntax
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ nano fixme2.py
 GNU nano 5.4                                               fixme2.py                                                  I      
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])


flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x58) + chr(0x1>

  
flag = str_xor(flag_enc, 'enkidu')

# Check that flag is not empty
if flag == "":
  print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)
                                  [ line 26/28 (92%), col 1/1 (100%), char 1028/1030 (99%) ]
^H Help        ^O Read File   ^R Replace     ^V Paste       ^G Go To Line  ^Y Redo        M-6 Copy       ^Q Where Was
^X Exit        ^F Where Is    ^K Cut         ^T Execute     ^Z Undo        M-A Set Mark   M-] To Bracket M-Q Previous
...

jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ python3 fixme2.py
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_e8814d03}
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ 

```

## Flag

picoCTF{3qu4l1ty_n0t_4551gnm3nt_e8814d03}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| python3 |  Permite entrar a la terminal de Python y poder correr el programa *.py* |
Se tuvo que corrigir la linea 22 del programa, porque, hubo una  una condicion que  necesita ```"==" y se tenia solo "="```

## Referencias

[Download Python script](https://artifacts.picoctf.net/c/65/fixme2.py)
