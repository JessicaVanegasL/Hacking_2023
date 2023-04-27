## Descripción
How about we take you on an adventure on exploring certificate signing requests Take a look at this CSR file [here](https://artifacts.picoctf.net/c/379/readmycert.csr).

## Hints
+ Download the certificate signing request and try to read it.


## Solución
```
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto]
└─$ cat readmycert.csr 
-----BEGIN CERTIFICATE REQUEST-----
MIICpzCCAY8CAQAwPDEmMCQGA1UEAwwdcGljb0NURntyZWFkX215Y2VydF82OTNm
N2MwM30xEjAQBgNVBCkMCWN0ZlBsYXllcjCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBAPp+XuDB3ZkmrkvAsgtjP+mjIcYDWfptuZsJieu6eRl39wl4Sg38
+/OfY24LV9sNmgKyTGvpmCaUoZMYkvkulYSoFzE0xqPBo6kruLEyIvqqpAFqRH2b
mierLT6RcKgJHYr/Vt6SwP8NCCawCrvhQ4NZcuB49Hr/2AiGHzmf86/lG/c+lhmH
gyqPb1kDghsVxi/GNs9i7AgniZikqT8OTp0INmmCgZtJn1Jo615Iu/tFiC8Sfhhg
QHmTDLjgx1oP1kvZV2PE5UUN/oC05Zup8f31LksXZwpazZKwYC/LbN96HdqgVQ9K
S8e/4I7MJQmPmLIsLp3sdL2FiDGML3smAi0CAwEAAaAmMCQGCSqGSIb3DQEJDjEX
MBUwEwYDVR0lBAwwCgYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBAOxSR8Fs
Tdjfu9e0vRNqKWd09ISmYDQc3qnSbLRlYZyMK4pguALq310h/1nNgURWESbNJPOp
FkBWG0XWhWyWP7rTqxo/pk9AKx0TNbHDrS6KiBnKPq0mxjPZsH1L7wNYDc5OANDl
btvn3zT7lMms6z1qM7xUWXR76n2xL/81cdF725nBZ00mWmPW0S1pSmA4EEHCEgNW
0vWQqsIDki3gYc4NCm8OHjx79kcwE+ksyc6vHgMOwsYoOFJnyayhl15oN/3x7hW3
G1xovPupABpfOSNOcTwbgfrfjUDOLx/wirvj9L1N5EGDh4FOLaRZDs+tMrimGBBS
zGU13BnykmQ5jOQ=
-----END CERTIFICATE REQUEST-----
                                                                                                                                                                      
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto]
└─$ openssl req -text -in readmycert.csr 
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: CN = picoCTF{read_mycert_693f7c03}, name = ctfPlayer
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:fa:7e:5e:e0:c1:dd:99:26:ae:4b:c0:b2:0b:63:
                    3f:e9:a3:21:c6:03:59:fa:6d:b9:9b:09:89:eb:ba:
                    79:19:77:f7:09:78:4a:0d:fc:fb:f3:9f:63:6e:0b:
                    57:db:0d:9a:02:b2:4c:6b:e9:98:26:94:a1:93:18:
                    92:f9:2e:95:84:a8:17:31:34:c6:a3:c1:a3:a9:2b:
                    b8:b1:32:22:fa:aa:a4:01:6a:44:7d:9b:9a:27:ab:
                    2d:3e:91:70:a8:09:1d:8a:ff:56:de:92:c0:ff:0d:
                    08:26:b0:0a:bb:e1:43:83:59:72:e0:78:f4:7a:ff:
                    d8:08:86:1f:39:9f:f3:af:e5:1b:f7:3e:96:19:87:
                    83:2a:8f:6f:59:03:82:1b:15:c6:2f:c6:36:cf:62:
                    ec:08:27:89:98:a4:a9:3f:0e:4e:9d:08:36:69:82:
                    81:9b:49:9f:52:68:eb:5e:48:bb:fb:45:88:2f:12:
                    7e:18:60:40:79:93:0c:b8:e0:c7:5a:0f:d6:4b:d9:
                    57:63:c4:e5:45:0d:fe:80:b4:e5:9b:a9:f1:fd:f5:
                    2e:4b:17:67:0a:5a:cd:92:b0:60:2f:cb:6c:df:7a:
                    1d:da:a0:55:0f:4a:4b:c7:bf:e0:8e:cc:25:09:8f:
                    98:b2:2c:2e:9d:ec:74:bd:85:88:31:8c:2f:7b:26:
                    02:2d
                Exponent: 65537 (0x10001)
        Attributes:
            Requested Extensions:
                X509v3 Extended Key Usage: 
                    TLS Web Client Authentication
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        ec:52:47:c1:6c:4d:d8:df:bb:d7:b4:bd:13:6a:29:67:74:f4:
        84:a6:60:34:1c:de:a9:d2:6c:b4:65:61:9c:8c:2b:8a:60:b8:
        02:ea:df:5d:21:ff:59:cd:81:44:56:11:26:cd:24:f3:a9:16:
        40:56:1b:45:d6:85:6c:96:3f:ba:d3:ab:1a:3f:a6:4f:40:2b:
        1d:13:35:b1:c3:ad:2e:8a:88:19:ca:3e:ad:26:c6:33:d9:b0:
        7d:4b:ef:03:58:0d:ce:4e:00:d0:e5:6e:db:e7:df:34:fb:94:
        c9:ac:eb:3d:6a:33:bc:54:59:74:7b:ea:7d:b1:2f:ff:35:71:
        d1:7b:db:99:c1:67:4d:26:5a:63:d6:d1:2d:69:4a:60:38:10:
        41:c2:12:03:56:d2:f5:90:aa:c2:03:92:2d:e0:61:ce:0d:0a:
        6f:0e:1e:3c:7b:f6:47:30:13:e9:2c:c9:ce:af:1e:03:0e:c2:
        c6:28:38:52:67:c9:ac:a1:97:5e:68:37:fd:f1:ee:15:b7:1b:
        5c:68:bc:fb:a9:00:1a:5f:39:23:4e:71:3c:1b:81:fa:df:8d:
        40:ce:2f:1f:f0:8a:bb:e3:f4:bd:4d:e4:41:83:87:81:4e:2d:
        a4:59:0e:cf:ad:32:b8:a6:18:10:52:cc:65:35:dc:19:f2:92:
        64:39:8c:e4
-----BEGIN CERTIFICATE REQUEST-----
MIICpzCCAY8CAQAwPDEmMCQGA1UEAwwdcGljb0NURntyZWFkX215Y2VydF82OTNm
N2MwM30xEjAQBgNVBCkMCWN0ZlBsYXllcjCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBAPp+XuDB3ZkmrkvAsgtjP+mjIcYDWfptuZsJieu6eRl39wl4Sg38
+/OfY24LV9sNmgKyTGvpmCaUoZMYkvkulYSoFzE0xqPBo6kruLEyIvqqpAFqRH2b
mierLT6RcKgJHYr/Vt6SwP8NCCawCrvhQ4NZcuB49Hr/2AiGHzmf86/lG/c+lhmH
gyqPb1kDghsVxi/GNs9i7AgniZikqT8OTp0INmmCgZtJn1Jo615Iu/tFiC8Sfhhg
QHmTDLjgx1oP1kvZV2PE5UUN/oC05Zup8f31LksXZwpazZKwYC/LbN96HdqgVQ9K
S8e/4I7MJQmPmLIsLp3sdL2FiDGML3smAi0CAwEAAaAmMCQGCSqGSIb3DQEJDjEX
MBUwEwYDVR0lBAwwCgYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBAOxSR8Fs
Tdjfu9e0vRNqKWd09ISmYDQc3qnSbLRlYZyMK4pguALq310h/1nNgURWESbNJPOp
FkBWG0XWhWyWP7rTqxo/pk9AKx0TNbHDrS6KiBnKPq0mxjPZsH1L7wNYDc5OANDl
btvn3zT7lMms6z1qM7xUWXR76n2xL/81cdF725nBZ00mWmPW0S1pSmA4EEHCEgNW
0vWQqsIDki3gYc4NCm8OHjx79kcwE+ksyc6vHgMOwsYoOFJnyayhl15oN/3x7hW3
G1xovPupABpfOSNOcTwbgfrfjUDOLx/wirvj9L1N5EGDh4FOLaRZDs+tMrimGBBS
zGU13BnykmQ5jOQ=
-----END CERTIFICATE REQUEST-----
                                                                                                                                                                      
┌──(kali㉿kali)-[~/Documents/PicoCTF/Retos Crypto]
└─$ 

```


## Flag

picoCTF{read_mycert_693f7c03}


## Notas adicionales

|Comando | Descripcion |
|------------ | ------------|
| openssl | herramienta que permite utilizar diversas funciones criptográficas de la biblioteca criptográfica de OpenSSL desde el shell |


## Referencias
+ [csr](https://www.dondominio.com/es/help/242/que-es-csr/)
+ [Decode with openssl](https://stackoverflow.com/questions/201070/how-to-decode-a-csr-file)
