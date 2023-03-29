## Bandit Level 32 → Level 33

## Objetivo


## Datos de acceso
 
**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit32
**Password**:  rmCBvG56y58BXzv98yZGdO7ATVL5dW8y 

## Solución

```
  Enjoy your stay!

WELCOME TO THE UPPERCASE SHELL
>> ls
sh: 1: LS: not found
>> $0
$ whoami
bandit33
$ ls
uppershell
$ cat /etc/bandit_pass/bandit33
odHo63fHiFqcWWJG9rLiLDtPm45KzUKy
$
```

## Notas adicionales

*$0* Permite expandir el nombre del shell, lo cuál corresponde al nombre del shell o shell-script que se está ejecutando.

## Referencias
[$0](http://trajano.us.es/~fjfj/shell/doc/shellscript33.html)
