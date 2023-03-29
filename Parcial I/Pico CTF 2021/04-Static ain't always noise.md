# Static ain't always noise

## Objetivo

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/0f6ea599582dcce7b4f1ba94e3617baf/static)? This [BASH script](https://mercury.picoctf.net/static/0f6ea599582dcce7b4f1ba94e3617baf/ltdis.sh) might help!

## Hints

(None)

## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ ls
ltdis.sh  static
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ chmod +x ltdis.sh
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ sudo ./ltdis.sh
[sudo] password for jessi:                
Attempting disassembly of  ...
objdump: 'a.out': No such file
objdump: section '.text' mentioned in a -j option, but not found in any input file
Disassembly failed!
Usage: ltdis.sh <program-file>
Bye!
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ sudo ./ltdis.sh static
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ cat static
picoCTF{d15a5m_t34s3r_6f8c8200}GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.08Tt��`�
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ cat static.ltdis.strings.txt | grep pico 
   1020 picoCTF{d15a5m_t34s3r_6f8c8200}
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ 
```

## Flag

picoCTF{d15a5m_t34s3r_6f8c8200}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| chmod +x |  Permite ejecutar el archivo  |
Y para poder ejecutarlo se toma el archivo *static* ,vaciando al txt **"static.ltdis.strings.txt"**.

## Referencias

[static](https://mercury.picoctf.net/static/0f6ea599582dcce7b4f1ba94e3617baf/static)
[BASH script](https://mercury.picoctf.net/static/0f6ea599582dcce7b4f1ba94e3617baf/ltdis.sh)