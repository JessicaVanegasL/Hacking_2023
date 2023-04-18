# Tapping

## Objetivo

Theres tapping coming in from the wires. What's it saying `nc jupiter.challenges.picoctf.org 9422`.

## Hints

- What kind of encoding uses dashes and dots?
- The flag is in the format PICOCTF{}

## Solución

```
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto_2019]
└─$ nc jupiter.challenges.picoctf.org 9422
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- -.... ---.. ...-- ---.. ..--- ....- -.... .---- ----- } 
```

![[Soluciòn.png]]

## Flag

picoCTF{M0RS3C0D31SFUN2683824610}

## Notas adicionales

**El código Morse** es un método utilizado en telecomunicaciones para codificar caracteres de texto como secuencias estandarizadas de dos duraciones de señal diferentes, llamadas _puntos_ y _rayas_ , o _puntos_ y _rayas_ . El código Morse lleva el nombre de Samuel Morse , uno de los inventores del telégrafo .

**El código Morse internacional** codifica las 26  letras latinas básicas de **la a** a la **z** , una letra latina acentuada (**é** ), los números arábigos y un pequeño conjunto de signos de puntuación y de procedimiento . No hay distinción entre mayúsculas y minúsculas. Cada símbolo del código Morse está formado por una secuencia de _dits_ y _dahs_ .
 
## Referencias

[morse code](https://en.wikipedia.org/wiki/Morse_code)
[CyberChef](https://gchq.github.io/CyberChef/)
