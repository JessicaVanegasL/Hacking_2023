# runme.py

## Objetivo

Run the `runme.py` script to get the flag. Download the script with your browser or with `wget` in the webshell.[Download runme.py Python script](https://artifacts.picoctf.net/c/86/runme.py)

## Hints

* 1.- If you have Python on your computer, you can download the script normally and run it. Otherwise, use the `wget` command in the webshell.
* 2.- To use `wget` in the webshell, first right click on the download link and select 'Copy Link' or 'Copy Link Address'
* 3.- Type everything after the dollar sign in the webshell: `$ wget` , then paste the link after the space after `wget` and press enter. This will download the script for you in the webshell so you can run it!
* 4.- Finally, to run the script, type everything after the dollar sign and then press enter: `$ python3 runme.py` You should have the flag now!

## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~$ wget https://artifacts.picoctf.net/c/86/runme.py
--2023-03-02 21:46:30--  https://artifacts.picoctf.net/c/86/runme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 13.249.74.56, 13.249.74.17, 13.249.74.22, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|13.249.74.56|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 270 [application/octet-stream]
Saving to: ‘runme.py’

runme.py            100%[===================>]     270  --.-KB/s    in 0s      

2023-03-02 21:46:31 (5.33 MB/s) - ‘runme.py’ saved [270/270]
jessi@jessi-Aspire-E5-511:~$ python3 runme.py
picoCTF{run_s4n1ty_run}
jessi@jessi-Aspire-E5-511:~$ 

```

## Flag

picoCTF{run_s4n1ty_run}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| python3 |  Permite entrar a la terminal de Python y poder correr el programa *.py* |


## Referencias

[Download runme.py Python script](https://artifacts.picoctf.net/c/86/runme.py)