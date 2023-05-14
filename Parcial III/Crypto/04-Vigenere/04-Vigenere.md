# Vigenere

## Objetivo

Can you decrypt this message?Decrypt this [message](https://artifacts.picoctf.net/c/160/cipher.txt) using this key "CYLAB".

## Hints

https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

## Solución

```              
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ ls -la
total 12
drwxr-xr-x 2 kali kali 4096 May 13 00:07 .
drwxr-xr-x 3 kali kali 4096 Apr 30 18:17 ..
-rw-r--r-- 1 kali kali   43 May 13 00:07 cipher.txt
                                                                                                                    
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ cat cipher.txt 
rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}

```

![[Parcial III/Crypto/04-Vigenere/flag.png]]

## Flag

picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_2951a89h}

## Notas adicionales


## Referencias

[Vigenere](https://www.dcode.fr/cifrado-vigenere)