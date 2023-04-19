# Search Source

## Objetivo

The developer of this website mistakenly left an important artifact in the website source, can you find it?The website is [here](http://saturn.picoctf.net:53295/)

## Hints

How could you mirror the website on your local machine so you could use more powerful tools for searching?

## Solución

- style.css
```
/** banner_main picoCTF{1nsp3ti0n_0f_w3bpag3s_8de925a7} **/
 .carousel-indicators li {
     width: 20px;
     height: 20px;
     border-radius: 11px;
     background-color: #070000;
}
 .carousel-indicators li.active {
    background-color: #35a30a;
}
 .carousel-indicators {
     left: inherit;
     top: 53%;
     width: 20px;
     display: block;
}
 .carousel-indicators li {
     margin: 8px 0;
```

## Flag

picoCTF{1nsp3ti0n_0f_w3bpag3s_8de925a7}

## Notas adicionales

## Referencias
