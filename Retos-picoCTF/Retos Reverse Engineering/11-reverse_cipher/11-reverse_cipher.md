# reverse_cipher

## Objetivo

We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/7aa5f383ec616fe9d72c2ffe1fabd0d9/rev) and a [text file](https://jupiter.challenges.picoctf.org/static/7aa5f383ec616fe9d72c2ffe1fabd0d9/rev_this). Can you reverse the flag.

## Hints

objdump and Gihdra are some tools that could assist with this

## Solución

```    
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ ls
rev  rev_this
                                                                                                                                                                      
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ file rev  
rev: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=523d51973c11197605c76f84d4afb0fe9e59338c, not stripped
                                                                                                                                                                      
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ file rev_this
rev_this: ASCII text, with no line terminators
                                                                                                                                                                      
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ cat rev_this  
picoCTF{w1{1wq84fb<1>49}                                                                                                                                                  
```

```
cifrado=open('rev_this', 'r').read()
print(cifrado)

flag = ''

for i in range (8, len(cifrado)-1):
    if i & 1 == 0:
        flag += chr(ord(cifrado[i])-5)
    else:
        flag += chr(ord(cifrado[i])+2)
        
print(flag)
```

- python3
```
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ python3 exp.py 
python3: can't open file '/home/kali/Documents/PicoCTF/exp.py': [Errno 2] No such file or directory
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ python3 exp.py
picoCTF{w1{1wq84fb<1>49}
r3v3rs36ad73964
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ 
```

## Flag

picoCTF{r3v3rs36ad73964}

## Notas adicionales

## Referencias

-   [x64 assembly](https://www.intel.com/content/dam/develop/external/us/en/documents/introduction-to-x64-assembly-181178.pdf)
-   [ghidra](https://ghidra-sre.org/)
-   [ida-pro](https://hex-rays.com/ida-pro/)