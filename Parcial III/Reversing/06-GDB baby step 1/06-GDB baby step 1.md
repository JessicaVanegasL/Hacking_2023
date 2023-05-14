# GDB baby step 1

## Objetivo

Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.Disassemble [this](https://artifacts.picoctf.net/c/512/debugger0_a).

## Hints

- gdb is a very good debugger to use for this problem and many others!
- `main` is actually a recognized symbol that can be used with gdb commands.

## Solución

```      
                                                                                                                    
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Reversing/06-GDB baby step 1]
└─$ ls               
'06-GDB baby step 1.md'   debugger0_a
                                                                                                                    
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Reversing/06-GDB baby step 1]
└─$ chmod +x debugger0_a
                                                                                                                    
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Reversing/06-GDB baby step 1]
└─$ ./debugger0_a

                                                                                                                    
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Reversing/06-GDB baby step 1]
└─$ gdb debugger0_a
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
Reading symbols from debugger0_a...
(No debugging symbols found in debugger0_a)
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000001129 <+0>:     endbr64
   0x000000000000112d <+4>:     push   %rbp
   0x000000000000112e <+5>:     mov    %rsp,%rbp
   0x0000000000001131 <+8>:     mov    %edi,-0x4(%rbp)
   0x0000000000001134 <+11>:    mov    %rsi,-0x10(%rbp)
   0x0000000000001138 <+15>:    mov    $0x86342,%eax
   0x000000000000113d <+20>:    pop    %rbp
   0x000000000000113e <+21>:    ret
End of assembler dump.
(gdb) 

```


## Flag

picoCTF{549698}

## Notas adicionales

El valor "0x86342" en decimal es *549698*

## Referencias

[HEXtoDEC](https://www.rapidtables.com/convert/number/hex-to-decimal.html)