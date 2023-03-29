## Bandit Level 10 → Level 11

## Objetivo

The password for the next level is stored in the file **data.txt**, which contains base64 encoded data.

## Datos de acceso
 
**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit10
**Password**: G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s

## Solución

```
bandit10@bandit:~$ ls
data.txt                                      
bandit10@bandit:~$ ls -la                     
total 24                                      
drwxr-xr-x  2 root     root     4096 Jan 11 19:18 .
drwxr-xr-x 70 root     root     4096 Jan 11 19:19 ..
-rw-r--r--  1 root     root      220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root     3771 Jan  6  2022 .bashrc
-rw-r-----  1 bandit11 bandit10   69 Jan 11 19:18 data.txt
-rw-r--r--  1 root     root      807 Jan  6  2022 .profile
bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==
bandit10@bandit:~$ cat data.txt | base64 -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
bandit10@bandit:~$ base64 -d data.txt
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
bandit10@bandit:~$ echo "VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==" | base64 -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
bandit10@bandit:~$ python3
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import base64
>>>base64.b64decode("VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==")b'The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM\n'
>>> 
```

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| ls |  Lista archivos  |
| cat |  Muestra contenido  |
| echo |  Imprime un texto en la terminal  |
| echo -n | Es un interruptor que omite al nuevo caracter de la línea  |
| base64  | Para codificar y decodificar los datos en una cadena o un archivo   |
| base64 -d | Para decodificar el texto contiene la cadena encriptada   |
| base64.b64decode | Es un script de python que permite decodificar datos en base64   |
| python3 | Permite correr los scripts de python  |

## Referencias

[echo](https://tecnonautas.net/como-dar-salida-a-texto-en-la-pantalla-usando-el-comando-linux-echo/)
[Base64 on Wikipedia](https://en.wikipedia.org/wiki/Base64)
[ciberchef](https://gchq.github.io/CyberChef/)
