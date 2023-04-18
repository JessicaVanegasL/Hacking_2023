# WebNet0

## Objetivo

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/picopico.key). Recover the flag.

## Hints

* Try using a tool like Wireshark.
* How can you decrypt the TLS stream?

## Solución

```
┌──(kali㉿kali)-[~/Downloads]
└─$ ssldump -r capture.pcap -k picopico.key -d | grep pico
    61 67 3a 20 70 69 63 6f 43 54 46 7b 6e 6f 6e 67    ag: picoCTF{nong
    67 3a 20 70 69 63 6f 43 54 46 7b 6e 6f 6e 67 73    g: picoCTF{nongs
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ ssldump -r capture.pcap -k picopico.key -d | grep pico -A 2
    61 67 3a 20 70 69 63 6f 43 54 46 7b 6e 6f 6e 67    ag: picoCTF{nong
    73 68 69 6d 2e 73 68 72 69 6d 70 2e 63 72 61 63    shim.shrimp.crac
    6b 65 72 73 7d 0d 0a 43 6f 6e 74 65 6e 74 2d 4c    kers}..Content-L
--
    67 3a 20 70 69 63 6f 43 54 46 7b 6e 6f 6e 67 73    g: picoCTF{nongs
    68 69 6d 2e 73 68 72 69 6d 70 2e 63 72 61 63 6b    him.shrimp.crack
    65 72 73 7d 0d 0a 43 6f 6e 74 65 6e 74 2d 4c 65    ers}..Content-Le
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ 

```

## Flag

picoCTF{nongshim.shrimp.crackers}

## Notas adicionales

| Archivo | Descripción |
|------------|-------------|
| ssldump| Permite rastrear una conexión TCP|
| -k | Permite pasar la key de SSL|
| -r | Permite para pasar la captura |

## Referencias

[tls](https://en.wikipedia.org/wiki/Unicode)
