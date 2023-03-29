# What Lies Within

## Objetivo

There's something in the [building](https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png). Can you retrieve the flag?

## Hints

There is data encoded somewhere... there might be an online decoder.

## Solución

```
┌──(kali㉿kali)-[~/Downloads]
└─$ ls -la
total 96944
drwxr-xr-x  2 kali kali     4096 Mar 19 00:58 .
drwx------ 19 kali kali     4096 Mar 18 23:36 ..
-rw-r--r--  1 kali kali   625219 Mar 19 00:58 buildings.png
-rw-r--r--  1 kali kali   239455 Mar 18 22:49 capture.pcap
-rw-r--r--  1 kali kali   202552 Mar 15 00:17 ld-linux-x86-64.so.2
-rwxr-xr-x  1 kali kali 98186710 Mar 14 10:27 Obsidian-1.1.16.AppImage
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ file buildings.png

buildings.png: PNG image data, 657 x 438, 8-bit/color RGBA, non-interlaced
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ open buildings.png                   

                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo gem install zsteg                          
[sudo] password for kali: 
kFetching zsteg-0.2.13.gem
Fetching rainbow-3.1.1.gem
Fetching zpng-0.4.5.gem
Fetching iostruct-0.0.5.gem
Successfully installed rainbow-3.1.1
Successfully installed zpng-0.4.5
Successfully installed iostruct-0.0.5
Successfully installed zsteg-0.2.13
Parsing documentation for rainbow-3.1.1
Installing ri documentation for rainbow-3.1.1
Parsing documentation for zpng-0.4.5
Installing ri documentation for zpng-0.4.5
Parsing documentation for iostruct-0.0.5
Installing ri documentation for iostruct-0.0.5
Parsing documentation for zsteg-0.2.13
Installing ri documentation for zsteg-0.2.13
Done installing documentation for rainbow, zpng, iostruct, zsteg after 3 seconds
4 gems installed
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ zsteg buildings.png  
b1,r,lsb,xy         .. text: "^5>R5YZrG"
b1,rgb,lsb,xy       .. text: "picoCTF{h1d1ng_1n_th3_b1t5}"
b1,abgr,msb,xy      .. file: PGP Secret Sub-key -
b2,b,lsb,xy         .. text: "XuH}p#8Iy="
b3,abgr,msb,xy      .. text: "t@Wp-_tH_v\r"
b4,r,lsb,xy         .. text: "fdD\"\"\"\" "
b4,r,msb,xy         .. text: "%Q#gpSv0c05"
b4,g,lsb,xy         .. text: "fDfffDD\"\""
b4,g,msb,xy         .. text: "f\"fff\"\"DD"
b4,b,lsb,xy         .. text: "\"$BDDDDf"
b4,b,msb,xy         .. text: "wwBDDDfUU53w"
b4,rgb,msb,xy       .. text: "dUcv%F#A`"
b4,bgr,msb,xy       .. text: " V\"c7Ga4"
b4,abgr,msb,xy      .. text: "gOC_$_@o"
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ zsteg buildings.png | grep pico
b1,rgb,lsb,xy       .. text: "picoCTF{h1d1ng_1n_th3_b1t5}"
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ 

```

## Flag

picoCTF{h1d1ng_1n_th3_b1t5}

## Notas adicionales

| Archivo | Descripción |
|------------|-------------|
| zsteg| Sirve para detectar datos ocultos en PNG o BMP|

## Referencias

[steganography](https://www.simplilearn.com/what-is-steganography-article)
[steganography online](https://stylesuxx.github.io/steganography/)