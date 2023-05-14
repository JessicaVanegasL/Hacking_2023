# transposition-trial

## Objetivo

Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.Download the corrupted message [here](https://artifacts.picoctf.net/c/191/message.txt)

## Hints

Split the message up into blocks of 3 and see how the first block is scrambled

## Solución

```             
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ ls -la
total 12
drwxr-xr-x 2 kali kali 4096 May 12 23:40 .
drwxr-xr-x 3 kali kali 4096 Apr 30 18:17 ..
-rw-r--r-- 1 kali kali   54 May 12 23:40 message.txt
                                                                                                                    
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ cat message.txt
heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4                                                                                                                    
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ touch trans.py                
                                                                                                                    
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ sudo nano trans.py               
[sudo] password for kali: 
                                                                                                                    
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ sudo nano trans.py
                                                                                                                    
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ sudo nano trans.py
                                                                                                                    
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ python3 trans.py
The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}
                                                                                                                    
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$
```

## Flag

picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}

## Notas adicionales

## Referencias
