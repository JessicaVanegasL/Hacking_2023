# Wave a flag

## Objetivo

Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm) has extraordinarily helpful information...

## Hints

* 1.- This program will only work in the webshell or another Linux computer.
* 2.- To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm`
* 3.- Run this program by entering the following in the Terminal prompt: `$ ./warm`, but you'll first have to make it executable with `$ chmod +x warm`
* 4.- -h and --help are the most common arguments to give to programs to get more information from them!
* 5.- Not every program implements help features like -h and --help.

## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~/Descargas$ cat warm
Hello user! Pass me a -h to learn what I can do!-hOh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}I don't know what '%s' means! I do know what -h means though!

```
### Solución 2
```
jessi@jessi-Aspire-E5-511:~/Descargas$ chmod +x warm
jessi@jessi-Aspire-E5-511:~/Descargas$ sudo ./warm
[sudo] password for jessi:                
Hello user! Pass me a -h to learn what I can do!
jessi@jessi-Aspire-E5-511:~/Descargas$ sudo ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}
jessi@jessi-Aspire-E5-511:~/Descargas$ 
```

## Flag

picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| chmod |  Sirve para gestionar los permisos de los archivos o directorios del sistema  |
| ./ |  Sirve para la ejecución de un programa  |

## Referencias

[This program](https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm)
