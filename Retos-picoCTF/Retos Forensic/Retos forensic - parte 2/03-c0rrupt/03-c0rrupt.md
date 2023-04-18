# c0rrupt

## Objetivo

We found this [file](https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery). Recover the flag.

## Hints

Try fixing the file header

## Solución

```
┌──(kali㉿kali)-[~/Downloads]
└─$ wget https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery
--2023-03-21 09:54:28--  https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 202940 (198K) [application/octet-stream]
Saving to: ‘mystery’

mystery                  100%[==================================>] 198.18K   745KB/s    in 0.3s    

2023-03-21 09:54:29 (745 KB/s) - ‘mystery’ saved [202940/202940]

                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ ls -la             
total 96300
drwxr-xr-x  3 kali kali     4096 Mar 21 09:54 .
drwx------ 19 kali kali     4096 Mar 21 09:54 ..
-rw-r--r--  1 kali kali   202552 Mar 15 00:17 ld-linux-x86-64.so.2
-rw-r--r--  1 kali kali   202940 Oct 26  2020 mystery
-rwxr-xr-x  1 kali kali 98186710 Mar 14 10:27 Obsidian-1.1.16.AppImage
drwxr-xr-x  9 root root     4096 Mar 19 02:41 sstv
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ file mystery       
mystery: data
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ xxd mystery | head       
00000000: 8965 4e34 0d0a b0aa 0000 000d 4322 4452  .eN4........C"DR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 aa00 1625 0000 1625 0149  ..pHYs...%...%.I
00000050: 5224 f0aa aaff a5ab 4445 5478 5eec bd3f  R$......DETx^..?
00000060: 8e64 cd71 bd2d 8b20 2080 9041 8302 08d0  .d.q.-.  ..A....
00000070: f9ed 40a0 f36e 407b 9023 8f1e d720 8b3e  ..@..n@{.#... .>
00000080: b7c1 0d70 0374 b503 ae41 6bf8 bea8 fbdc  ...p.t...Ak.....
00000090: 3e7d 2a22 336f de5b 55dd 3d3d f920 9188  >}*"3o.[U.==. ..

┌──(kali㉿kali)-[~/Downloads]
└─$ file mystery            
mystery: PNG image data, 1642 x 1095, 8-bit/color RGB, non-interlaced

┌──(kali㉿kali)-[~/Downloads]
└─$ sudo apt install pngcheck

┌──(kali㉿kali)-[~/Downloads]
└─$ pngcheck -v mystery 
File: mystery (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 2852132389x5669 pixels/meter
  CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
ERRORS DETECTED in mystery

┌──(kali㉿kali)-[~/Downloads]
└─$ pngcheck -v mystery 
File: mystery (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 5669x5669 pixels/meter (144 dpi)
  chunk IDAT at offset 0x00057, length 65445
    zlib: deflated, 32K window, fast compression
  chunk IDAT at offset 0x10008, length 65524
  chunk IDAT at offset 0x20008, length 65524
  chunk IDAT at offset 0x30008, length 6304
  chunk IEND at offset 0x318b4, length 0
No errors detected in mystery (9 chunks, 96.3% compression).
┌──(kali㉿kali)-[~/Downloads]
└─$ open  mystery            
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ 
```


## Flag

picoCTF{c0rrupt10n_1847995}

## Notas adicionales

| Archivo | Descripción |
|------------|-------------|
|**pngcheck**| verifica la integridad de los archivos PNG, JNG y MNG (verificando los CRC internos de 32 bits, también conocidos como sumas de verificación, y descomprimiendo los datos de la imagen); opcionalmente, puede volcar casi toda la información de nivel de fragmento en la imagen en forma legible por humanos. Por ejemplo, se puede utilizar para imprimir las estadísticas básicas sobre una imagen (dimensiones, profundidad de bits, etc.); para enumerar la información de color y transparencia en su paleta (suponiendo que tenga una); o para extraer las anotaciones de texto incrustadas. Este es un programa de línea de comandos con capacidades por lotes. | 
 

## Referencias

[file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
[pngcheck](http://www.libpng.org/pub/png/apps/pngcheck.html)
