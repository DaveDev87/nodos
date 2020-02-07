f = open("index.html", "w")

mensaje = """<html>
<head></head>
<body><p>Hola Mundo!</p>
<script>alert("me pelan la verga")</script>
</body>
</html>"""

f.write(mensaje)
f.close