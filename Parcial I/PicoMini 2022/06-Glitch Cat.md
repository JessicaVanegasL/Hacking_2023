# Glitch Cat

## Objetivo

Our flag printing service has started glitching!`$ nc saturn.picoctf.net 51109`

## Hints

* 1.- ASCII is one of the most common encodings used in programming
* 2.- We know that the glitch output is valid Python, somehow!
* 3.- Press Ctrl and c on your keyboard to close your connection and return to the command prompt

## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~$ nc saturn.picoctf.net 51109
'picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}'
jessi@jessi-Aspire-E5-511:~$ python3
Python 3.8.10 (default, Nov 14 2022, 12:59:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print('picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}')
picoCTF{gl17ch_m3_n07_bda68f75}
>>> 
```

## Flag

picoCTF{gl17ch_m3_n07_bda68f75}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| python3 |  Permite entrar a la terminal de Python y poder correr el programa *.py* 
| chr |  Permite recibir un entero y como resultado da un caracter|

## Referencias

[chr ](https://parzibyte.me/blog/2018/12/10/ord-chr-python/)
