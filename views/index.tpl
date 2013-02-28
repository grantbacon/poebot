<!DOCTYPE html>

<html>
<head>
<title>POE BAWT</title>
<link rel="stylesheet" type="text/css" href="/static/css/index.css" />
<link rel="apple-touch-icon" href="/static/apple-touch-icon.png" />
<link rel="shortcut icon" href="/static/favicon.ico" />
</head>

<body>

<div id="main">
<form id="form" action="#">
<input type='text' name='message' placeholder='poe shall say'> 
<input type='submit' value='speak' id='submit'>
<br> fresh color: <input type='checkbox' id='new_color' name='new_color' value='true'>
</form>

<div id="success"> 
<span id="success_message"> </span>
</div>
<a href="/static/log.html"> log of messages </a>
</div>

<div id="footer">
<span id="footer_message"> <a href="/about"> about the poe bot </a> </span>
</div>

<script type="text/javascript" src="http://code.jquery.com/jquery-1.8.3.min.js"></script>
<script type="text/javascript" src="/static/js/index.js"></script>

</body>
</html>
