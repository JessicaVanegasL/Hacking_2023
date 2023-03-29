# plumbing

## Objetivo

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `jupiter.challenges.picoctf.org 14291`.

## Hints

* 1.-Remember the flag format is picoCTF{XXXX}
* 2.-What's a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)

## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~$ nc jupiter.challenges.picoctf.org 14291 >> flagout.txt

jessi@jessi-Aspire-E5-511:~$ ls

 flagout.txt                            Público
 hello2                                 strings
jessi@jessi-Aspire-E5-511:~$ cat flagout.txt | grep pico
picoCTF{digital_plumb3r_ea8bfec7}
jessi@jessi-Aspire-E5-511:~$ 

```
## Flag

picoCTF{digital_plumb3r_ea8bfec7}

## Notas adicionales

Cunado nos  conectamos al servidor a traves del puerto 14291, nos brinda una salida con  pipe "|" y  completandolo con el comando **grep.

## Referencias

[PIPE](http://www.linfo.org/pipes.html)
