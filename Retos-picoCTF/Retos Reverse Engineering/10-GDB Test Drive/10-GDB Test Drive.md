# GDB Test Drive

## Objetivo

Can you get the flag?Download this [binary](https://artifacts.picoctf.net/c/85/gdbme).Here's the test drive instructions:

-   `$ chmod +x gdbme`
-   `$ gdb gdbme`
-   `(gdb) layout asm`
-   `(gdb) break *(main+99)`
-   `(gdb) run`
-   `(gdb) jump *(main+104)`

## Hints

## Solución

```   
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ ls
gdbme
                                                                                               
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ file gdbme          
gdbme: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=eeea2c770465e109c185011ad3a7925a2796ce92, for GNU/Linux 3.2.0, not stripped
                                                                                               
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ chmod +x gdbme         
                                                                                               
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ ./gdbme         
^C
                                                                                               
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ gdb gdbme          
GNU gdb (Debian 13.1-2) 13.1
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from gdbme...
(No debugging symbols found in gdbme)
(gdb) layout asm

```

![[01r.png]]

![[Retos-picoCTF/Retos Reverse Engineering/10-GDB Test Drive/pico.png]]

## Flag

picoCTF{d3bugg3r_dr1v3_197c378a}

## Notas adicionales

## Referencias
