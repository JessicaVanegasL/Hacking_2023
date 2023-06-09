# Scavenger Hunt

## Objetivo

There is some interesting information hidden around this site [http://mercury.picoctf.net:39698/](http://mercury.picoctf.net:39698/). Can you find it?

## Hints

- You should have enough hints to find the files, don't run a brute forcer.

## Solución

- HTML
```
<!doctype html>
<html>
  <head>
    <title>Scavenger Hunt</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans|Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="mycss.css">
    <script type="application/javascript" src="myjs.js"></script>
  </head>

  <body>
    <div class="container">
      <header>
		<h1>Just some boring HTML</h1>
      </header>

      <button class="tablink" onclick="openTab('tabintro', this, '#222')" id="defaultOpen">How</button>
      <button class="tablink" onclick="openTab('tababout', this, '#222')">What</button>

      <div id="tabintro" class="tabcontent">
		<h3>How</h3>
		<p>How do you like my website?</p>
      </div>

      <div id="tababout" class="tabcontent">
		<h3>What</h3>
		<p>I used these to make this site: <br/>
		  HTML <br/>
		  CSS <br/>
		  JS (JavaScript)
		</p>
	<!-- Here's the first part of the flag: picoCTF{t -->
      </div>

    </div>

  </body>
</html>
```

- mycss.css

```
div.container {
    width: 100%;
}

header {
    background-color: black;
    padding: 1em;
    color: white;
    clear: left;
    text-align: center;
}

body {
    font-family: Roboto;
}

h1 {
    color: white;
}

p {
    font-family: "Open Sans";
}

.tablink {
    background-color: #555;
    color: white;
    float: left;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 16px;
    font-size: 17px;
    width: 50%;
}

.tablink:hover {
    background-color: #777;
}

.tabcontent {
    color: #111;
    display: none;
    padding: 50px;
    text-align: center;
}

#tabintro { background-color: #ccc; }
#tababout { background-color: #ccc; }
```

- robots.txt [robots](http://mercury.picoctf.net:39698/robots.txt)

```
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
User-agent: *
Disallow: /index.html

# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```

- htaccess [htaccess](http://mercury.picoctf.net:39698/.htaccess)

```
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

- .DS_Store [.DS_STORE](http://mercury.picoctf.net:39698/.DS_Store)

```
Congrats! You completed the scavenger hunt. Part 5: _fa04427c}
```

## Flag

picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_fa04427c}

## Notas adicionales

| Archivo | Descripción |
|------------|-------------|
|.htaccess files|Los archivos proporcionan una forma de realizar cambios de configuración en cada directorio.|
|.DS_Store| Es un archivo que almacena atributos personalizados de la carpeta que lo contiene, como la posición de los iconos o la imagen de fondo.|

## Referencias

[.htaccess files](https://httpd.apache.org/docs/2.4/en/howto/htaccess.html )
[.DS_Store](https://es.wikipedia.org/wiki/.DS_Store)
