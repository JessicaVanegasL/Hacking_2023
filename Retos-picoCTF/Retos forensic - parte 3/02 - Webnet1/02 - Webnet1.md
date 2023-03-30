# Webnet1

## Objetivo

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/picopico.key). Recover the flag.

## Hints

- Try using a tool like Wireshark.
- How can you decrypt the TLS stream?

## Solución

```
┌──(kali㉿kali)-[~/Downloads]
└─$ ls -la
total 132
drwxr-xr-x  3 kali kali 28672 Mar 30 00:45 .
drwx------ 18 kali kali  4096 Mar 30 00:22 ..
-rw-r--r--  1 kali kali 92525 Mar 30 00:45 capture.pcap
-rw-r--r--  1 kali kali  1704 Mar 30 00:45 picopico.key
drwxr-xr-x  9 root root  4096 Mar 19 02:41 sstv
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ wireshark capture.pcap  
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ ssldump -r capture.pcap -k picopico.key -d | grep pico     
    61 67 3a 20 70 69 63 6f 43 54 46 7b 74 68 69 73    ag: picoCTF{this
    67 3a 20 70 69 63 6f 43 54 46 7b 74 68 69 73 2e    g: picoCTF{this.
    Pico-Flag: picoCTF{this.is.not.your.flag.anymore}
    00 00 00 01 00 00 00 01 70 69 63 6f 43 54 46 7b    ........picoCTF{
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ ssldump -r capture.pcap -k picopico.key -d | grep pico -A 2
    61 67 3a 20 70 69 63 6f 43 54 46 7b 74 68 69 73    ag: picoCTF{this
    2e 69 73 2e 6e 6f 74 2e 79 6f 75 72 2e 66 6c 61    .is.not.your.fla
    67 2e 61 6e 79 6d 6f 72 65 7d 0d 0a 43 6f 6e 74    g.anymore}..Cont
--
    67 3a 20 70 69 63 6f 43 54 46 7b 74 68 69 73 2e    g: picoCTF{this.
    69 73 2e 6e 6f 74 2e 79 6f 75 72 2e 66 6c 61 67    is.not.your.flag
    2e 61 6e 79 6d 6f 72 65 7d 0d 0a 43 6f 6e 74 65    .anymore}..Conte
--
    Pico-Flag: picoCTF{this.is.not.your.flag.anymore}
    Keep-Alive: timeout=5, max=99
    Connection: Keep-Alive
--
    00 00 00 01 00 00 00 01 70 69 63 6f 43 54 46 7b    ........picoCTF{
    68 6f 6e 65 79 2e 72 6f 61 73 74 65 64 2e 70 65    honey.roasted.pe
    61 6e 75 74 73 7d 00 00 ff e2 02 1c 49 43 43 5f    anuts}......ICC_
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ 
```

## Flag

picoCTF{honey.roasted.peanuts}

## Notas adicionales

| Archivo | Descripción |
|------------|-------------|
| ssldump| Permite rastrear una conexión TCP|
| -k | Permite pasar la key de SSL|
| -r | Permite para pasar la captura |

## Referencias

[tls](https://en.wikipedia.org/wiki/Unicode)