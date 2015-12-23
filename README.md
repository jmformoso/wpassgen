<h1>Generador de contraseñas</h1>
<p>Incluye varias opciones, desde solo números hasta combinaciones de números, letras y símbolos.</p>
<p><h3>Estas son las opciones:</h3></p>
<ul>
<li>"-l" -> solo letras</li>
<li>"-ll" -> solo letras minúsculas</li>
<li>"-lL" -> solo letras mayúsculas</li>
<li>"-n" -> solo números</li>
<li>"-s" -> solo símbolos</li>
<li>"-o" -> solo signos de puntuación</li>
<li>"-h" -> hexagesimal</li>
<li>"-nl" -> números y letras</li>
<li>"-ns" -> números y símbolos</li>
<li>"-ls" -> letras y símbolos</li>
</ul>
<p><h3>Ejemplos de uso:</h3></p>
<ul>
<li>python wpassgen.py -> devuelve una contraseña de 10 caracteres (por defecto) de longitud con letras, números y símbolos.</li>
<li>python wpassgen.py 11 -> devuelve uan contraseña de 11 caracteres de longitud con letras, números y símbolos.</li>
<li>python wpassgen.py 12 -n -> devuelve una contraseña de 12 con solo números.</li>
<li>python wpassgen.py -n -> devuelve una contraseña de 10 caracteres (por defecto) de longitud con solo números.</li>
</ul>