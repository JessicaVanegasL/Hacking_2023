# caesar

## Objetivo

Decrypt this [message](https://jupiter.challenges.picoctf.org/static/49f31c8f17817dc2d367428c9e5ab0bc/ciphertext).

## Hints

caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)

## Solución

```
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto_2019]
└─$ ls -la
total 16
drwxr-xr-x 2 kali kali 4096 Apr 18 15:33 .
drwxr-xr-x 3 kali kali 4096 Apr 17 23:02 ..
-rw-r--r-- 1 kali kali   35 Apr 18 15:19 ciphertext
-rw-r--r-- 1 kali kali 1024 Apr 18 15:33 .exp.py.swp
                                                                          
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto_2019]
└─$ cat ciphertext
picoCTF{ynkooejcpdanqxeykjrbdofgkq}   
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto_2019]
└─$ python3 exp.py
xmjnndiboczmpwdxjiqacnefjp
                                                                          
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto_2019]
└─$ python3 exp.py
crossingtherubiconvfhsjkou
```


## Flag

picoCTF{crossingtherubiconvfhsjkou}

## Notas adicionales

- **Cifrado Cear**
Conocido como cifrado por desplazamiento, es una de las formas más antiguas y sencillas de cifrar un mensaje.
Es un tipo de cifrado de sustitución en el que cada letra del mensaje original (que en criptografía se llama texto sin formato) se reemplaza con una letra correspondiente a un cierto número de letras desplazadas hacia arriba o hacia abajo en el alfabeto.
Para cada letra del alfabeto, tomaría su posición en el alfabeto, diría 3 para la letra 'C' y la cambiaría por el número clave. Si tuviéramos una clave de +3, esa 'C' se cambiaría a una 'F', y ese mismo proceso se aplicaría a cada letra en el texto sin formato.

## Referencias

[cesar ciphe](https://privacycanada.net/classical-encryption/caesar-cipher/)
[CyberChef](https://gchq.github.io/CyberChef/#recipe=A1Z26_Cipher_Decode('Space')&input=MTYgOSAzIDE1IDMgMjAgNiB7IDIwIDggNQoxNCAyMSAxMyAyIDUgMTggMTkgMTMgMSAKMTkgMTUgMTQgfQ)
