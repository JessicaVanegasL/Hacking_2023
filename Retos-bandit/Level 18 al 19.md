## Bandit Level 18 → Level 19

## Objetivo

The password for the next level is stored in a file **readme** in the homedirectory. Unfortunately, someone has modified **.bashrc** to log you out when you log in with SSH.

## Datos de acceso
 
**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit18
**Password**: hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg

## Solución

```
┌──(jessy22㉿JessicaVanegas)-[~]
└─$ ssh bandit18@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
...
...
Byebye !
Connection to bandit.labs.overthewire.org closed.'

┌──(jessy22㉿JessicaVanegas)-[~]
└─$ ssh bandit18@bandit.labs.overthewire.org -p 2220 ls -la
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 

total 24
drwxr-xr-x  2 root     root     4096 Feb 21 22:02 .
drwxr-xr-x 70 root     root     4096 Feb 21 22:04 ..
-rw-r--r--  1 root     root      220 Jan  6  2022 .bash_logout
-rw-r-----  1 bandit19 bandit18 3794 Feb 21 22:02 .bashrc
-rw-r--r--  1 root     root      807 Jan  6  2022 .profile
-rw-r-----  1 bandit19 bandit18   33 Feb 21 22:02 readme
┌──(jessy22㉿JessicaVanegas)-[~]
└─$ ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
awhqfNnAbc1naukrpqDYcF95h7HoMTrC

┌──(jessy22㉿JessicaVanegas)-[~]
└─$ ssh bandit18@bandit.labs.overthewire.org -p 2220 /bin/bash 
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
ls
readme
cat readme
awhqfNnAbc1naukrpqDYcF95h7HoMTrC
exit
```

## Notas adicionales

Existe la posibilida de poder  ejecutar comandos antes de ejecutar iniciar con el bash del servidor, es por eso que se utiliza el comando **cat** o **bin/bash** para leer solo el password.

## Referencias