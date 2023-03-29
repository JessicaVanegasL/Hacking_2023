## Bandit Level 30 → Level 31

## Objetivo


## Datos de acceso
 
**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit30
**Password**:  xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS

## Solución

```
bandit30@bandit:/tmp/j30$ git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit30/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit30/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit30-git@localhost's password: 
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), 299 bytes | 299.00 KiB/s, done.
bandit30@bandit:/tmp/j30$ ls
repo
bandit30@bandit:/tmp/j30$ cd repo
bandit30@bandit:/tmp/j30/repo$ ls
README.md
bandit30@bandit:/tmp/j30/repo$ cat README.md 
just an epmty file... muahaha
bandit30@bandit:/tmp/j30/repo$ git log
commit cf552c166d78421e64ddf52f850e680075d216e1 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:13 2023 +0000

    initial commit of README.md
bandit30@bandit:/tmp/j30/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
bandit30@bandit:/tmp/j30/repo$ git tag
secret
bandit30@bandit:/tmp/j30/repo$ git show secret
OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt
bandit30@bandit:/tmp/j30/repo$ 

```

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
|  git tag |  Muestra una lista de todos los tags, dónde permite hacer una creación,modificación y eliminar   |
| git show| Muestra los detalles de objetos de git (cometarios-etiquetas) |

## Referencias

[Git](https://gist.github.com/dasdo/9ff71c5c0efa037441b6)
