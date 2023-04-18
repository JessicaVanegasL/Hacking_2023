# So Meta

## Objetivo

Find the flag in this [picture](https://jupiter.challenges.picoctf.org/static/89b371a46702a31aa9931a2a2b12f8bf/pico_img.png).

## Hints

- What does meta mean in the context of files?
- Ever heard of metadata?

## Solución

```
┌──(kali㉿kali)-[~/Downloads]
└─$ ls -la
total 108928
drwxr-xr-x  2 kali kali     4096 Mar 18 01:53 .
drwx------ 19 kali kali     4096 Mar 18 01:56 ..
-rw-r--r--  1 kali kali  2295192 Mar 18 01:42 garden.jpg
-rw-r--r--  1 kali kali   202552 Mar 15 00:17 ld-linux-x86-64.so.2
-rwxr-xr-x  1 kali kali 98186710 Mar 14 10:27 Obsidian-1.1.16.AppImage
-rw-r--r--  1 kali kali   108795 Mar 18 01:53 pico_img.png
-rw-r--r--  1 kali kali  4678467 Mar 16 14:49 timer.apk
-rw-r--r--  1 kali kali  6049568 Mar 16 14:52 timer-dex2jar.jar
                                                                                 
┌──(kali㉿kali)-[~/Downloads]
└─$ man exiftool
┌──(kali㉿kali)-[~/Downloads]
└─$ exiftool pico_img.png

ExifTool Version Number         : 12.57
File Name                       : pico_img.png
Directory                       : .
File Size                       : 109 kB
File Modification Date/Time     : 2023:03:18 01:53:54-04:00
File Access Date/Time           : 2023:03:18 01:53:53-04:00
File Inode Change Date/Time     : 2023:03:18 01:53:54-04:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Software                        : Adobe ImageReady
XMP Toolkit                     : Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27
Creator Tool                    : Adobe Photoshop CS6 (Windows)
Instance ID                     : xmp.iid:A5566E73B2B811E8BC7F9A4303DF1F9B
Document ID                     : xmp.did:A5566E74B2B811E8BC7F9A4303DF1F9B
Derived From Instance ID        : xmp.iid:A5566E71B2B811E8BC7F9A4303DF1F9B
Derived From Document ID        : xmp.did:A5566E72B2B811E8BC7F9A4303DF1F9B
Warning                         : [minor] Text/EXIF chunk(s) found after PNG IDAT (may be ignored by some readers)
Artist                          : picoCTF{s0_m3ta_eb36bf44}
Image Size                      : 600x600
Megapixels                      : 0.360
                                                                                 
┌──(kali㉿kali)-[~/Downloads]
└─$ exiftool pico_img.png -Artist

Artist                          : picoCTF{s0_m3ta_eb36bf44}
                                                                                                     
┌──(kali㉿kali)-[~/Downloads]
└─$ strings pico_img.png | grep pico
picoCTF{s0_m3ta_eb36bf44}
                                                                                                     
┌──(kali㉿kali)-[~/Downloads]
└─$ 
```

## Flag

picoCTF{s0_m3ta_eb36bf44}

## Notas adicionales

| Archivo | Descripción |
|------------|-------------|
| exiftool| Sirve para leer, escribir y manipular metadatos de imágenes, audio y video|

## Referencias

[metadata](https://en.wikipedia.org/wiki/Metadata)
