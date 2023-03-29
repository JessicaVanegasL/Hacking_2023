# what's a net cat

## Objetivo

Using netcat (nc) is going to be pretty important. Can you connect to `jupiter.challenges.picoctf.org` at port `25103` to get the flag?

## Hints

nc [tutorial](https://linux.die.net/man/1/nc)

## Solución

### Solución 1
```
jessy_vl-picoctf@webshell:~$ nc
usage: nc [-46CDdFhklNnrStUuvZz] [-I length] [-i interval] [-M ttl]
          [-m minttl] [-O length] [-P proxy_username] [-p source_port]
          [-q seconds] [-s sourceaddr] [-T keyword] [-V rtable] [-W recvlimit]
          [-w timeout] [-X proxy_protocol] [-x proxy_address[:port]]
          [destination] [port]
jessy_vl-picoctf@webshell:~$ netcat jupiter.challenges.picoctf.org 25103
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_d0c64587}
>>> 
```

## Flag

picoCTF{nEtCat_Mast3ry_d0c64587}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| nc (netcat) |  Comando que permite acceder a puertos TCP o UDP de la propia máquina o de otras máquinas remotas. También permite quedar a la escucha en un puerto dado (TCP o UDP) de la máquina local.   |


## Referencias

[nc](https://www.neoguias.com/comando-nc/)