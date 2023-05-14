# Bit-O-Asm-2

## Objetivo

Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.Download the assembly dump [here](https://artifacts.picoctf.net/c/510/disassembler-dump0_b.txt).

## Hints

`PTR`'s or 'pointers', reference a location in memory where values can be stored.

## Solución

```         
┌──(kali㉿kali)-[~/Documents/PicoCTF/Bit-O-Asm-2]
└─$ ls -la                      
total 12
drwxr-xr-x 2 kali kali 4096 May 14 14:28 .
drwxr-xr-x 6 kali kali 4096 May 14 14:19 ..
-rw-r--r-- 1 kali kali  270 May 14 14:27 disassembler-dump0_b.txt
                                                                                                                    
┌──(kali㉿kali)-[~/Documents/PicoCTF/Bit-O-Asm-2]
└─$ cat disassembler-dump0_b.txt
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
<+25>:    pop    rbp
<+26>:    ret
                                                                                                                    
┌──(kali㉿kali)-[~/Documents/PicoCTF/Bit-O-Asm-2]
└─$ 

```


## Flag

picoCTF{654874}

## Notas adicionales

*eax* es  la direccion *rbp-0x4* por lo tanto, la instruccion tiene el valor de *0x9fe1a*.

## Referencias

[HEXtoDEC](https://www.rapidtables.com/convert/number/hex-to-decimal.html)