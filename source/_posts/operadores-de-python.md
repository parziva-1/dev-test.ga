---
title: Operadores de python
date: 2021-05-17 20:05:50
tags: Python
categories: [Principiantes]
toc: true
desc: ¡Hola y bienvenidos!. Si estás aprendiendo Python, esta guía es para ti, encontraras una exhaustiva descripción de la sintaxis de Python y montones de código de ejemplos para ayudarte en tu aprendizaje.
---
¡Hola y bienvenidos!. Si estás aprendiendo Python, esta guía es para ti, encontraras una exhaustiva descripción de la sintaxis de Python y montones de código de ejemplos para ayudarte en tu aprendizaje.

Esta guía es una adaptación y traducción de un artículo original de [Estefania Cassingena Navone](https://twitter.com/EstefaniaCassN) que lo puedes encontrar en [FreeCodeCamp.org](https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/).

>💡***Anotación:*** a lo largo de esta guiá, voy a usar `<>` para indicar que esta parte de la sintaxis sera remplazada por el elemento descrito por el texto dentro de ella. Un ejemplo de ello seria `<variable>` y para temas prácticos voy a usar un diminutivo `<var>` esto quiere decir que sera remplazado por el nombre de una variable cuando escribamos el código.


## Operadores aritméticos en Python

Esos operadores son:

### Adicción: `+`


``` python
>>> 5 + 6
11

>>> 0 + 6
6

>>> 3.4 + 5.7
9.1

>>> "Hola" + ", " + "Mundo"
'Hola, Mundo'

>>> True + False
1
```

>💡***Anotación:*** Los dos últimos ejemplos son curiosos, ¿verdad? Estos operadores se comportan diferente según el tipo de dato de los operandos.
>
>Cuando son strings (cadenas de texto), este operador concatena las cadenas de texto y cuando son valores Booleanos, se realiza una operación particular.
>
>En python, `True` es equivalente a `1` y `False` es equivalente a `0`. Por eso el resultado es: `1 + 0 = 1`

### Sustracción: `-`

``` python
>>> 5 - 6
-1

>>> 10 - 3
7

>>> 5 - 6
-1

>>> 4.5 - 5.6 - 2.3
-3.3999999999999995

>>> 4.5 - 7
-2.5

>>> - 7.8 - 6.2
-14.0
```

### Multiplicación: `*`

``` python
>>> 5 * 6
30

>>> 6 * 7
42

>>> 10 * 100
1000

>>> 4 * 0
0

>>> 3.4 *6.8
23.119999999999997

>>> 4 * (-6)
-24

>>> (-6) * (-8)
48

>>> "Hola" * 4
'HolaHolaHolaHola'

>>> "Hola" * 0
''

>>> "Hola" * -1
''
```

>💡***Anotación:*** Tu puedes "Multiplicar" un `str` por un `int` (Numero entero) para repetir la cadena de texto un numero dado de veces.

### Potenciación: `**`

``` python
>>> 6 ** 8
1679616

>>> 5 ** 2
25

>>> 4 ** 0
1

>>> 16 ** (1/2)
4.0

>>> 16 ** (0.5)
4.0

>>> 125 ** (1/3)
4.999999999999999

>>> 4.5 ** 2.3
31.7971929089206

>>> 3 ** (-1)
0.3333333333333333
```

### División: `/`

``` python
>>> 25 / 5
5.0

>>> 3 / 6
0.5

>>> 0 / 5
0.0

>>> 2467 / 4673
0.5279263856195163

>>> 1 / 2
0.5

>>> 4.5 / 3.5
1.2857142857142858

>>> 6 / 7
0.8571428571428571

>>> -3 / -4
0.75

>>> 3 / -4
-0.75

>>> -3 / 4
-0.75
```

>💡***Anotación:*** Este operador devuelve un `float` como resultado, incluso si la parte decimal es `.0`

Si tratas de dividir por cero, te devolverá un error `ZeroDivisionError`:

``` python
>>> 5 / 0
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    5 / 0
ZeroDivisionError: division by zero
```

### División entera: //

Este operador devuelve un `int` si los operandos son `int`. Si son `float`, el resultado será un `float` con `.0` como parte decimal porque trunca la parte decimal.

``` python
>>> 5 // 6
0

>>> 8 // 2
4

>>> -4 // -5
0

>>> -5 // 8
-1

>>> 0 // 5
0

>>> 156773 // 356
440
```

### Modulo: %

``` python
>>> 1 % 5
1

>>> 2 % 5
2

>>> 3 % 5
3

>>> 4 % 5
4

>>> 5 % 5
0

>>> 5 % 8
5

>>> 3 % 1
0

>>> 15 % 3
0

>>> 17 % 8
1

>>> 2568 % 4
0

>>> 245 % 15
5

>>> 0 % 6
0

>>> 3.5 % 2.4
1.1

>>> 6.7 % -7.8
-1.0999999999999996

>>> 2.3 % 7.5
2.3
```

## Operadores de comparación

Estos operadores son:

- Mayor que: `>`
- Mayor que o igual a: `>=`
- Menor que: `<`
- Menor que o igual a: `<`
- Igual que: `==`
- Diferente o no igual: `!=`

Estos operadores de comparación hacen expresiones que evalúan si es `True` o `False`, Algunos ejemplos:

``` python
>>> 5 > 6
False

>>> 10 > 8
True

>>> 8 > 8
False

>>> 8 >= 5
True

>>> 8 >= 8
True

>>> 5 < 6
True

>>> 10 < 8
False

>>> 8 < 8
False

>>> 8 <= 5
False

>>> 8 <= 8
True

>>> 8 <= 10
True

>>> 56 == 56
True

>>> 56 == 78
False

>>> 34 != 59
True

>>> 67 != 67
False
```

También puedes usarlos para comparar `str` cadenas de texto basado en orden del alfabético:

```python
>>> "Hello" > "World"
False
>>> "Hello" >= "World"
False
>>> "Hello" < "World"
True
>>> "Hello" <= "World"
True
>>> "Hello" == "World"
False
>>> "Hello" != "World"
True
```

Típicamente los usamos para comparar los valores de dos o más variables:

``` python
>>> a = 1
>>> b = 2

>>> a < b
True

>>> a <= b
True

>>> a > b
False

>>> a >= b
False

>>> a == b
False

>>> a != b
True
```

>💡***Anotación:*** Nótese que el operador de comparación es `==` mientras que el de asignación es `=`. El efecto es diferente. `==` devuelve `True` o `False` mientras que `=` asigna un valor a un variable.

## Encadenamiento de operadores de comparación

En Python podemos usar algo denominado "comparison operator chaining" en español "Encadenamiento de operadores de comparación" en la que encadenamos los operadores de comparación para hacer más de una comparación de una manera más concisa.

Por ejemplo, esto verifica si `a` es menor que `b` y `b` es menor que `c`

```python
a < b < c
```

Aquí tenemos algunos ejemplos:

``` python
>>> a = 1
>>> b = 2
>>> c = 3

>>> a < b < c
True

>>> a > b > c
False

>>> a <= b <= c
True

>>> a >= b >= c
False

>>> a >= b > c
False

>>> a <= b < c
True
```

## Operadores lógicos

Hay tres operadores lógicos en Python: `and`, `or`, and `not`. Cada uno de estos operadores tiene su propia tabla de verdad y son esenciales para trabajar con condiciones.

El operador  `and`:

``` python
>>> True and True
True

>>> True and False
False

>>> False and True
False

>>> False and False
False
```

El operador `or`:

``` python
>>> True or True
True

>>> True or False
True

>>> False or True
True

>>> False or False
False
```

El operador `not`:

``` python
>>> not True
False

>>> not False
True
```

Estos operadores son usados para formar expresiones más complejas que combinan diferentes operadores y variables.

Por ejemplo:

``` python
>>> a = 6
>>> b = 3

>>> a < 6 or b > 2
True

>>> a >= 3 and b >= 1
True

>>> (a + b) == 9 and b > 1
True

>>> ((a % 3) < 2) and ((a + b) == 3)
False
```

## Operadores de asignación

Los operadores de asignación son usados para asignar un valor a una variable.

Estos son: `=`, `+=`, `-=`, `*=`, `%=`, `/=`, `//=`, `**=`

- El operador `=` asigna el valor a la variable.
- Los otros operadores realizan una operación con el valor actual de la variable y el nuevo valor y asigna el resultado de la operación a la misma variable.

Por ejemplo:

``` python
>>> x = 3
>>> x
3

>>> x += 15
>>> x
18

>>> x -= 2
>>> x
16

>>> x *= 2
>>> x
32

>>> x %= 5
>>> x
2

>>> x /= 1
>>> x
2.0

>>> x //= 2
>>> x
1.0

>>> x **= 5
>>> x
1.0
```

>💡***Anotación:*** estos operadores realizan operaciones bit a bit antes de asignar el resultado a la variable: `&=`, `|=`, `^=`, `>>=`, `<<=`.

## Operadores de membresía

Puedes comprobar si un elemento es una lista secuencia o no con los operadores: `in` y `not in`. El resultado será `True` o `False`.

Por ejemplo:

``` python
>>> 5 in [1, 2, 3, 4, 5]
True

>>> 8 in [1, 2, 3, 4, 5]
False

>>> 5 in (1, 2, 3, 4, 5)
True

>>> 8 in (1, 2, 3, 4, 5)
False

>>> "a" in {"a": 1, "b": 2}
True

>>> "c" in {"a": 1, "b": 2}
False

>>> "h" in "Hello"
False

>>> "H" in "Hello"
True

>>> 5 not in [1, 2, 3, 4, 5]
False

>>> 8 not in (1, 2, 3, 4, 5)
True

>>> "a" not in {"a": 1, "b": 2}
False

>>> "c" not in {"a": 1, "b": 2}
True

>>> "h" not in "Hello"
True

>>> "H" not in "Hello"
False
```

Típicamente los usamos con variables que almacenan secuencias, como en este ejemplo:

``` python
>>> mensaje = "Hola, Mundo!"

>>> "o" in mensaje
True
```

Este es un artículo al cual regresar constante mente mientras interiorizas estos nuevos conceptos, añádelo a tus marcadores, te invito a que abras tu editor de código favorito y practiques, no te olvides de comentar y compartir, nos vemos en otro artículo.