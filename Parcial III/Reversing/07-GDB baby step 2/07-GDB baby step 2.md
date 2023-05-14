# GDB baby step 2

## Objetivo

Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`. Debug [this](https://artifacts.picoctf.net/c/520/debugger0_b).

## Hints

You could calculate `eax` yourself, or you could set a breakpoint for after the calculcation and inspect `eax` to let the program do the heavy-lifting for you.

## Solución

```      
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Reversing/07-GDB baby step 2]
└─$ ls
'07-GDB baby step 2.md'   debugger0_b
                                                                                                                    
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Reversing/07-GDB baby step 2]
└─$ chmod +x debugger0_b
                                                                                                                    
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Reversing/07-GDB baby step 2]
└─$ ./debugger0_b       

                                                                                                                    
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Reversing/07-GDB baby step 2]
└─$ gdb debugger0_b     
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
Reading symbols from debugger0_b...
(No debugging symbols found in debugger0_b)
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   %rbp
   0x000000000040110b <+5>:     mov    %rsp,%rbp
   0x000000000040110e <+8>:     mov    %edi,-0x14(%rbp)
   0x0000000000401111 <+11>:    mov    %rsi,-0x20(%rbp)
   0x0000000000401115 <+15>:    movl   $0x1e0da,-0x4(%rbp)
   0x000000000040111c <+22>:    movl   $0x25f,-0xc(%rbp)
   0x0000000000401123 <+29>:    movl   $0x0,-0x8(%rbp)
   0x000000000040112a <+36>:    jmp    0x401136 <main+48>
   0x000000000040112c <+38>:    mov    -0x8(%rbp),%eax
   0x000000000040112f <+41>:    add    %eax,-0x4(%rbp)
   0x0000000000401132 <+44>:    addl   $0x1,-0x8(%rbp)
   0x0000000000401136 <+48>:    mov    -0x8(%rbp),%eax
   0x0000000000401139 <+51>:    cmp    -0xc(%rbp),%eax
   0x000000000040113c <+54>:    jl     0x40112c <main+38>
   0x000000000040113e <+56>:    mov    -0x4(%rbp),%eax
   0x0000000000401141 <+59>:    pop    %rbp
   0x0000000000401142 <+60>:    ret
End of assembler dump.
(gdb) 

```


## Flag

picoCTF{307019}

## Notas adicionales

El codigo  para que se finalize  debe pasar 607 usaremos una formula de gauss s=((1+606)/2)*606 dandonos 183921 + el valor de [rbp-0x4] en decimal que es 123098 

## Referencias

[HEXtoDEC](https://www.rapidtables.com/convert/number/hex-to-decimal.html)