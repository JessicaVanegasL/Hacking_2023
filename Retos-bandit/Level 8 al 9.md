## Bandit Level 8 → Level 9
## Objetivo

The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once.

## Datos de acceso
 
**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit8
**Password**: TESKZC0XvTetK0S9xNwm25STk5iWrBvP

## Solución

```
bandit8@bandit:~$ ls
data.txt
bandit8@bandit:~$ ls -la
total 56
drwxr-xr-x  2 root    root     4096 Jan 11 19:19 .
drwxr-xr-x 70 root    root     4096 Jan 11 19:19 ..
-rw-r--r--  1 root    root      220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root    root     3771 Jan  6  2022 .bashrc
-rw-r-----  1 bandit9 bandit8 33033 Jan 11 19:19 data.txt
-rw-r--r--  1 root    root      807 Jan  6  2022 .profile
bandit8@bandit:~$ wc data.txt
 1001  1001 33033 data.txt
bandit8@bandit:~$ sort data.txt | uniq -u 
EN632PlfYiZbn3PhVK3XOGSlNInNE00t
bandit8@bandit:~$ 
```

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| wc |  Brinda los datos para la cantidad de lineas, caracteres y palabras de un archivo |
| uniq |  Filtra la salida para mostrar solo las lineas que coinciden un patron  |
| sort |  Ordena las líneas de texto  |
| -c |  Cuenta las líneas repetidas |
| -d |  Muestra las líneas repetidas  |
| -u |  Muestra solo los unicos  |

## Referencias