# Bandit Level 1 → Level 2
## Objetivo

The password for the next level is stored in a file called **-** located in the home directory

## Datos de acceso

**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit1
**Password**: NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

## Solución

```
bandit1@bandit:~$ whoami
bandit1
bandit1@bandit:~$ pwd
/home/bandit1
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat -
^C
bandit1@bandit:~$ cat ./-
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
bandit1@bandit:~$ 
```

## Notas adicionales

Para leer el contenido de un archivo se definide con un "-" al inicio y para leer con el cat con "./-" o utilizando cat /home/bandit1/

| Comando | Descripción |
|------------|-------------|
| ls |  Lista archivos |
| cat |  Muestra contenido |
| pwd |  Muestra la ruta del directorio actual  |
| whoami |  Muestra el nombre de usuario  |

## Referencias
-   [Google Search for “dashed filename”](https://www.google.com/search?q=dashed+filename)
-   [Advanced Bash-scripting Guide - Chapter 3 - Special Characters](https://tldp.org/LDP/abs/html/special-chars.html)