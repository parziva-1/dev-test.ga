---
title: Funciones En Python
date: 2021-06-02 20:37:57
tags: Python
categories: [Principiantes]
toc: true
desc: En Python, podemos definir función para hacer nuestro código reutilizable, más legible y organizado. Esta es la sintaxis básica de una función en Python.
---
¡Hola y bienvenidos!. Si estás aprendiendo Python, esta guía es para ti, encontraras una exhaustiva descripción de la sintaxis de Python y montones de código de ejemplos para ayudarte en tu aprendizaje.

Esta guía es una adaptación y traducción de un artículo original de [Estefania Cassingena Navone](https://twitter.com/EstefaniaCassN) que lo puedes encontrar en [FreeCodeCamp.org](https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/).

>💡***Anotación:*** A lo largo de esta guía, voy a usar `<>` para indicar que esta parte de la sintaxis será remplazada por el elemento descrito por el texto dentro de ella. Un ejemplo de ello seria <variable> y para temas prácticos voy a usar un diminutivo <var> esto quiere decir que será remplazado por el nombre de una variable cuando escribamos el código.

En Python, podemos definir función para hacer nuestro código reutilizable, más legible y organizado. Esta es la sintaxis básica de una función en Python.

``` python
def <nombre_de_la_funcion>(<parametro1>, <parametro2>, ...):
    <code>
```

>💡***Anotación:*** Una función Puede tener cero, uno o múltiples parámetros.

## Funciones sin parámetros

Una función sin parámetros, tiene un par vacío de paréntesis después del nombre de la función. Por ejemplo:

``` python
def mostrar_patron():
    talla = 4
    for i in range(talla):
        print("*" * talla)
```

La salida de esta función cuando la llamemos va a ser:

``` python
>>> mostrar_patron()
****
****
****
****
```
>💡***Anotación:*** Tienes que escribir un par de paréntesis vacíos después del nombre de la variable a llamar.

## Funciones con un parámetro

Una función con uno o más parámetros tiene una lista de parámetros dentro de los paréntesis después del nombre de la variable.

``` python
def bienvenido_estudiante(nombre):
    print(f"¡Hola, {nombre}! Bienvenido a clase.")
```

Cuando llamemos a la función, solo tendremos que pasar un valor como argumento, este valor será remplazado donde usemos el parámetro en la función:

``` python
>>> bienvenido_estudiante("Jaime")
¡Hola, Jaime! Bienvenido a clase.
```

Veamos otro ejemplo, una función que nos muestre por pantalla un patrón realizado con asteriscos. Tienes que especificar cuantas filas quieres mostrar.

``` python
def mostrar_patron(num_filas):
    for i in range(num_filas):
        for num_cols in range(num_filas-i):
            print("*", end="")
        print()
```

Mira la diferencia de la salida desde pendiendo del número de filas que le indicamos `num_filas`:

``` python
>>> mostrar_patron(3)
***
**
*

>>> mostrar_patron(5)
*****
****
***
**
*

>>> print_pattern(8)
********
*******
******
*****
****
***
**
*
```

## Funciones con dos o más parámetros

Para definir dos o más parámetros, solo tenemos que separarlos con una coma:

``` python
def suma(a, b):
    print(a + b)
```

Ahora cuando llamamos una función necesitamos pasar dos argumentos:

``` python
>>> suma(4, 5)
9

>>> suma(8, 9)
17

>>> suma(0, 0)
0

>>> suma(3, 5)
8
```

Podemos adaptar la función para que muestre un número definido de filas y un carácter personalizado, usando otro parámetro:

``` python
def mostrar_patron(num_filas, carac):
    for i in range(num_filas):
        for num_cols in range(num_filas-i):
            print(carac, end="")
        print()
```

Puedes ver la salida con el carácter personalizado, algo que le especificamos en el segundo parámetro:

``` python
>>> mostrar_patron(5, "A")
AAAAA
AAAA
AAA
AA
A

>>> mostrar_patron(8, "%")
%%%%%%%%
%%%%%%%
%%%%%%
%%%%%
%%%%
%%%
%%
%

>>> mostrar_patron(10, "#")
##########
#########
########
#######
######
#####
####
###
##
#
```

## Como retornar un valor en un función

Ya sabes como definir una función, ahora vamos a trabajar con las declaraciones de devolución.

A menudo vamos a necesitar devolver un valor desde una función. Podemos hacerlo usando el estamento `return`, solo necesitamos escribir esto en la definición de la función:

``` python
return <valor_a_retornar>
```

>💡***Anotación:*** La función para inmediatamente cuando el estamento `return` es encontrado y el valor es devuelto.

Algunos ejemplos:

``` python
def area_regtangulo(largo, ancho):
    return largo * ancho
```

Ahora llamemos a la función y asignémosle el resultado a una variable:

``` python
>>> area = area_regtangulo(4, 5)
>>> area
20
```

También podemos usar el estamento `return` con un condicional para devolver un valor basado en sí es `True` o `False`.

En este ejemplo, la función retorna el primer número par encontrado en la secuencia:

``` python
def obtener_primer_par(seq):
    for num in seq:
        if num % 2 == 0: 
            return num
        else: 
            return None
```

Llamemos la función para ver el resultado:

``` python
>>> valor1 = obtener_primer_par([2, 3, 4, 5])
>>> valor1
2
```

``` python
>>> valor2 = obtener_primer_par([3, 5, 7, 9])
>>> valor2
None
```

>💡***Anotación:*** Si una función no tiene un estamento `return` o no se encuentra en su ejecución, esta retornara un valor por defecto que es `None`.

La [Guía de Estilo Para Código de Python](https://www.python.org/dev/peps/pep-0008/#programming-recommendations) recomienda usar un estamento `return` coherentemente. Menciona que deberíamos:

>Sea coherente en las declaraciones de devolución. O todas las declaraciones de retorno de una función deben devolver una expresión, o ninguna de ella debe hacerlo. Si alguna declaración de devolución devuelve una expresión, cualquier declaración de devolución en la que no se devuelva ningún valor debe indicarlo explícitamente como retorno `None`, y una declaración de devolución explícita debe de estar presente al final de la función (si es accesible).

## Argumentos predeterminados

Podemos asignar valores predeterminados a los argumentos para los parámetros de nuestra función. Para hacer esto, necesitamos escribir `<parametro>=<valor>` en la lista de parámetros.

>💡***Anotación:*** La [Guía de Estilo Para Código de Python](https://www.python.org/dev/peps/pep-0008/#other-recommendations) menciona que no deberíamos "usar espacios entre el signo de asignación `=` y el valor cuando lo usamos para asignar un valor a un argumento."

En este ejemplo, asignaremos un valor predeterminado de 5 al parámetro `b`. Si omitimos este valor cuando llamemos la función, el valor predeterminado será usado.

``` python
def producto(a, b=5):
    return(a * b) 
```

Si llamamos la función sin un argumento:

``` python
>>> producto(4)
20
```

Esto nos confirma que el valor predeterminado que es `5` fue usado en la operación.

Pero también podemos asignar un valor personalizado a `b` pasando un segundo argumento:

``` python
>>> producto(3, 4)
12
```

>💡***Anotación:*** Los parámetros con argumentos predeterminados deben definirse al final de la lista de parámetros, de lo contrario, verá este error: `SyntaxError: non-default argument follows default argument`. 

Otro ejemplo con la función que usamos para mostrar un patrón. Vamos a asignar un valor predeterminado al parámetro `carac` que va a ser `"*"`.

``` python
def mostrar_patron(num_filas, carac="*"):
    for i in range(num_filas):
        for num_cols in range(num_filas-i):
            print(carac, end="")
        print()
```

Ahora cuando llamemos la función con un solo argumento:

``` python
>>> mostrar_patron(5)
*****
****
***
**
*

>>> mostrar_patron(6, "&")
&&&&&&
&&&&&
&&&&
&&&
&&
&
```