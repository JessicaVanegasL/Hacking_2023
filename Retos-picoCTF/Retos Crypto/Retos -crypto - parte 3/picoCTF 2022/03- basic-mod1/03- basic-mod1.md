#  basic-mod1

## Objetivo

We found this weird message being passed around on the servers, we think we have a working decryption scheme.Download the message [here](https://artifacts.picoctf.net/c/128/message.txt).Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Hints

- Do you know what `mod 37` means?
- `mod 37` means modulo 37. It gives the remainder of a number after being divided by 37.

## Solución

``` 
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto]
└─$ ls    
message.txt
                                                                                                                        
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto]
└─$ cat message.txt
165 248 94 346 299 73 198 221 313 137 205 87 336 110 186 69 223 213 216 216 177 138                                                                                                                         
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto]
└─$ nano exp.py   
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto]
└─$ python3 exp.py 
picoCTF{R0UND_N_R0UND_B6B25531}
                                                                                                                         
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto]
└─$ 
```

 - python3
 ```
 datos = open('message.txt').read().split()

flag= ''

for n in datos:
    c=int(n)%37
    if c>=0 and c<=25:
        s=chr(c+65)
    elif c>=26 and c<=35:
        s=chr(c+22)
    else:
        s='_'
    flag+=s
    
print(f"picoCTF{{{flag}}}")

 ```

## Flag

picoCTF{R0UND_N_R0UND_B6B25531}

## Notas adicionales


## Referencias

-   [Padding oracle attack](https://en.wikipedia.org/wiki/Padding_oracle_attack)
-   [Homomorphic encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption)