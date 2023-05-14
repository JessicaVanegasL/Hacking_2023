# Bit-O-Asm-3

## Objetivo

Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`. Download the assembly dump [here](https://artifacts.picoctf.net/c/530/disassembler-dump0_c.txt).

## Hints

Not everything in this disassembly listing is optimal.

## Solución

```     
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Reversing/05-Bit-O-Asm-3]
└─$ ls                          
05-Bit-O-Asm-3.md  disassembler-dump0_c.txt
                                                                                                                    
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Reversing/05-Bit-O-Asm-4]
└─$ cat disassembler-dump0_c.txt
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a 
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc] //eax=0x9fe1a
<+32>:    imul   eax,DWORD PTR [rbp-0x8] //eax=0x27f868 ya que se multiplica por 4
<+36>:    add    eax,0x1f5 // eax= 0x27fa5d ya qeu se le suma 0x1f5
<+41>:    mov    DWORD PTR [rbp-0x4],eax //eax= 0x27fa5d, [rbp-0x4]=0x27fa5d
<+44>:    mov    eax,DWORD PTR [rbp-0x4] // no cambian del anterior
<+47>:    pop    rbp
<+48>:    ret
                                                                                                                    
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Reversing/05-Bit-O-Asm-4]
└─$ 

```

## Flag

picoCTF{2619997}

## Notas adicionales

## Referencias

[HEXtoDEC](https://www.rapidtables.com/convert/number/hex-to-decimal.html)