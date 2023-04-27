# Pixelated

## Objetivo

I have these 2 images, can you make a flag out of them? [scrambled1.png](https://mercury.picoctf.net/static/e8054e22552c6aba591cdf7440eb25e4/scrambled1.png) [scrambled2.png](https://mercury.picoctf.net/static/e8054e22552c6aba591cdf7440eb25e4/scrambled2.png)

## Hints

- [https://en.wikipedia.org/wiki/Visual_cryptography](https://en.wikipedia.org/wiki/Visual_cryptography)
- Think of different ways you can "stack" images

## Solución

``` 
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto]
└─$ java -jar /opt/stegsolve.jar
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
```  

```      
                                                                                                                         
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto/opt]
└─$ cd /opt                
                                                                                                                         
┌──(kali㉿kali)-[/opt]
└─$ sudo wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
--2023-04-26 23:37:08--  http://www.caesum.com/handbook/Stegsolve.jar
Resolving www.caesum.com (www.caesum.com)... 216.234.173.1
Connecting to www.caesum.com (www.caesum.com)|216.234.173.1|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 312271 (305K) [application/x-java-archive]
Saving to: ‘stegsolve.jar’

stegsolve.jar                  100%[=================================================>] 304.95K  32.2KB/s    in 10s     

2023-04-26 23:37:20 (29.1 KB/s) - ‘stegsolve.jar’ saved [312271/312271]

                                                                                                                         
┌──(kali㉿kali)-[/opt]
└─$ sudo chmod +x stegsolve.jar                                            
                                                                                                                         
┌──(kali㉿kali)-[/opt]
└─$ sudo chmod +x stegsolve.jar    
```


![[Retos-picoCTF/Retos Crypto/Retos -crypto - parte 3/picoCTF 2021/02-Pixelated/Soluciòn.png]]

## Flag

picoCTF{d72ea4af}

## Notas adicionales


## Referencias

-   [Visual Cryptography]([https://en.wikipedia.org/wiki/Visual_cryptography](https://en.wikipedia.org/wiki/Visual_cryptography)
-   [stegsolve](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install)
