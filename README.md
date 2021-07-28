# Generador de contraseñas
> by @jmformoso & @palacios22c

Simple generador de contraseñas que incluye varias opciones, desde solo números hasta combinaciones de números, letras, símbolos, etc.
## 1. Opciones

* "-l" -> solo letras
* "-ll" -> solo letras minúsculas
* "-lL" -> solo letras mayúsculas
* "-n" -> solo números
* "-s" -> solo símbolos
* "-o" -> solo signos de puntuación
* "-h" -> hexadecimal
* "-nl" -> números y letras
* "-ns" -> números y símbolos
* "-ls" -> letras y símbolos
* "-sy" -> juego de caracteres válidos para Symfony (Mailer)

## 2. Ejemplos

* ```$ python wpassgen.py``` -> devuelve una contraseña de 12 caracteres (por defecto) de longitud con letras, números y símbolos.
* ```$ python wpassgen.py 11``` -> devuelve una contraseña de 11 caracteres de longitud con letras, números y símbolos.
* ```$ python wpassgen.py 13 -n``` -> devuelve una contraseña de 13 con solo números.
* ```$ python wpassgen.py -n``` -> devuelve una contraseña de 12 caracteres (por defecto) de longitud con solo números.

Demo con algunas opciones implementadas en [wikitel.org/wpassgen](https://wikitel.org/wpassgen)

## 3. Versión
La última versión estable es la v0.2.0, compatible tanto con Python 2.x como Python 3.x

## 4. Autores
Código desarrollado por [@jmformoso](https://twitter.com/jmformoso) con la colaboración de [@_spalacios](https://twitter.com/_spalacios)

## 5. Copyright y licencia
Este código y su documentación se distribuye bajo licencia Apache 2.0

## 6. Redes sociales

[![Twitter Follow](https://img.shields.io/twitter/follow/jmformoso?style=social)](https://twitter.com/jmformoso)
![GitHub Followers](https://img.shields.io/github/followers/jmformoso?style=social)
[![Twitter Follow](https://img.shields.io/twitter/follow/wikitel?style=social)](https://twitter.com/wikitel)
[![Twitter Follow](https://img.shields.io/twitter/follow/_spalacios?style=social)](https://twitter.com/_spalacios)