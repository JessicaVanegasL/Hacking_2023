# Nice netcat...

## Objetivo

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 21135`, but it doesn't speak English...

## Hints
* 1.- You can practice using netcat with this picoGym problem: [what's a netcat?](https://play.picoctf.org/practice/challenge/34)
* 2.- You can practice reading and writing ASCII with this picoGym problem: [Let's Warm Up](https://play.picoctf.org/practice/challenge/22)
## Solución

### Solución 1
```
jessi@jessi-Aspire-E5-511:~$ nc mercury.picoctf.net 21135
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
97 
102 
100 
53 
102 
100 
97 
52 
125 
10 

jessi@jessi-Aspire-E5-511:~$ 
```
## Flag

picoCTF{g00d_k1tty!_n1c3_k1tty!_afd5fda4}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| nc (netcat) |  Comando que permite acceder a puertos TCP o UDP de la propia máquina o de otras máquinas remotas. También permite quedar a la escucha en un puerto dado (TCP o UDP) de la máquina local.   |
Por lo tantoo, cada número es convertido de ascii a texto.

## Referencias
[Conversor ascii](https://www.duplichecker.com/ascii-to-text.php)
