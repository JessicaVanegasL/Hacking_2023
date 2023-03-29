## Bandit Level 7 → Level 8
## Objetivo

The password for the next level is stored in the file **data.txt** next to the word **millionth**.

## Datos de acceso
 
**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit7
**Password**: z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

## Solución

```
bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ ls -la
total 4108
drwxr-xr-x  2 root    root       4096 Jan 11 19:19 .
drwxr-xr-x 70 root    root       4096 Jan 11 19:19 ..
-rw-r--r--  1 root    root        220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root    root       3771 Jan  6  2022 .bashrc
-rw-r-----  1 bandit8 bandit7 4184396 Jan 11 19:19 data.txt
-rw-r--r--  1 root    root        807 Jan  6  2022 .profile
bandit7@bandit:~$ nano data.txt
TESKZC0XvTetK0S9xNwm25STk5iWrBvP
bandit7@bandit:~$ wc data.txt
bandit7@bandit:~$ grep millionth data.txt
millionth       TESKZC0XvTetK0S9xNwm25STk5iWrBvP
bandit7@bandit:~$
```

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| wc |  Brinda los datos para la cantidad de lineas, caracteres y palabras de un archivo |
| grep |  Filtra la salida para mostrar solo las lineas que coinciden un patron  |
| nano |  Especifíca solamente la palabra  |

## Referencias
