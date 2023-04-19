# SQL Direct

## Objetivo

Connect to this PostgreSQL server and find the flag!

Additional details will be available after launching your challenge instance.

## Hints



## Solución

```
jessy_vl-picoctf@webshell:~$ psql -h saturn.picoctf.net -p 62235 -U postgres pico
Password for user postgres: 
psql (14.5 (Ubuntu 14.5-0ubuntu0.22.04.1), server 15.2 (Debian 15.2-1.pgdg110+1))
WARNING: psql major version 14, server major version 15.
         Some psql features might not work.
Type "help" for help.

pico=# table flags;
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 rows)

pico=# 
```

## Flag

picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}

## Notas adicionales

- Use el comando *dt* o *dt+* en psql para mostrar tablas en una base de datos específica.

## Referencias

[postgresql-show-tables](https://www.postgresqltutorial.com/postgresql-administration/postgresql-show-tables/)
