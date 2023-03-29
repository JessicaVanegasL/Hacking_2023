## Bandit Level 20 → Level 21

## Objetivo

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

**NOTE:** Try connecting to your own network daemon to see if it works as you think

## Datos de acceso
 
**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit20
**Password**: VxCazJaVykI6W36BkBU0mJTCM8rR95XT

## Solución

```
bandit20@bandit:~$ ls -la
total 36
drwxr-xr-x  2 root     root      4096 Feb 21 22:03 .
drwxr-xr-x 70 root     root      4096 Feb 21 22:04 ..
-rw-r--r--  1 root     root       220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root      3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root     root       807 Jan  6  2022 .profile
-rwsr-x---  1 bandit21 bandit20 15600 Feb 21 22:03 suconnect
bandit20@bandit:~$ ./suconnect
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.
bandit20@bandit:~$ nc -lnvp 3030 
Listening on 0.0.0.0 3030
bandit20@bandit:~$ nc -lnvp 2022 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT &
[1] 2840016
bandit20@bandit:~$ Listening on 0.0.0.0 2022
bandit20@bandit:~$ ./suconnect 2022
Connection received on 127.0.0.1 39968
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Password matches, sending next password
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
[1]+  Done                    nc -lnvp 2022 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT
bandit20@bandit:~$ 
```

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
|  & |  Permite enviar un proceso a segundo plano  |
|  nc -lnvp|  abre el puerto **l - listen**, **p - puerto**, **n - no resolucion de nombres**, **v - muestra una salida y permite verla**  |
|  jobs | Permite ver el estado de los procesos en los puertos en segundo plano  |

## Referencias