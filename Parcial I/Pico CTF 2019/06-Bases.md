# Bases

## Objetivo

What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.

## Hints

Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solución

### Solución 1
```
jessy_vl-picoctf@webshell:~$ echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d -
l3arn_th3_r0p35jessy_vl-picoctf@webshell:~$ 
>>> 
```
## Flag

picoCTF{l3arn_th3_r0p35}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| base64 -d | Permite hacer una codificación y decodificación a una base de 64. |

## Referencias

[Base64](https://en.wikipedia.org/wiki/Base64)