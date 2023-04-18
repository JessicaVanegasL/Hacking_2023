# Easy 1

## Objetivo

The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help `UFJKXQZQUNB` with the key of `SOLVECRYPTO`. Can you use this [table](https://jupiter.challenges.picoctf.org/static/1fd21547c154c678d2dab145c29f1d79/table.txt) to solve it?.

## Hints

- Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.
- Please use all caps for the message.

## Solución

```
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto_2019]
└─$ ls -la
total 112
drwxr-xr-x 2 kali kali   4096 Apr 18 00:18 .
drwxr-xr-x 3 kali kali   4096 Apr 17 23:02 ..
-rw-r--r-- 1 kali kali   1571 Apr 18 00:18 table.txt
-rw-r--r-- 1 kali kali 100721 Apr 17 23:05 the_numbers.png
                                                                                                    
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto_2019]
└─$ open table.txt  

```
![[Retos-picoCTF/Retos Crypto/Retos -crypto  - parte 1/02-Easy 1/solución.png]]

## Flag

picoCTF{CRYPTOISFUN}

## Notas adicionales

| Archivo | Descripción |
|------------|-------------|
|**Relleno de un solo uso** |Es un tipo de algoritmos de cifrado por el que el texto en claro se combina con una clave aleatoria o «libreta» igual de larga que el texto en claro y que sólo se utiliza una vez. |
|**El cifrado de Vigenère** |Es un cifrado basado en diferentes series de caracteres o letras del cifrado César formando estos caracteres una tabla, llamada tabla de Vigenère, que se usa como clave. El cifrado de Vigenère es un cifrado polialfabético y de sustitución. |
 
## Referencias

[one-time-pad](https://es.wikipedia.org/wiki/Libreta_de_un_solo_uso)
[cifrado de Vigenere](https://www.ugr.es/~anillos/textos/pdf/2011/EXPO-1.Criptografia/02a11.htm)
