## Bandit Level 9 → Level 10

## Objetivo

The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.

## Datos de acceso
 
**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit9
**Password**: EN632PlfYiZbn3PhVK3XOGSlNInNE00t

## Solución

```
bandit9@bandit:~$ ls
data.txt
bandit9@bandit:~$ ls -la
total 40
drwxr-xr-x  2 root     root     4096 Jan 11 19:18 .
drwxr-xr-x 70 root     root     4096 Jan 11 19:19 ..
-rw-r--r--  1 root     root      220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root     3771 Jan  6  2022 .bashrc
-rw-r-----  1 bandit10 bandit9 19379 Jan 11 19:18 data.txt
-rw-r--r--  1 root     root      807 Jan  6  2022 .profile
bandit9@bandit:~$ strings data.txt -n 10
c========== the
h;========== password
========== isT
Q!%     6eSvd]
n.E========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
e:V&nQutgo
bandit9@bandit:~$ strings data.txt -n 10 | grep "="
c========== the
h;========== password
========== isT
n.E========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
bandit9@bandit:~$ 
```

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| grep |  Filtra la salida para mostrar solo las lineas que coinciden un patron  |
| strings |  Sustrae la cadena de texto de un archivo data, solo deja los caracteres que se pueden mostrar  |

## Referencias