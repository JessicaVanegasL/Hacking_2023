# Picker IV

## Objetivo

Can you figure out how this program works to get the flag?

Additional details will be available after launching your challenge instance.
Connect to the program with netcat: `$ nc saturn.picoctf.net 56130` The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/529/picker-IV.c). The binary can be downloaded [here](https://artifacts.picoctf.net/c/529/picker-IV).

## Hints

## Solución

```
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Binary Explotation/01-Picker IV]
└─$ ls                         
'01-Picker IV.md'   picker-IV   picker-IV.c
                                                                                                                                                                      
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Binary Explotation/01-Picker IV]
└─$ chmod +x picker-IV         
                                                                                                                                                                      
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Binary Explotation/01-Picker IV]
└─$ ./picker-IV                
Enter the address in hex to jump to, excluding '0x': ADSFD
You input 0xad
Segfault triggered! Exiting.
CD


^Z
zsh: suspended  ./picker-IV
                                                                                
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Binary Explotation/01-Picker IV]
└─$ gdb picker-IV              
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
Reading symbols from picker-IV...
(No debugging symbols found in picker-IV)
(gdb) layout asm

zsh: suspended  gdb picker-IV
                                                                                                                                                                      
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Binary Explotation/01-Picker IV]
└─$ nc saturn.picoctf.net 56130
Enter the address in hex to jump to, excluding '0x': 40129e
You input 0x40129e
You won!
picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_b8de1af4}
                                                                                                                                                                      
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Binary Explotation/01-Picker IV]
└─$
```


## Flag

picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_b8de1af4}

## Notas adicionales

Analizamos el codigo ensamblador y  buscaremos *win* la direccion donde inicia es *0x40129e*.

## Referencias
