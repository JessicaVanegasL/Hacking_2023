# extensions

## Objetivo

This is a really weird text file TXT? Can you find the flag?

## Hints

- How do operating systems know what kind of file it is? (It's not just the ending!
- Make sure to submit the flag as picoCTF{XXXXX}

## Solución

```
┌──(kali㉿kali)-[~/Downloads]
└─$ $file flag.txt 
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
┌──(kali㉿kali)-[~/Downloads]
└─$ $mv flag.txt flag.png
┌──(kali㉿kali)-[~/Downloads]
└─$ open flag.png
┌──(kali㉿kali)-[~/Downloads]
└─$
```

## Flag

picoCTF{now_you_know_about_extensions}

## Notas adicionales

| Archivo | Descripción |
|------------|-------------|
| mv | Sirve  para mover archivos y directorios de una ubicación a otra, y es utilizado para renombrar archivos|

## Referencias

[robots.txt](https://es.wikipedia.org/wiki/Est%C3%A1ndar_de_exclusi%C3%B3n_de_robots)
