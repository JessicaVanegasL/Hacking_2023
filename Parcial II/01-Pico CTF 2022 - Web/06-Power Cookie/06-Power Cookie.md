# Power Cookie

## Objetivo

Can you get the flag?Go to this [website](http://saturn.picoctf.net:57329/) and see what you can discover.

## Hints

Do you know how to modify cookies?

## Solución

- guest.js
```
function continueAsGuest()
{
  window.location.href = '/check.php';
  document.cookie = "isAdmin=0";
}
```

![[Parcial II/01-Pico CTF 2022 - Web/06-Power Cookie/solución.png]]

## Flag

picoCTF{gr4d3_A_c00k13_65fd1e1a}

## Notas adicionales

## Referencias

[Download runme.py Python script](https://artifacts.picoctf.net/c/86/runme.py)