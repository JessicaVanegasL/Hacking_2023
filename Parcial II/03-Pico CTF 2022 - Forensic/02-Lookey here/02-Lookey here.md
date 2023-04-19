# Lookey here

## Objetivo

Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.Download the data [here](https://artifacts.picoctf.net/c/126/anthem.flag.txt).

## Hints

Download the file and search for the flag based on the known prefix.

## Solución

```
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ ls -la
total 120
drwxr-xr-x 3 kali kali   4096 Apr 19 15:43  .
drwxr-xr-x 3 kali kali   4096 Apr 17 23:01  ..
-rw-r--r-- 1 kali kali 108668 Apr 19 15:42  anthem.flag.txt
drwxr-xr-x 2 kali kali   4096 Apr 18 15:57 'Retos Crypto_2019'
                                                                                                        
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ cat anthem.flag.txt | grep pico
      we think that the men of picoCTF{gr3p_15_@w3s0m3_2116b979}
                                                                                                        
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ 
```

## Flag

picoCTF{gr3p_15_@w3s0m3_2116b979}

## Notas adicionales

## Referencias
