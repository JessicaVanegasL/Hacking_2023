# MacroHard WeakEdge

## Objetivo


## Hints



## Solución

```
┌──(kali㉿kali)-[~/Downloads]
└─$ ls    
'Forensics is fun.pptm'   sstv
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ unzip Forensics\ is\ fun.pptm
Archive:  Forensics is fun.pptm
  inflating: [Content_Types].xml     
  inflating: _rels/.rels             
  inflating: ppt/presentation.xml 
┌──(kali㉿kali)-[~/Downloads]
└─$ echo "Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q" | tr -d " "
ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ
┌──(kali㉿kali)-[~/Downloads]
└─$ echo "Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q" | tr -d " " | base64 -d
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}base64: invalid input
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ 
```

- Utilizando el explorador de archivos para observar la cadena de texto en el archivo hidden
```
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
```

## Flag

picoCTF{D1d_u_kn0w_ppts_r_z1p5}

## Notas adicionales

| Archivo | Descripción |
|------------|-------------|
| tr -d " "|  Permite eliminar los espacios de una cadena |

## Referencias

[.pptm](https://www.reviversoft.com/es/file-extensions/pptm)