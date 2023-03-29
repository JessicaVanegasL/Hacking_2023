# m00nwalk

## Objetivo

Decode this [message](https://jupiter.challenges.picoctf.org/static/14393e18d98fedbaedbc28896d7ef31a/message.wav) from the moon.

## Hints

- How did pictures from the moon landing get sent back to Earth?
- What is the CMU mascot?, that might help select a RX option

## Solución

```
┌──(kali㉿kali)-[~/Downloads]
└─$ ls -la                      
total 106904
drwxr-xr-x  2 kali kali     4096 Mar 19 02:29 .
drwx------ 19 kali kali     4096 Mar 19 02:29 ..
-rw-r--r--  1 kali kali   202552 Mar 15 00:17 ld-linux-x86-64.so.2
-rw-r--r--  1 kali kali 11066998 Mar 19 02:29 message.wav
-rwxr-xr-x  1 kali kali 98186710 Mar 14 10:27 Obsidian-1.1.16.AppImage
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ file message.wav            

message.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 48000 Hz
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ strings -n 10  message.wav  
$]&,&$$r ^
LSU3X0UXL)>
AK@F<45f+E
┌──(kali㉿kali)-[~/Downloads]
└─$ ls -la 
total 106904
drwxr-xr-x  2 kali kali     4096 Mar 19 02:29 .
drwx------ 19 kali kali     4096 Mar 19 02:29 ..
-rw-r--r--  1 kali kali   202552 Mar 15 00:17 ld-linux-x86-64.so.2
-rw-r--r--  1 kali kali 11066998 Mar 19 02:29 message.wav
-rwxr-xr-x  1 kali kali 98186710 Mar 14 10:27 Obsidian-1.1.16.AppImage
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ open message.wav  
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ 
(parole:5508): xfconf-WARNING **: 02:34:03.506: Failed to set property "parole::/audio/volume": Operation was cancelled

                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ open message.wav
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo git clone https://github.com/colaclanth/sstv.git              
[sudo] password for kali: 
Cloning into 'sstv'...
remote: Enumerating objects: 221, done.
remote: Total 221 (delta 0), reused 0 (delta 0), pack-reused 221
Receiving objects: 100% (221/221), 1.01 MiB | 142.00 KiB/s, done.
Resolving deltas: 100% (140/140), done.
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ cd sstv/                            
                                                                                                    
┌──(kali㉿kali)-[~/Downloads/sstv]
└─$ python3 setup.py install
running install
/usr/lib/python3/dist-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
/usr/lib/python3/dist-packages/setuptools/command/easy_install.py:146: EasyInstallDeprecationWarning: easy_install command is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
error: can't create or remove files in install directory

The following error occurred while trying to add or remove files in the
installation directory:

    [Errno 13] Permission denied: '/usr/local/lib/python3.11/dist-packages/test-easy-install-9842.write-test'

The installation directory you specified (via --install-dir, --prefix, or
the distutils default setting) was:

    /usr/local/lib/python3.11/dist-packages/

Perhaps your account does not have write access to this directory?  If the
installation directory is a system-owned directory, you may need to sign in
as the administrator or "root" account.  If you do not have administrative
access to this machine, you may wish to choose a different installation
directory, preferably one that is listed in your PYTHONPATH environment
variable.

For information on other options, you may wish to consult the
documentation at:

  https://setuptools.pypa.io/en/latest/deprecated/easy_install.html

Please make the appropriate changes for your system and try again.

                                                                                                    
┌──(kali㉿kali)-[~/Downloads/sstv]
└─$ sudo python3 setup.py install                        
running install
                                                                                                    
┌──(kali㉿kali)-[~/Downloads/sstv]
└─$ 
/home/kali/Downloads/result.png

```

## Flag

picoCTF{beep_boop_im_in_space}

## Notas adicionales

| Archivo | Descripción |
|------------|-------------|
| sstv |Sirve para  decodificar videos en imagenes |

## Referencias

[apolo 11 - sstv](https://en.wikipedia.org/wiki/Apollo_11_missing_tapes)
[sstv decoder git repo](https://github.com/colaclanth/sstv)
