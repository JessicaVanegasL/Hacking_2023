# picobrowser

## Objetivo

This website can be rendered only by **picobrowser**, go and catch the flag! `https://jupiter.challenges.picoctf.org/problem/50522/` ([link](https://jupiter.challenges.picoctf.org/problem/50522/)) or http://jupiter.challenges.picoctf.org:50522

## Hints

You don't need to download a new web browser.

## Solución

### Solución 1
```
jessy_vl-picoctf@webshell:~$ curl -s https://jupiter.challenges.picoctf.org/problem/50522/flag -H "User-Agent: picobrowser" | grep pico
         <!-- <strong>Title</strong> --> picobrowser!
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{p1c0_s3cr3t_ag3nt_51414fa7}</code></p>
jessy_vl-picoctf@webshell:~$ 
```

## Flag

picoCTF{p1c0_s3cr3t_ag3nt_51414fa7}

## Notas adicionales

El *user agent*  permite ver información del cliente, sin embargo, le enviamos la información *user-agent* como picobrowser para tener acceso a la bandera.

## Referencias

[user agent](https://developer.mozilla.org/es/docs/Web/HTTP/Headers/User-Agent)
