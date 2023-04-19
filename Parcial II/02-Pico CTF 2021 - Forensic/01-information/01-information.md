# information

## Objetivo

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/e5825f58ef798fdd1af3f6013592a971/cat.jpg)

## Hints

- Look at the details of the file
- Make sure to submit the flag as picoCTF{XXXXX}

## Solución

```
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ cat cat.jpg | grep pico                                         
                                                                     
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ exiftool                     

Syntax:  exiftool [OPTIONS] FILE

Consult the exiftool documentation for a full list of options.
                                                                     
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ exiftool cat.jpg

ExifTool Version Number         : 12.57
File Name                       : cat.jpg
Directory                       : .
File Size                       : 878 kB
File Modification Date/Time     : 2023:04:19 01:33:51-04:00
File Access Date/Time           : 2023:04:19 01:34:01-04:00
File Inode Change Date/Time     : 2023:04:19 01:34:01-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
                                        
```

## Flag

picoCTF{the_m3tadata_1s_modified}

## Notas adicionales

**ExifTool** es un programa de software gratuito y de código abierto que se utiliza para leer, escribir y actualizar metadatos de varios tipos de archivos.


## Referencias

[exiftool](https://www.poftut.com/how-to-install-and-use-exiftool-in-linux-windows-kali-ubuntu-mint-with-examples/)