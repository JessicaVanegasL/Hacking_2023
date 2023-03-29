# Based

## Objetivo

To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 15130`.

## Hints

* 1.- I hear python can convert things.
* 2.- It might help to have multiple windows open.

## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~$ nc jupiter.challenges.picoctf.org 15130
Let us see how data is stored
test
Please give the 01110100 01100101 01110011 01110100 as a word.
...
you have 45 seconds.....

Input:
test
Please give me the  154 141 155 160 as a word.
Input:
lamp
Please give me the 737472656574 as a word.
Input:
street
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_02167de8}
```
## Flag

picoCTF{learning_about_converting_values_02167de8}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| nc (netcat) |  Comando que permite acceder a puertos TCP o UDP de la propia máquina o de otras máquinas remotas. También permite quedar a la escucha en un puerto dado (TCP o UDP) de la máquina local.   |

## Referencias
[Conversor de hexa a ascii](https://www.binaryhexconverter.com/hex-to-ascii-text-converter)
[Conversor de octal a ascii](https://onlineasciitools.com/convert-octal-to-ascii)
[Conversor de binario a ascii](https://www.convertstore.com/number/binarytoascii/es/binary-to-ascii-text-converter.htm)