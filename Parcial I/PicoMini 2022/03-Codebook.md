# Codebook

## Objetivo

Run the Python script `code.py` in the same directory as `codebook.txt`.

-   [Download code.py](https://artifacts.picoctf.net/c/102/code.py)
-   [Download codebook.txt](https://artifacts.picoctf.net/c/102/codebook.txt)

## Hints
* 1.- On the webshell, use `ls` to see if both files are in the directory you are in
* 2.- https://play.picoctf.org/practice/challenge/238?category=5&originalEvent=69&page=1#:~:text=The%20str_xor%20function%20does%20not%20need%20to%20be%20reverse%20engineered%20for%20this%20challenge.

## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ ls
Addadshashanammu.zip  codebook.txt  code.py  convertme.py  runme.py
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ python3 code.py
picoCTF{c0d3b00k_455157_197a982c}
jessi@jessi-Aspire-E5-511:~/Descargas/PICO$ 
```

## Flag

picoCTF{c0d3b00k_455157_197a982c}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| python3 |  Permite entrar a la terminal de Python y poder correr el programa *.py* |
Se imprime el *flag* utilizando el archivo .txt
## Referencias

[Download code.py](https://artifacts.picoctf.net/c/102/code.py)
[Download codebook.txt](https://artifacts.picoctf.net/c/102/codebook.txt)
https://play.picoctf.org/practice/challenge/238?category=5&originalEvent=69&page=1#:~:text=The%20str_xor%20function%20does%20not%20need%20to%20be%20reverse%20engineered%20for%20this%20challenge.
