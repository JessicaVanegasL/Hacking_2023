# convertme.py

## Objetivo

Run the Python script and convert the given number from decimal to binary to get the flag.[Download Python script](https://artifacts.picoctf.net/c/31/convertme.py)

## Hints

* 1.- Look up a decimal to binary number conversion app on the web or use your computer's calculator!
* 2.- The `str_xor` function does not need to be reverse engineered for this challenge.
* 3.- If you have Python on your computer, you can download the script normally and run it. Otherwise, use the `wget` command in the webshell.
* 4.- To use `wget` in the webshell, first right click on the download link and select 'Copy Link' or 'Copy Link Address'
* 5.- Type everything after the dollar sign in the webshell: `$ wget` , then paste the link after the space after `wget` and press enter. This will download the script for you in the webshell so you can run it!
* 6.- Finally, to run the script, type everything after the dollar sign and then press enter: `$ python3 convertme.py`

## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ python3 convertme.py
If 28 is in decimal base, what is it in binary base?
Answer: 11100
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_9c3b7d4d}
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ 
```

## Flag

picoCTF{4ll_y0ur_b4535_9c3b7d4d}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| python3 |  Permite entrar a la terminal de Python y poder correr el programa *.py* |
Y se utiliza un conversor de decimal a binario.

## Referencias

[Download Python script](https://artifacts.picoctf.net/c/31/convertme.py)
[convertir decimal a binario](https://www.rapidtables.com/convert/number/decimal-to-binary.html?x=45)

