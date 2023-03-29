# Warmed Up

## Objetivo

What is 0x3D (base 16) in decimal (base 10)?

## Hints

Submit your answer in our flag format. For example, if your answer was '22', you would submit 'picoCTF{22}' as the flag.

## Solución

### Solución 1
```
jessy_vl-picoctf@webshell:~$ python
Python 3.10.6 (main, Aug 10 2022, 11:40:04) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> int(0x3D)
61
>>>
```

## Flag

picoCTF{61}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| int |  Este comando es utilizado para que Python tome la entrada como un número entero.Sin embargo lo use para  convertir un numero de hexa a decimal (0x). |

## Referencias
[Conversor de hexa a decimal](https://www.chileoffshore.com/es/toolkits/basic-conversion/hexa-to-ascii)
