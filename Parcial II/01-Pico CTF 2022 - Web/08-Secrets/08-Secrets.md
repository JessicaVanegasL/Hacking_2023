# Secrets

## Objetivo

We have several pages hidden. Can you find the one with the flag?The website is running [here](http://saturn.picoctf.net:53932/).

## Hints

folders folders folders

## Solución

```
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8" />

<meta

name="viewport"

content="width=device-width, initial-scale=1, shrink-to-fit=no"

/>

<meta name="description" content="" />

<!-- Bootstrap core CSS -->

<link href="[vendor/bootstrap/css/bootstrap.min.css](http://saturn.picoctf.net:53932/vendor/bootstrap/css/bootstrap.min.css)" rel="stylesheet" />

<!-- title -->

<title>home</title>

<!-- css -->

<link href="[secret/assets/index.css](http://saturn.picoctf.net:53932/secret/assets/index.css)" rel="stylesheet" />

</head>

<body>

<!-- ***** Header Area Start ***** -->

<div class="topnav">

<a class="active" href="[#home](http://saturn.picoctf.net:53932/#home)">Home</a>

<a href="[about.html](http://saturn.picoctf.net:53932/about.html)">About</a>

<a href="[contact.html](http://saturn.picoctf.net:53932/contact.html)">Contact</a>

</div>

  

<div class="imgcontainer">

<img

src="[secret/assets/DX1KYM.jpg](http://saturn.picoctf.net:53932/secret/assets/DX1KYM.jpg)"

alt="https://www.alamy.com/security-safety-word-cloud-concept-image-image67649784.html"

class="responsive"

/>

<div class="top-left">

<h1>If security wasn't your job, would you do it as a hobby?</h1>

</div>

</div>

</body>

</html>
```

- hidden
```
<!DOCTYPE html>

<html>

<head>

<title>LOGIN</title>

<!-- css -->

<link href="[superhidden/login.css](http://saturn.picoctf.net:53932/secret/hidden/superhidden/login.css)" rel="stylesheet" />

</head>

<body>

<form>

<div class="container">

<form method="" action="/secret/assets/popup.js">

<div class="row">

<h2 style="text-align: center">

Login with Social Media or Manually

</h2>

<div class="vl">

<span class="vl-innertext">or</span>

</div>

  

<div class="col">

<a href="[#](http://saturn.picoctf.net:53932/secret/hidden/#)" class="fb btn">

<i class="fa fa-facebook fa-fw"></i> Login with Facebook

</a>

<a href="[#](http://saturn.picoctf.net:53932/secret/hidden/#)" class="twitter btn">

<i class="fa fa-twitter fa-fw"></i> Login with Twitter

</a>

<a href="[#](http://saturn.picoctf.net:53932/secret/hidden/#)" class="google btn">

<i class="fa fa-google fa-fw"></i> Login with Google+

</a>

</div>

  

<div class="col">

<div class="hide-md-lg">

<p>Or sign in manually:</p>

</div>

  

<input

type="text"

name="username"

placeholder="Username"

required

/>

<input

type="password"

name="password"

placeholder="Password"

required

/>

<input type="hidden" name="db" value="superhidden/xdfgwd.html" />

  

<input

type="submit"

value="Login"

onclick="alert('Thank you for the attempt but oops! try harder. better luck next time')"

/>

</div>

</div>

</form>

</div>

  

<div class="bottom-container">

<div class="row">

<div class="col">

<a href="[#](http://saturn.picoctf.net:53932/secret/hidden/#)" style="color: white" class="btn">Sign up</a>

</div>

<div class="col">

<a href="[#](http://saturn.picoctf.net:53932/secret/hidden/#)" style="color: white" class="btn">Forgot password?</a>

</div>

</div>

</div>

</form>

</body>

</html>
```

![[Parcial II/01-Pico CTF 2022 - Web/08-Secrets/solución.png]]

## Flag

picoCTF{succ3ss_@h3n1c@10n_51b260fe}

## Notas adicionales

## Referencias
