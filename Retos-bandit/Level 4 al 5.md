## Bandit Level 4 → Level 5

## Objetivo

The password for the next level is stored in the only human-readable file in the **inhere** directory. Tip: if your terminal is messed up, try the “reset” command.

## Datos de acceso
 
**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit4
**Password**: 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

## Solución

```
bandit4@bandit:~/inhere$ whoami
bandit4
bandit4@bandit:~/inhere$ ls
-file00  -file02  -file04  -file06  -file08
-file01  -file03  -file05  -file07  -file09
bandit4@bandit:~/inhere$ cd inhere/
bandit4@bandit:~/inhere$ ls
-file00  -file02  -file04  -file06  -file08
-file01  -file03  -file05  -file07  -file09
bandit4@bandit:~/inhere$ file ./-file00
./-file00: data
bandit4@bandit:~/inhere$ file ./-file0?
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data 
bandit4@bandit:~/inhere$ cat ./-file07
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
bandit4@bandit:~/inhere$ 
```
## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| ls |  Lista archivos |
| ls -la |  Lista archivos con formato, incluye archivos ocultos  |
| pwd |  Muestra la ruta del directorio actual  |
| file |  Identifica el tipo de archivo |
| * |  Comodin que significa todo  |
| ? |  Comodin para sustituir solo una posición: file ./-file0?  |

## Referencias