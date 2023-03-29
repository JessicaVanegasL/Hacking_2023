## Bandit Level 25 → Level 26

## Objetivo

Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not **/bin/bash**, but something else. Find out what it is, how it works and how to break out of it.

## Datos de acceso
 
**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit25
**Password**: p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d

## Solución

```
bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

exec more ~/text.txt
exit 0
bandit25@bandit:~$ whoami
bandit25
bandit25@bandit:~$ ls -la
total 32
drwxr-xr-x  2 root     root     4096 Feb 21 22:03 .
drwxr-xr-x 70 root     root     4096 Feb 21 22:04 ..
-rw-r-----  1 bandit25 bandit25   33 Feb 21 22:03 .bandit24.password
-r--------  1 bandit25 bandit25 1679 Feb 21 22:03 bandit26.sshkey
-rw-r--r--  1 root     root      220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root     3771 Jan  6  2022 .bashrc
-rw-r-----  1 bandit25 bandit25    4 Feb 21 22:03 .pin
-rw-r--r--  1 root     root      807 Jan  6  2022 .profile
bandit25@bandit:~$  ssh -i bandit26.sshkey bandit26@localhost -p 2220
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit25/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit25/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

!!! You are trying to log into this SSH server with a password on port 2220 from localhost.

  Enjoy your stay!

  _                     _ _ _   ___   __  
 | |                   | (_) | |__ \ / /  
 | |__   __ _ _ __   __| |_| |_   ) / /_  
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \ 
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/ 
Connection to localhost closed.
bandit25@bandit:~$ 

bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

exec more ~/text.txt
exit 0
bandit25@bandit:~$ more .profile
--More--(48%) 
v
c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1
~                                                                               
~                                                                               
~                                                                               
"/etc/bandit_pass/bandit26" [readonly] 1L, 33B                1,1           All
~                                                                               
------------------------
Connection to localhost closed.
bandit25@bandit:~$ 
```

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
|  more |  Permite mostrar el texto y editar un archivo mediante v   |
|v| Nos permite editar el texto|
|:q| Nos permite salir de v |
|:e| Nos permite editar |
|:qa!| Nos permite salir |
|:r| Nos ayuda a ejecutar un comando|

## Referencias