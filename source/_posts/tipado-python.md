---
title: Tipado En python
author: Jaime Linares
date: 2021-05-14 20:49:21
tags: Python
categories: [Principiantes]
desc: En este artículo voy a tratar de explicar el tipado que maneja el lenguaje de programación Python en su versión 3.x, sin más rodeos empiezo.
---

En este artículo voy a tratar de explicar el tipado que maneja el lenguaje de programación Python en su versión 3.x, sin más rodeos empiezo.

Wikipedia nos da esta definición de tipado:

>En ciencias de la computación, un sistema de tipos define cómo un lenguaje de programación clasifica los valores y las expresiones en tipos, cómo se pueden manipular estos tipos y cómo interactúan. [WikiPedia.org](https://es.wikipedia.org/wiki/Sistema_de_tipos).

En un lenguaje menos técnico y para Python seria; tengo una variable `nombre` y le asigno un valor quedando `nombre = "Jaime Linares"` y luego a esa misma variable le puedo asignar otro tipo de dato.


``` python
nombre = "Jaime Linares"
print(type(nombre)) 
```

Cuando ejecute nos va a decir:

``` python
<class 'str'>
```

Pero que pasa si ahora en la misma variable quiero guardar dos nombres y con ello tener una lista.

``` python
# Usamos el codigo anterior
nombre = "Jaime Linares"
print(type(nombre))

# Y ahora lo modificamos para que sea nuestra lista de nombres
nombre = ["Jaime Linares", "Alberto Perlaza"]
print(type(nombre))
```

Cuando ejecutemos nos va a decir:

``` python
<class 'str'>
<class 'list'>
```

¿Qué es lo que acabamos de hacer?, cambiamos el tipo de `'str'` a `'list'` y este es el tipado dinámico de Python, ¿no te queda claro?, otro ejemplo:

```python
# Definimos nuestra variable
valorProducto = 50000 # Si ejecutáramos la función type(), nos daría un 'int'
iva = 0.19

# Podríamos declarar otra variable para el valor total del producto con 
# el impuesto, pero de manera educativa no lo vamos a hacer, vamos a 
# alterar su valor

valorProducto = valorProducto+(valorProducto * iva) 

print(valorProducto)
print(type(valorProducto))
# nuestra variable 'valorProducto' que inicialmente era de un tipo 'int' 
# ahora es del tipo 'float'
```
Espero que con esto quede claro el tipado de datos que maneja Python, como vimos en los dos ejemplos que realizamos, te invito a que abras tu editor de código favorito y practiques, no te olvides de comentar y compartir, nos vemos en otro artículo.