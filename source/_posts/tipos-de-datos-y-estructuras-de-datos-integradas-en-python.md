---
title: Tipos de datos y estructuras de datos integradas en Python
date: 2021-05-20 14:40:43
tags: Python
categories: [Principiantes]
toc: true
---
¡Hola y bienvenidos!. Si estás aprendiendo Python, esta guía es para ti, encontraras una exhaustiva descripción de la sintaxis de Python y montones de código de ejemplos para ayudarte en tu aprendizaje.

Esta guía es una adaptación y traducción de un artículo original de [Estefania Cassingena Navone](https://twitter.com/EstefaniaCassN) que lo puedes encontrar en [FreeCodeCamp.org](https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/).

>💡***Anotación:*** A lo largo de esta guía, voy a usar `<>` para indicar que esta parte de la sintaxis será remplazada por el elemento descrito por el texto dentro de ella. Un ejemplo de ello seria `<variable>` y para temas prácticos voy a usar un diminutivo `<var>` esto quiere decir que será remplazado por el nombre de una variable cuando escribamos el código.

Tenemos varios tipos de datos y estructuras de datos con los que podemos usar en nuestros programas. Cada un tiene su aplicación particular. Vamos a verlos en detalle.

## Tipos de datos numéricos en Python: int (Enteros), floats (Números decimales), y complex (Números complejos)

Estos son tipos de datos numéricos que puedes usar en Python:

### Integers (Enteros)

Los `integers` son números sin decimales. Puedes confirmar si un número es un `int` con la función `type()`. Si la salida es `<class 'int'>`, entonces el número es un entero.

Por ejemplo:

``` python
>>> type(1)
<class 'int'>

>>> type(15)
<class 'int'>

>>> type(0)
<class 'int'>

>>> type(-46)
<class 'int'>
```

### Floats (Números decimales)

Puedes detectar los `floats` visualmente por la ubicación del punto decimal. Si usas la función `type()` para confirmar el tipo de dato verás esto en la salida `<class 'float'>`.

Aquí te muestro algunos ejemplos:

``` python 
>>> type(4.5)
<class 'float'>

>>> type(5.8)
<class 'float'>

>>> type(2342423424.3)
<class 'float'>

>>> type(4.0)
<class 'float'>

>>> type(0.0)
<class 'float'>

>>> type(-23.5)
<class 'float'>
```

### Complex (Números complejos)

Los números `complex` tienen una parte real y otra parte imaginaria denotada con `j`. Puedes crear números `complex` en Python con la función `complex()`. El primer argumento es la parte real y el segundo es la parte imaginaria.

Aquí te muestro algunos ejemplos:

``` python
>>> complex(4, 5)
(4+5j)

>>> complex(6, 8)
(6+8j)

>>> complex(3.4, 3.4)
(3.4+3.4j)

>>> complex(0, 0)
0j

>>> complex(5)
(5+0j)

>>> complex(0, 4)
4j
```

## Strings (Cadenas de texto) en Python

Los `strings` son muy útiles en Python. Ellos contienen una secuencia de caracteres y usualmente son usadas para representar texto en el código.

Por ejemplo:

``` python
"Hola, Mundo"
```

``` python
'Hola, Mundo'
```

Podemos usar ambas, comillas simples `''` o comillas dobles `""` para definir un `string`. Ambas son válidas y equivalentes, pero deberías elegir una de las dos y usarla consiente mente en todo el programa.

>💡***Anotación:*** ¡Si! Usas un `string` cuando tu escribes "Hola, Mundo" en el programa.  Cuando tu veas un valor dentro de comillas simples o dobles en python, este sera un `string`.

Los `string` pueden contener cualquier carácter que podamos escribir con nuestro teclado, incluyendo número, símbolos, y cualquier otro símbolo especial.

Por ejemplo:

``` python
'45678'
```

``` python
'my_email@email.com'
```

``` python
'#IlovePython'
```

>💡***Anotación:*** Los espacios en blanco cuentan como caracteres en un `string`.

### Comillas dentro de  strings (Cadenas de texto)

Si definimos un `string` con comillas dobles `""`, entonces podemos usar comillas simples dentro de un `string`.

Por ejemplo:

``` python
"I'm 20 years old"
```

Si definimos un `string` con comillas simples `''`, entonces podemos usar comillas dobles dentro del `string`. 

Por ejemplo:

``` python
'Mi libro favorito es "Ready Player One"'
```

### Indexación de cadenas de texto (String Indexing)

Podemos usar índices para acceder a un carácter de un `string` en Python. Un índice es un número que representa una posición específica en un `string`. Podemos asociar el carácter con la posición.

Este es un diagrama de un `string` `Hola`:

``` python
String: H o l a
Index:  0 1 2 3
```

>💡***Anotación:*** Inicia desde el `0` y va incrementando en `1` por cada carácter a la derecha.

Por ejemplo:

``` python
>>> my_string = "Hello"

>>> my_string[0]
'H'

>>> my_string[1]
'e'

>>> my_string[2]
'l'

>>> my_string[3]
'l'

>>> my_string[4]
'o'
```

Podemos también usar números negativos de índices para acceder a caracteres:

``` python
>>> my_string = "Hello"

>>> my_string[-1]
'o'

>>> my_string[-2]
'l'

>>> my_string[-3]
'l'

>>> my_string[-4]
'e'

>>> my_string[-5]
'H'
```

>💡***Anotación:*** Comúnmente usaremos `-1` para acceder al último carácter de un string

### Rebanamiento de caracteres (String slicing)

Posiblemente necesitemos obtener un carácter o una parte de los caracteres de un string.

Esta es la sintaxis general:

``` python 
<string_variable>[inicio:final:paso]
```

- `inicio` es el índice del primer carácter que incluiremos en el slice. Por defecto es `0`.

- `final` es el índice del último carácter que vamos a incluir en el slice (este carácter no será incluido). Por defecto, es el último carácter del string (si omitimos este valor, el último carácter será incluido).

- `paso` es cuanto vamos a sumar al índice actual para llegar al próximo.

Podemos especificar 2 parámetros para usar el valor por defecto del `paso` es de 1. Este incluirá todos los caracteres dentro `inicio` y `final` (no incluido):

``` python 
<string_variable>[inicio:final]
```

Por ejemplo: 

``` python 
>>> freecodecamp = "freeCodeCamp"

>>> freecodecamp[2:8]
'eeCode'

>>> freecodecamp[0:3]
'fre'

>>> freecodecamp[0:4]
'free'

>>> freecodecamp[4:7]
'Cod'

>>> freecodecamp[4:8]
'Code'

>>> freecodecamp[8:11]
'Cam'

>>> freecodecamp[8:12]
'Camp'

>>> freecodecamp[8:13]
'Camp'
```

>💡***Anotación:*** Nótese que si el valor del parámetro va más allá de un rango válido de índices el slice continuara estando presente. Esta es la forma en que el creador de Python implemento esta característica de string slicing.

Si agregamos un valor a `paso`, vamos a "saltar" del índice uno al siguiente según el valor que demos.

Por ejemplo:

``` python 
>>> freecodecamp = "freeCodeCamp"

>>> freecodecamp[0:9:2]
'feCdC'

>>> freecodecamp[2:10:3]
'eoC'

>>> freecodecamp[1:12:4]
'roa'

>>> freecodecamp[4:8:2]
'Cd'

>>> freecodecamp[3:9:2]
'eoe'

>>> freecodecamp[1:10:5]
'rd'
```

Nosotros podemos también usar un paso negativo para ir de derecha a izquierda:

``` python 
>>> freecodecamp = "freeCodeCamp"

>>> freecodecamp[10:2:-1]
'maCedoCe'

>>> freecodecamp[11:4:-2]
'paeo'

>>> freecodecamp[5:2:-4]
'o'
```

Y podemos omitir un parámetro para usar el valor por defecto. Solo tenemos que incluir el correspondiente signo `:` si omitimos el `inicio`, `final`, o ambos:

``` python 
>>> freecodecamp = "freeCodeCamp"

# Por defecto inicio y paso
>>> freecodecamp[:8]
'freeCode'

# Por defecto final y paso
>>> freecodecamp[4:]
'CodeCamp'

# Por defecto inicio
>>> freecodecamp[:8:2]
'feCd'

# Por defecto final
>>> freecodecamp[4::3]
'Cem'

# Por defecto inicio y final
>>> freecodecamp[::-2]
'paeoer'

# Por defecto inicio y final
>>> freecodecamp[::-1]
'pmaCedoCeerf'
```

>💡***Anotación:*** El último ejemplo es una de las formas más comunes para invertir un string.

### f-Strings

En Python 3.6 y en versiones más recientes, podemos usar un tipo de string llamado f-string que nos ayuda a darle formato a nuestros strings de manera más sencilla.

Para definir un f-string, solo necesitamos añadir una `f` antes de las comillas simples o comillas dobles. Luego con el string, vamos a meter las variables o expresiones en llaves `{}`. Esto se remplazará con el valor en la variable o ejecución cuando ejecutemos el programa.

Por ejemplo:

``` python 
primer_nombre = "Jaime"
lenguaje_favorito = "Python"

print(f"Hola, mi nombre es {primer_nombre}. Y estoy aprendiendo {lenguaje_favorito}.")
```

Salida:

``` python 
Hola, mi nombre es Jaime. y estoy aprendiendo Python.
```

Aquí tenemos un ejemplo donde calculamos el valor de una expresión y remplazamos el valor en el string:

``` python 
valor = 5

print(f"{valor} multiplicado por 2 es: {valor * 2}")
```

Salida:

``` python 
5 multiplicado por 2 es: 10
```

También podemos usar métodos dentro de las llaves y el valor retornado remplazará el original en el string cuando ejecutemos el programa:

``` python 
freecodecamp = "FREECODECAMP"

print(f"{frecodecamp.lower()}")
```

Salida:

``` python 
freecodecamp
```

### Métodos de los strings

Los strings tienen métodos con los cuales realizar funciones comunes implementadas por los desarrolladores de Python, nosotros podemos hacer uso de ellas directamente en nuestros programas. Son un útiles para hacer operaciones comunes.

Estos tienen una sintaxis general para usarlos métodos:

``` python 
<nombre_de_variable_string>.<nombre_del_metodo>(<argumentos>)
```

Por ejemplo:

``` python
>>> freecodecamp = "freeCodeCamp"

>>> freecodecamp.capitalize()
'Freecodecamp'

>>> freecodecamp.count("C")
2

>>> freecodecamp.find("e")
2

>>> freecodecamp.index("p")
11

>>> freecodecamp.isalnum()
True

>>> freecodecamp.isalpha()
True

>>> freecodecamp.isdecimal()
False

>>> freecodecamp.isdigit()
False

>>> freecodecamp.isidentifier()
True

>>> freecodecamp.islower()
False

>>> freecodecamp.isnumeric()
False

>>> freecodecamp.isprintable()
True

>>> freecodecamp.isspace()
False

>>> freecodecamp.istitle()
False

>>> freecodecamp.isupper()
False

>>> freecodecamp.lower()
'freecodecamp'

>>> freecodecamp.lstrip("f")
'reeCodeCamp'

>>> freecodecamp.rstrip("p")
'freeCodeCam'

>>> freecodecamp.replace("e", "a")
'fraaCodaCamp'

>>> freecodecamp.split("C")
['free', 'ode', 'amp']

>>> freecodecamp.swapcase()
'FREEcODEcAMP'

>>> freecodecamp.title()
'Freecodecamp'

>>> freecodecamp.upper()
'FREECODECAMP'
```

Si quieres aprender más sobre los métodos en Python, te recomiendo que leas este [artículo](https://docs.python.org/3/library/stdtypes.html#string-methods) de la documentación de Python.

>💡***Anotación:*** Todos los métodos retornan una copia del string. Los métodos no modifican directamente el string porque los strings son inmutables en Python.

## Valores booleanos en Python

Los valores booleanos son True y False en Python. Deben iniciar con una letra mayúscula para ser reconocidos como un valor booleano.

Por ejemplo:

``` python 
>>> type(True)
<class 'bool'>

>>> type(False)
<class 'bool'>
```

Si los escribimos en minúsculas, nos va a dar un error:

``` python 
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined

>>> type(false)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    type(false)
NameError: name 'false' is not defined
```

## Listas en Python

Ahora que cubrimos los tipos básicos de datos en Python, continuemos con las estructuras de datos incluidas en Python. Comenzando con las listas.

Para definir una lista, usamos corchetes [] con elementos separados por coma `,`.

>💡***Anotación:*** Es recomendable añadir un espacio después de cada coma para hacer el código más legible.

Por ejemplo:

``` python
[1, 2, 3, 4, 5]
```

``` python
["a", "b", "c", "d"]
```

``` python
[3.4, 2.4, 2.6, 3.5]
```

Las listas contienen valores de diferentes tipos de datos, esta es una lista válida en Python:

``` python
[1, "Emily", 3.4]
```

También podemos asignar una lista a una variable:

``` python
mi_lista = [1, 2, 3, 4, 5]
```

``` python
letras = ["a", "b", "c", "d"]
```

### Listas anidadas

Las listas pueden contener valores de cualquier tipo de dato, incluso otras listas. Estas listas son llamadas `nested list` (listas anidadas).

``` python
[[1, 2, 3], [4, 5, 6]]
```

En este ejemplo, `[1, 2, 3]` y `[4, 5, 6]` son listas anidadas.

Otros ejemplos de listas anidadas válidas:

``` python
[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
```

``` python
[1, [2, 3, 4], [5, 6, 7], 3.4]
```

También podemos acceder a la lista anidada usando su correspondiente índice.

``` python
>>> mi_lista = [[1, 2, 3], [4, 5, 6]]

>>> mi_lista[0]
[1, 2, 3]

>>> mi_lista[1]
[4, 5, 6]
```

Las listas anidadas pueden ser usadas para representar, por ejemplo, una estructura de un tablero de juegos 2D donde cada número puede representar un elemento diferente.

``` python
# Tablero de ejemplo donde: 
# 0 = Mosaico vació
# 1 = Moneda
# 2 = Enemigo
# 3 = Objetivo
tablero = [[0, 0, 1],
         [0, 2, 0],
         [1, 0, 3]]
```

### Longitud de la lista (List length)

Podemos usar la función `len()` para obtener la longitud de una lista (el número de elementos que esta contiene).

Por ejemplo:

``` python
>>> mi_lista = [1, 2, 3, 4]

>>> len(mi_lista)
4
```

### Actualizar un valor de una lista

Podemos actualizar un valor en particular con el índice usando esta sintaxis:

``` python
<nombre_de_variable_lista>[<indice>] = <valor>
``` 

Por ejemplo:

``` python
>>> letras = ["a", "b", "c", "d"]

>>> letras[0] = "z"

>>> letras
['z', 'b', 'c', 'd']
```

### Añadiendo valores a una lista

Podemos añadir un nuevo valor al final de una lista con el método `.append()`.

Por ejemplo:

``` python
>>> mi_lista = [1, 2, 3, 4]

>>> mi_lista.append(5)

>>> mi_lista
[1, 2, 3, 4, 5]
```

### Remover valores de una lista

Podemos remover un valor de una lista con el metodo `remove()`.

Por ejemplo:

``` python
>>> mi_lista = [1, 2, 3, 4]

>>> mi_lista.remove(3)

>>> mi_lista
[1, 2, 4]
```

>💡***Anotación:*** Esto solo va a remover el primer valor que sea igual al valor indicado. Por ejemplo, si tratamos de remover el número 3 de una lista que tiene dos números 3, el segundo no va a ser removido:

``` python
>>> mi_lista = [1, 2, 3, 3, 4]

>>> mi_lista.remove(3)

>>> mi_lista
[1, 2, 3, 4]
```

### Indexación de listas

Podemos usar un índice en una lista como un índice de un string, con índices que inician desde 0.

``` python
>>> letras = ["a", "b", "c", "d"]

>>> letras[0]
'a'

>>> letras[1]
'b'

>>> letras[2]
'c'

>>> letras[3]
'd'
```

### Rebanamiento de listas (List slicing)

También podemos Rebanamiento una lista usando la misma sintaxis que usamos con los strings y podemos omitir los parámetros usando los que están por defecto. Ahora, en lugar de añadir caracteres al segmento, añadiremos los elementos de una lista.

``` python
<variable_de_lista>[inicio, fin, paso]
```

Por ejemplo:

``` python
>>> mi_lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

>>> my_list[2:6:2]
['c', 'e']

>>> mi_lista[2:8]
['c', 'd', 'e', 'f', 'g', 'h']

>>> mi_lista[1:10]
['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

>>> mi_lista[4:8:2]
['e', 'g']

>>> mi_lista[::-1]
['i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

>>> mi_lista[::-2]
['i', 'g', 'e', 'c', 'a']

>>> mi_lista[8:1:-1]
['i', 'h', 'g', 'f', 'e', 'd', 'c']
```

### Métodos de las listas

Python también tiene métodos ya implementados para ayudarnos con las operaciones más comunes con las listas. Te mostraré algunos ejemplos usando los métodos más comunes.

``` python
>>> mi_lista = [1, 2, 3, 3, 4]

>>> mi_lista.append(5)
>>> my_list
[1, 2, 3, 3, 4, 5]

>>> mi_lista.extend([6, 7, 8])
>>> my_list
[1, 2, 3, 3, 4, 5, 6, 7, 8]

>>> mi_lista.insert(2, 15)
>>> my_list
[1, 2, 15, 3, 3, 4, 5, 6, 7, 8, 2, 2]

>>> mi_lista.remove(2)
>>> mi_lista
[1, 15, 3, 3, 4, 5, 6, 7, 8, 2, 2]

>>> mi_lista.pop()
2

>>> mi_lista.index(6)
6

>>> mi_lista.count(2)
1

>>> mi_lista.sort()
>>> mi_lista
[1, 2, 3, 3, 4, 5, 6, 7, 8, 15]

>>> mi_lista.reverse()
>>> mi_lista
[15, 8, 7, 6, 5, 4, 3, 3, 2, 1]

>>> mi_lista.clear()
>>> mi_lista
[]
```
## Tuplas en Python

Para definir una tupla en Python, vamos a usar paréntesis `()` y se separan los elementos con una coma `,`. Es recomendado añadir un espacio después de cada coma para hacer el código más legible.

``` python
(1, 2, 3, 4, 5)
```

``` python
("a", "b", "c", "d")
```

``` python
(3.4, 2.4, 2.6, 3.5)
```

Podemos asignar una tupla a una variable:

``` python
mi_tupla = (1, 2, 3, 4, 5)
```

### Indexación de tuplas 

Podemos acceder a cada elemento de una tupla con su correspondiente índice:

``` python
>>> mi_tupla = (1, 2, 3, 4)

>>> mi_tupla[0]
1

>>> mi_tupla[1]
2

>>> mi_tupla[2]
3

>>> mi_tupla[3]
4
```

También podemos usar índices negativos:

``` python
>>> mi_tupla = (1, 2, 3, 4)

>>> mi_tupla[-1]
4

>>> mi_tupla[-2]
3

>>> mi_tupla[-3]
2

>>> mi_tupla[-4]
1
```

### Longitud de una tupla (Tuple length)

Para saber la longitud de una tupla, usamos la función `len()`, pasando la tupla como argumento:

``` python
>>> mi_tupla = (1, 2, 3, 4)

>>> len(mi_tupla)
4
```

### Tuplas anidadas

Las tuplas pueden contener valores de cualquier tipo, incluso listas y otras tuplas. Estas tuplas se llaman tuplas anidadas (nested tuples).

``` python
([1, 2, 3], (4, 5, 6))
```

En el ejemplo anterior, tenemos una tupla anidada (4, 5, 6) y una lista, puedes acceder a estas estructuras de datos anidadas con su correspondiente índice.

Por ejemplo:

``` python
>>> mi_tupla = ([1, 2, 3], (4, 5, 6))

>>> mi_tupla[0]
[1, 2, 3]

>>> mi_tupla[1]
(4, 5, 6)
```

### Rebanamiento de tuplas (Tuple slicing)

También podemos rebanar una tupla como las listas y strings. El mismo principio y reglas que antes.

Esta es la sintaxis general:

``` python
<nombre_de_variable_tupla>[inicio, fin, paso]
```

Por ejemplo:

``` python
>>> mi_tupla = (4, 5, 6, 7, 8, 9, 10)

>>> mi_tupla[3:8]
(7, 8, 9, 10)

>>> mi_tupla[2:9:2]
(6, 8, 10)

>>> mi_tupla[:8]
(4, 5, 6, 7, 8, 9, 10)

>>> mi_tupla[:6]
(4, 5, 6, 7, 8, 9)

>>> mi_tupla[:4]
(4, 5, 6, 7)

>>> mi_tupla[3:]
(7, 8, 9, 10)

>>> mi_tupla[2:5:2]
(6, 8)

>>> mi_tupla[::2]
(4, 6, 8, 10)

>>> mi_tupla[::-1]
(10, 9, 8, 7, 6, 5, 4)

>>> mi_tupla[4:1:-1]
(8, 7, 6)
```

### Métodos de las tuplas (Tuple methods)

Estos son dos métodos que están por defecto en Python para trabajar con tuplas:

``` python
>>> mi_tupla = (4, 4, 5, 6, 6, 7, 8, 9, 10)

>>> mi_tupla.count(6)
2

>>> mi_tupla.index(7)
5
```

>💡***Anotación:*** Las tuplas son inmutables. Ellas no pueden ser modificadas, así que no podemos añadir, actualizar, o remover elementos de una tupla. Si necesitamos hacerlo, tendemos que crear una copia de una tupla.

## Asignación de tupla (Tuple assignment)

En Python, Tenemos una característica muy útil llamada Asignación de tupla. Con este tipo de asignación, podemos asignar valores a múltiples variables en la misma línea.

Los valores son asignados a la correspondiente variable en orden que aparecen. Por ejemplo, en la asignación `a, b = 1, 2` el valor `1` es asiganado a la variable `a` y el valor `2` es asignado a la variable `b`.

Por ejemplo:

``` python
# Asignación de tupla   
>>> a, b = 1, 2

>>> a
1

>>> b
2
```

>💡***Anotación:*** La asignación de tupla es comúnmente usada para cambiar valores de dos variables:

``` python
>>> a = 1

>>> b = 2

# Cambio de valores
>>> a, b = b, a

>>> a
2

>>> b
1
```

## Diccionarios en Python (Dictionaries in Python) 

Ahora vamos a iniciar con los diccionarios. Esta estructura incorporada nos permite crear pares de valores donde un valor es asociado con otro.

Para definir un diccionario en Python,  usaremos los corchetes `{}` con su respectivo par clave-valor separados por una coma.

La llave es separada del valor con `:`.

``` python
{"a": 1, "b": 2, "c"; 3}
```

Tu puedes asignar el diccionario a una variable:

``` python
mi_dicc = {"a": 1, "b": 2, "c"; 3}
```

Las claves de un diccionario deben ser de un tipo de dato inmutable. Por ejemplo, pueden ser strings, números, o tuplas, pero no listas, ya que son mutables.

- Strings: {"Ciudad 1": 456, "Ciudad 2": 577, "Ciudad 3": 678}
- Numeros: {1: "Move Left", 2: "Move Right", 3: "Move Up", 4: "Move Down"}
- Tuplas: {(0, 0): "Inicio", (2, 4): "Meta"}

Los valores de un diccionario pueden ser cualquier tipo de dato, as que podemos asignar strings, números, listas, tuplas, sets, e incluso otros diccionarios como valores. Aquí te dejo algunos ejemplos:

``` python
{"producto_id": 4556, "ingredientes": ["tomate", "queso", "hongos"], "precio": 10.67}
```

``` python
{"id": 567, "nombre": "Emily", "grados": {"Matemáticas": 80, "Biología": 74, "Ingles": 97}}
```

### Longitud de un Diccionario (Dictionary length)

Para obtener el número de pares claves-valor, usamos la función len():

``` python
>>> mi_dicc = {"a": 1, "b": 2, "c": 3, "d": 4}

>>> len(mi_dicc)
4
```

### Obtener el valor en un diccionario

Para obtener el valor en un diccionario, usamos la clave con esta sintaxis:

``` python
<nombre_de_variable_diccionario>[<clave>]
```

Esta expresión será remplazada con el valor correspondiente a esa clave.

Por ejemplo:

``` python
mi_dicc = {"a": 1, "b": 2, "c": 3, "d": 4}

print(mi_dicc["a"])
```

La salida es el valor asociado a `"a"`:

``` python
1
```

### Actualizando un valor en un diccionario

Para actualizar un valor asociado con una clave existente, usaremos la misma sintaxis, pero ahora añadiremos un operador de asignación y el valor:

``` python
<nombre_de_variable_diccionario>[<clave>] = <valor>
```

Por ejemplo:

``` python
>>> mi_dicc = {"a": 1, "b": 2, "c": 3, "d": 4}

>>> mi_dicc["b"] = 6
```

Ahora el diccionario es:

``` python
{'a': 1, 'b': 6, 'c': 3, 'd': 4}
```

### Añadir un par clave-valor a un diccionario

Las claves de un diccionario tienen que ser únicas. Para añadir un nuevo par clave-valor usamos la misma sintaxis que usamos para actualizar el valor, pero ahora la clave tiene que ser nueva.

``` python
<nombre_de_variable_diccionario>[<nueva_clave>] = <valor>
```

Por ejemplo:

``` python
>>> mi_dicc = {"a": 1, "b": 2, "c": 3, "d": 4}

>>> mi_dicc["e"] = 5
```

Ahora el diccionario tiene un nuevo par clave-valor:

``` python
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

### Eliminar un par clave-valor en un diccionario

Para eliminar un par clave-valor, usamos la declaración `del`.

Por ejemplo:

``` python
>>> mi_dicc = {"a": 1, "b": 2, "c": 3, "d": 4}

>>> del mi_dicc["c"]
```

Ahora el diccionario es:

``` python
{'a': 1, 'b': 2, 'd': 4}
```

### Métodos de los diccionarios

Estos son algunos de los métodos más comúnmente usados de los diccionarios:

``` python
>>> mi_dicc = {"a": 1, "b": 2, "c": 3, "d": 4}

>>> mi_dicc.get("c")
3

>>> mi_dicc.items()
dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

>>> mi_dicc.keys()
dict_keys(['a', 'b', 'c', 'd'])

>>> mi_dicc.pop("d")
4

>>> mi_dicc.popitem()
('c', 3)

>>> mi_dicc.setdefault("a", 15)
1

>>> mi_dicc
{'a': 1, 'b': 2}

>>> mi_dicc.setdefault("f", 25)
25

>>> mi_dicc
{'a': 1, 'b': 2, 'f': 25}

>>> mi_dicc.update({"c": 3, "d": 4, "e": 5})

>>> mi_dicc.values()
dict_values([1, 2, 25, 3, 4, 5])

>>> mi_dicc.clear()

>>> mi_dicc
{}
```

Para aprender más sobre los métodos de los diccionarios, les recomiendo leer este [artículo](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) de la documentación de Python.

Este es un artículo al cual regresar constante mente mientras interiorizas estos nuevos conceptos, añádelo a tus marcadores, te invito a que abras tu editor de código favorito y practiques, no te olvides de comentar y compartir, nos vemos en otro artículo.