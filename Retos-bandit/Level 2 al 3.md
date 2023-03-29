# # Bandit Level 2 → Level 3

## Objetivo

The password for the next level is stored in a file called **spaces in this filename** located in the home directory.

## Datos de acceso

**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit2
**Password**: rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

## Solución
 
```
bandit2@bandit:~$ whoami
bandit2
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat spaces in this filename
cat: spaces: No such file or directory
cat: in: No such file or directory
cat: this: No such file or directory
cat: filename: No such file or directory
bandit2@bandit:~$ cat "spaces in this filename"
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
bandit2@bandit:~$
```

## Notas adicionales

Para leer el contenido de un archivo  se puede leer incluyendo comillas " " o utilizando barras invertidas.

| Comando | Descripción |
|------------|-------------|
| ls |  Lista archivos |
| ls -la |  Lista archivos con formato, incluye archivos ocultos  |
| pwd |  Muestra la ruta del directorio actual  |

## Referencias
[https://linuxhint.com/reference-filename-with-spaces-linux/]

