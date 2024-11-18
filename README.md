***Proyecto:***
Sopa de letras

***AUTOR:***
Samuel Velasquez Alzate

***Descipción del proyecto***
Este es un proyecto el cual analiza un archivo de texto que contiene una sopa de letras y una lista de palabras a buscar la cual se busca resolver.
Y una vez resuelto se generará un archivo tipo .json en el cual se almacenará la lista de palabras que se pudo encontrar y palabras que no se encontraron,
este archivo se le entregará al usuario.

***Como ejecutar el proyecto***
Solo basta con tener un archivo de texto con el siguiente formato:
<letras en mayusculas separadas por espacios>
"---"
<lista de palabras en mayusculas a buscar>

Para que el formato se entienda mejor, el proyecto incluye un archivo de ejemplo, el cual puede ser replazado

Ahora solo queda ejecutar el archivo main.py con un compilador de python, como por ejemplo Visual Studio Code

***Aviso***
Si el archivo de texto es reemplazado, asegurese de una de las dos cosas:
1) El archivo de texto nuevo tiene el mismo nombre que el archivo de texto de ejemplo
2) reemplazar la constante "TXT_PATH" en la 3ra linea del archivo main.py por el nombre de el nuevo archivo de texto
