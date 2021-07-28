<h1>Generador de contraseñas</h1>
<p>Simple generador de contraseñas que incluye varias opciones, desde solo números hasta combinaciones de números, letras, símbolos, etc.</p>
<h2>1. Opciones</h2>
<ul>
<li>"-l" -> solo letras</li>
<li>"-ll" -> solo letras minúsculas</li>
<li>"-lL" -> solo letras mayúsculas</li>
<li>"-n" -> solo números</li>
<li>"-s" -> solo símbolos</li>
<li>"-o" -> solo signos de puntuación</li>
<li>"-h" -> hexadecimal</li>
<li>"-nl" -> números y letras</li>
<li>"-ns" -> números y símbolos</li>
<li>"-ls" -> letras y símbolos</li>
<li>"-sy" -> juego de caracteres válidos para Symfony (Mailer)</li>
</ul>
<h2>2. Ejemplos</h2>
<ul>
<li><code>$ python wpassgen.py</code> -> devuelve una contraseña de 12 caracteres (por defecto) de longitud con letras, números y símbolos.</li>
<li><code>$ python wpassgen.py 11</code> -> devuelve una contraseña de 11 caracteres de longitud con letras, números y símbolos.</li>
<li><code>$ python wpassgen.py 13 -n</code> -> devuelve una contraseña de 13 con solo números.</li>
<li><code>$ python wpassgen.py -n</code> -> devuelve una contraseña de 12 caracteres (por defecto) de longitud con solo números.</li>
</ul>
<p><b>Demo</b> con algunas opciones implementadas en <a href="https://wikitel.org/wpassgen" target="_blank">wikitel.org/wpassgen</a></p>
<h2>3. Versión</h2>
<p>La última versión estable es la v0.2.0, compatible tanto con Python 2.x como Python 3.x</p>
<h2>4. Autores</h2>
<p>Código desarrollado por <a href="https://twitter.com/jmformoso" target="_blank">@jmformoso</a> con la colaboración de <a href="https://twitter.com/_spalacios" target="_blank">@_spalacios</a>
<h2>5. Copyright y licencia</h2>
<p>Este código y su documentación se distribuye bajo licencia Apache 2.0</p>

### 6. Redes sociales

[![Twitter Follow](https://img.shields.io/twitter/follow/jmformoso?style=social)](https://twitter.com/jmformoso)
[![GitHub Followers]](https://img.shields.io/github/followers/jmformoso?style=social)
[![Twitter Follow](https://img.shields.io/twitter/follow/wikitel?style=social)](https://twitter.com/wikitel)
[![Twitter Follow](https://img.shields.io/twitter/follow/_spalacios?style=social)](https://twitter.com/_spalacios)