# strings it

## Objetivo

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings) without running it?

## Hints

[strings](https://linux.die.net/man/1/strings)

## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~$ wget https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings
--2023-03-02 11:06:37--  https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 776032 (758K) [application/octet-stream]
Saving to: ‘strings’

strings             100%[===================>] 757.84K   929KB/s    in 0.8s    

2023-03-02 11:06:39 (929 KB/s) - ‘strings’ saved [776032/776032]

jessi@jessi-Aspire-E5-511:~$ strings strings | grep pico
picoCTF{5tRIng5_1T_d66c7bb7}
jessi@jessi-Aspire-E5-511:~$ 

```
## Flag

picoCTF{5tRIng5_1T_d66c7bb7}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| wget | Admite protocolos de descarga HTTP, HTTPS y FTP. |
| strings | Muestra las cadenas de caracteres imprimibles que contengan los ficheros, útil para visualizar ficheros que no sean, o que no se sepa que son de texto plano. |
| grep | Busca un patrón que definamos en un archivo de texto |

## Referencias

[strings](https://linux.die.net/man/1/strings)