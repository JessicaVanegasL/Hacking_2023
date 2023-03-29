## Bandit Level 11 → Level 12

## Objetivo

The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions.

## Datos de acceso
 
**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit11
**Password**:  6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM

## Solución

```
bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
bandit11@bandit:~$ cat data.txt | tr "a-zA-Z" "n-za-mN-ZA-M"
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
bandit11@bandit:~$

bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
bandit11@bandit:~$ python3
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import codecs
>>> codecs.decode('Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi','rot13')
'The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv'
>>>
bandit11@bandit:~$
```

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| ls |  Lista archivos  |
| cat |  Muestra contenido  |
| tr |  Copia la entrada estándar en la salida estándar sustituyendo o borrando los caracteres seleccionados incluso puede cambiar buscar palabras,eliminar.  |
| python3 | Permite correr los scripts de python  |
| codecs.decode | Recibe parámetros de la cadena de caracteres y hace la función  |
| rot13  | Función de python que permite a decifrar el algoritmo rot13   |

La sintaxis para usar el comando `tr` tiene la siguiente estructura:

```shell
tr Opciones conjunto_caracteres_1 conjunto_caracteres_2
```
Donde:

`tr`: Parte del comando que hace que se ejecute la utilidad tr.

`Opciones`: Se puede dejar en blanco o usar las opciones `-c`, `-d`, `-s`, y `-t`. En los ejemplos del siguiente apartado verán como pueden usar todas y cada una de de las opciones.

`conjunto_caracteres_1`: Conjunto de caracteres que se buscaran en un texto.

`conjunto_caracteres_2`: Conjunto de caracteres que se usarán para modificar un texto.

## Referencias

[tr](https://geekland.eu/uso-del-comando-tr-en-linux-y-unix-con-ejemplos/)
[Rot13 on Wikipedia](https://en.wikipedia.org/wiki/Rot13)