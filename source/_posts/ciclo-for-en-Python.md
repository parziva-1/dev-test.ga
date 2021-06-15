---
title: Ciclo for en Python
date: 2021-05-24 19:26:19
tags: Python
categories: [Principiantes]
toc: true
desc: Ahora vas a saber como escribir condiciones en Python, vamos a iniciar con los ciclos. El ciclo for es una de esas estructuras de programación que vamos a usar para repetir un bloque de código un número específico de veces.

---
¡Hola y bienvenidos!. Si estás aprendiendo Python, esta guía es para ti, encontraras una exhaustiva descripción de la sintaxis de Python y montones de código de ejemplos para ayudarte en tu aprendizaje.

Esta guía es una adaptación y traducción de un artículo original de [Estefania Cassingena Navone](https://twitter.com/EstefaniaCassN) que lo puedes encontrar en [FreeCodeCamp.org](https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/)

>💡***Anotación:*** A lo largo de esta guía, voy a usar `<>` para indicar que esta parte de la sintaxis será remplazada por el elemento descrito por el texto dentro de ella. Un ejemplo de ello seria <variable> y para temas prácticos voy a usar un diminutivo <var> esto quiere decir que será remplazado por el nombre de una variable cuando escribamos el código.

## Manos a la obra

Ahora vas a saber como escribir condiciones en Python, vamos a iniciar con los ciclos. El ciclo for es una de esas estructuras de programación que vamos a usar para repetir un bloque de código un número específico de veces.

Esta es la sintaxis básica para escribir ciclos en Python:


``` python
for <variable_del_ciclo> in <iterable>:
    <código>
```

El iterable puede ser una lista, una tupla, un diccionario, un string (cadena de texto), un rango,  un archivo, o cualquier otro tipo de dato iterable en Python. Vamos a empezar con `range()`.

### Función `range()` en Python

Esta función retorna una secuencia de números enteros que usamos para determinar cuantas iteraciones (repeticiones) del ciclo hemos completado. El ciclo completa una iteración por entero.

>💡***Anotación:*** Cada entero es asignado por el ciclo a la variable del ciclo uno en uno por iteración.

Esta es la sintaxis general para escribir un ciclo for con la función `range()`:


``` python
for <variable_del_ciclo> in range(<inicio>, <fin>, <paso>):
    <código>
```

Como puedes ver, el rango es una función que tiene tres parámetros:

- `inicio`: es donde comenzara la secuencia de números enteros. Por defecto es `0`.

- `fin`: es donde finalizara la secuencia de números enteros (sin incluir este valor).

- `paso`: el valor que se irá sumando en cada iteración al valor anterior. De forma predeterminada es 1.

Puedes pasar 1, 2, o 3 argumentos a la función `range()`:

- Con 1 argumento que le demos a la función `range()`, el valor es asignado al parámetro `fin` y los demás parámetros quedan con los valores por defecto.

- Con 2 argumentos que le pasemos a la función `range()`, serán asignamos a los parámetros `inicio` y `fin` en ese orden especifico quedando el parámetro `paso` con su valor por defecto.

- Con los 3 argumentos, los valores serán asignados a los argumentos `inicio` ,  `fin` y `paso` en ese orden.

Algunos ejercicios con ***un parámetro***:


``` python
for i in range(5):
    print(i)
```

Salida:

``` python
0
1
2
3
4
```

>💡***Anotación:*** La variable del ciclo es actualizada automáticamente por el ciclo.

``` python
for j in range(15):
    print(j * 2)
```

Salida:

``` python
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
```

En el ejemplo siguiente repetiremos un string tantas veces como lo indique la variable del ciclo:

``` python
for num in range(8):
	print("Hola" * num)
```

Salida:

``` python
Hola
HolaHola
HolaHolaHola
HolaHolaHolaHola
HolaHolaHolaHolaHola
HolaHolaHolaHolaHolaHola
HolaHolaHolaHolaHolaHolaHola
```

También podemos usar el ciclo for con estructuras de datos integradas como las listas:

``` python
mi_lista = ["a", "b", "c", "d"]

for i in range(len(mi_lista)):
	print(mi_lista[i])
```

Salida:

``` python
a
b
c
d
```
>💡***Anotación:*** Cuando uses range(len(<secuencia>)), estás usando números que van desde 0 hasta len(<secuencia>)-1. Esto representa la secuencia de índices válidos.

Algunos ejemplos con ***dos parámetros***:

``` python
for i in range(2, 10):
	print(i)
```

Salida:

``` python
2
3
4
5
6
7
8
9
```

Código:

``` python
for j in range(2, 5):
	print("Python" * j)
```

Salida: 

``` python
PythonPython
PythonPythonPython
PythonPythonPythonPython
```

Código:

``` python
mi_lista = ["a", "b", "c", "d"]

for i in range(2, len(mi_lista)):
	print(mi_lista[i])
```

Salida:

``` python
c
d
```

Código:

``` python
mi_lista = ["a", "b", "c", "d"]

for i in range(2, len(mi_lista)-1):
	mi_lista[i] *= i
```

Ahora la lista es: `['a', 'b', 'cc', 'd']`

Algunos ejemplos con ***tres parámetros***:

``` python
for i in range(3, 16, 2):
	print(i)
```

Salida:

``` python
3
5
7
9
11
13
15
```

Código:

``` python
for j in range(10, 5, -1):
	print(j)
```

Salida:

``` python
10
9
8
7
6
```

Código:

``` python
mi_lista = ["a", "b", "c", "d", "e", "f", "g"]

for i in range(len(mi_lista)-1, 2, -1):
	print(mi_lista[i])
```

Salida:

``` python
g
f
e
d
```

### Como iterar sobre iterables en Python

Podemos iterar directamente sobre iterables como son listas, tuplas, diccionarios, strings, y archivos usando el ciclo for. Podemos obtener cada uno de los elementos una vez por iteraciones. Esto es muy útil para trabajar directamente con ellos.

Veamos algunos ejemplos:

### Iterando sobre strings

Si iteramos sobre un string, estos caracteres se asignaran a la variable del ciclo uno por uno (incluyendo espacios y símbolos).

``` python
mensaje = "Hola, ¡Mundo!"

for carac in mensaje:
	print(carac)

```

Salida:

``` python
H
o
l
a
,
 
¡
M
u
n
d
o
!
```

También podemos iterar sobre copias del  string usando métodos de un string cuando especificamos el iterable en el ciclo for. Esto asignará la copia del string como el iterable que será usando para la iteración, como esto:

``` python
palabra = "Hola"

for carac in palabra.lower(): # Llamamos un método de los strings
	print(carac)

```

Salida:

``` python
h
o
l
a
```

``` python
palabra = "Hola"

for carac in palabra.upper(): # Llamamos un método de los strings
	print(carac)

```

Salida:

``` python
H
O
L
A
```

### Iterando sobre listas y Tuplas

``` python
mi_lista = [2, 3, 4, 5]

for num in mi_lista:
	print(num)
```

Salida:

``` python
2
3
4
5
```

Código:

``` python
mi_lista = (2, 3, 4, 5)

for num in mi_lista:
	if num % 2 == 0:
		print("Par")
	else:
		print("Impar")
```

Salida:

``` python
Par
Impar
Par
Impar
```

### Iterando sobre las llaves, los valores, y los pares clave-valor de los diccionarios

Podemos iterar, sobre las llaves, sobre los valores, y los pares clave-valor de un diccionario llamando métodos de los diccionarios. 

Para iterar sobre las llaves, escribimos:

``` python
for <var> in <variables_de_diccionario>:
    <código>
```

Solo escribimos el nombre de la variable que almacena el diccionario a iterar.

>💡***Anotación:*** Tu puedes escribir `<variable_de_diccionario.keys()>` pero escribir el nombre de la variable directamente es mas conciso y funciona exactamente igual.

Por ejemplo:

``` python
mi_dicc = {"a": 1, "b": 2, "c": 3}

for llave in mi_dicc:
	print(llave)
```

``` python
a
b
c
```

>💡***Anotación:*** Puedes asignar cualquier nombre válido a la variable del ciclo.

Para ***iterar sobre valores***, usamos:

``` python
for <var> in <variable_de_diccionario>.values():
	<código>
```

Por ejemplo:

``` python
mi_dicc = {"a": 1, "b":2, "c": 3}

for valor in mi_dicc.values():
	print(valor)
```

Salida:

``` python
1
2
3
```

Para ***iterar sobre pares clave-valor***, usamos:

``` python
for <var>, <valor> in <variable_de_diccionario>.items():
	<código>
```

>💡***Anotación:*** Definimos dos variables de ciclo porque queremos asignarle la clave y el valor para poder usarlas en el ciclo.

``` python
mi_dicc = {"a": 1, "b":2, "c": 3}

for llave, valor in mi_dicc.items():
	print(llave, valor)
```

Salida:

``` python
a 1
b 2
c 3
```

Si definimos solo una variable del ciclo, esta variable contendrá una tupla con el par de clave-valor:

``` python
mi_dicc = {"a": 1, "b":2, "c": 3}

for par in mi_dicc.items():
	print(par)
```

Salida:

``` python
('a', 1)
('b', 2)
('c', 3)
```

## Breack y Continue en Python

Ahora sabes como iterar sobre secuencias en Python. Ahora veremos como tener control sobre el ciclo usando: `break` y `continue`.

### Declaración Break

La declaración `breack` es usada para parar el ciclo inmediatamente.

Cuando una declaración `breack` es encontrada, el ciclo para y el programa retoma su funcionamiento normal después del ciclo.

En el siguiente ejemplo, vamos a parar el ciclo cuando un elemento par es encontrado.

``` python
mi_lista = [1, 2, 3, 4, 5]

for elem in mi_lista:
	if elem % 2 == 0:
		print("Par: ", elem)
		print("break")
		break
	else: print("Impar: ", elem)
```

Salida: 

``` python
Impar 1
Par: 2
break
```

### Declaración Continue

La declaración `continue` es usada para saldar el resto de la iteración actual.

Cuando se encuentra en la ejecución del ciclo, la iteración actual para y una nueva empieza con los valores actualizados en la variable del ciclo.

En el siguiente ejemplo, saltaremos la iteración actual si el elemento es par y mostraremos el valor si el elemento es impar:

``` python
mi_lista = [1, 2, 3, 4, 5]

for elem in mi_lista:
	if elem % 2 == 0:
		print("continue")
		continue
	print("Impar: ", elem)
```

Salida:

``` python
Impar: 1
continue
Impar: 3
continue
Impar: 5
```

## Función zip() en Python

`zip()` es una sorprendente función incorporada que nos ofrece Python para iterar sobre múltiples secuencias de una vez, obteniendo sus correspondientes elementos en cada iteración.

Por ejemplo:

``` python
mi_lista1 = [1, 2, 3, 4]
mi_lista2 = [5, 6, 7, 8]

for elem1, elem2 in zip(mi_lista2, mi_lista2):
	print(elem1, elem2)
```

Salida:

``` python
1 5
2 6
3 7
4 8
```

## Función enumerate() en Python

Puedes mantener localizado un contador mientras el ciclo se está ejecutando con la función `enumerate()`. Comúnmente usado para iterar sobre una secuencia y obtener el correspondiente índice.

>💡***Anotación:*** Por defecto el contador inicia en `0`.

Por ejemplo:

``` python
mi_lista = [5, 6, 7, 8]

for i, elem in enumerate(mi_lista):
	print(i, elem)
```

Salida:

``` python
0 5
1 6
2 7
3 8
```

``` python
palabra = "Hola"

for i, carac in enumerate(palabra):
	print(i, carac)
```

Salida:

``` python
0 H
1 o
2 l
3 a
```

Si inicias el contador desde `0`, puedes usar el índice y el valor actual en la misma iteración para modificar la secuencia:

``` python
mi_lista = [5, 6, 7, 8]

for indice, num in enumerate(mi_lista):
	mi_lista[indice] = num * 3

mi_lista
```

Salida:

``` python
[15, 18, 21, 24]
```

Puedes iniciar el contador con un número diferente pasando un segundo argumento al la función `enumerate()`:

``` python
palabra = "Hola"

for i, carac in enumerate(palabra, 2):
	print(i, carac)
```

Salida:

``` python
2 H
3 o
4 l
5 a
```

## La cláusula else

Los ciclos también tienen una cláusula `else`. Puedes añadir esta cláusula al ciclo si quieres ejecutar un bloque de código específico cuando el ciclo complete todas sus iteraciones sin encontrar una declaración `break`.

>💡***Anotación:*** Si la declaración `break` es encontrado, la cláusula `else` no se va a ejecutar y si la declaración `break` no es encontrado la cláusula `else` sera ejecutada.

``` python
mi_lista = [1, 2, 3, 4, 5]

for elem in mi_lista:
    if elem > 6:
        print("Encontrado")
        break
else:
    print("No encontrado")
```

Salida:

``` python
No encontrado
```

Sin embargo, si la declaración `break` se ejecuta, la cláusula `else` no se ejecuta. Podemos ver esto en el siguiente ejemplo:

``` python
mi_lista = [1, 2, 3, 4, 5] # Ahora la lista tiene el valor 8

for elem in mi_lista:
    if elem > 6:
        print("Encontrado")
        break
else:
    print("No encontrado")
```

Salida:

``` python
Encontrado
```

Este es un artículo al cual regresar constante mente mientras interiorizas estos nuevos conceptos, añádelo a tus marcadores, te invito a que abras tu editor de código favorito y practiques, no te olvides de comentar y compartir, nos vemos en otro artículo.