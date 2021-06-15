---
title: CRUD en Python Con Archivos Y Listas - Tutorial
tags:
  - Python
  - CRUD
categories:
  - Tutoriales
toc: true
date: 2021-06-13 18:55:46
desc: En informática, CRUD es el acrónimo de
---

## CRUD, ¿Qué es?
"En informática, CRUD es el acrónimo de "Crear, Leer, Actualizar y Borrar" (del original en inglés: Create, Read, Update and Delete), que se usa para referirse a las funciones básicas en bases de datos o la capa de persistencia en un software." [Wikipedia](https://es.wikipedia.org/wiki/CRUD)

>💡***Anotación:*** A lo largo de esta guía, voy a usar `<>` para indicar que esta parte de la sintaxis será remplazada por el elemento descrito por el texto dentro de ella. Un ejemplo de ello seria <variable> y para temas prácticos voy a usar un diminutivo <var> esto quiere decir que será remplazado por el nombre de una variable cuando escribamos el código.

## Antes de iniciar

Voy a asumir que ya tienes un entorno él el cual tienes un editor de texto configurado y Python instalado, en mi caso voy a usar `VS Code` y Python en su versión `3.8.5`. Y aquí vas a encontrar el [código completo](https://github.com/parziva-1/dev-test.ga-tutoriales/blob/main/python/CRUD-en-Python-Con-Archivos-Y-Listas/main.py) que vamos a hacer en este tutorial por si se te facilita de esta manera.

Para este tutorial vamos a usar:

- La función `open()` que nos provee Python.
- [Listas y sus métodos.](https://dev-test.ga/2021/05/20/tipos-de-datos-y-estructuras-de-datos-integradas-en-python/#Listas-en-Python)
- Funciones
- Condiciones
- [Ciclo for](https://dev-test.ga/2021/05/24/ciclo-for-en-Python/)

Si no te sientes preparado te recomiendo, ir a mirar rápidamente en los links que te deje arriba y así tendrás más claro el panorama para entender lo que vamos a hacer.

## Manos a la obra
En este caso hipotético, una tienda quiere tener un inventario de sus productos, para hacerlo fácil, solo se van a contemplar 3 aspectos, el nombre del producto, las existencias, y el valor de este producto, cuando termines el tutorial sería bueno que agregaras un, `id` a cada producto, y afianzaras todo lo aprendido en este tutorial.

En tu editor de código crea una carpeta yo la nombraré: `Python-CRUD-txt`, puedes ponerle el mismo o el que quieras, dentro de ella crea un archivo `main.py`, es el cual va a alojar el código de este tutorial.

Voy a dividir la estructura del tutorial en unas funciones básicas y estas serán:

- Una función para limpiar la consola.
- Una función para crear el menú.
- Una función principal que se encargara de manejar las otras funciones.
- Una función para crear productos.
- Una función para listar todos los productos.
- Una función para modificar un producto.
- Una función para eliminar un producto.
- Una función para buscar un solo producto.

## Funciones

### Limpiar la consola.

Esta función es muy fácil de entender y le va a dar un toque mucho más profesional a nuestro programa en consola, vamos a importar el módulo `os` que viene en Python, nos va a permitir ejecutar comandos en la consola entre otras cosas, te dejo aquí  [link a la documentación](https://docs.python.org/es/3.10/library/os.html) oficial si quieres saber más de este módulo.

``` python
#main.py
import os

def limpiar():
    os.system("clear") # Si estas en Linux o Mac
    os.system("cls") # Si estas en Windows
    # Solo deja el del sistema operativo que estés usando, para no generar mensajes indeseados
```

>💡***Anotación:*** Es posible detectar en que sistema operativo estamos y asi usar un comando u otro, pero para este tutorial decidi dejarlo lo mas entendible y corto posible, si gustas investiga como hacerlo, y te doy una pista: `os.name` o `sys.platform` te pueden ayudar a saberlo.

### El menú

El menú va a ser la parte visual con la que le vamos a permitir al usuario interactuar con nuestro programa, si algo no te gusta te invito a cambiarlo, y compartas tu versión en los comentarios me gustaría verlo.

``` python
#main.py
def menu():
    print("................::::INVENTARIO::::................")
    print("*" * 50)
    print("Selecciona una opción:")
    print("[C]rear producto")
    print("[L]istar todos los productos")
    print("[M]odificar un producto")
    print("[E]liminar un producto")
    print("[B]usacar un producto")
    print("[S]alir")
    print("*" * 50)

```

>💡***Anotación:*** Como puedes ver estoy multiplicando un `str` esta es una cualidad de este tipo de dato si quieres saber mas revisa este [link](https://dev-test.ga/2021/05/17/operadores-de-python/#Multiplicacion).

### La función principal

Esta va a ser la función que nos va a permitir llamar a nuestras funciones una y otra vez, según lo necesitemos y definamos. Adicional a esto vamos a importar el módulo, `time`, para dar un retardo entre operaciones ya verás como lo vamos a usar, es 100% opcional igual que el módulo os, pero le da un toque más profesional, en tus manos esta si usarlo o no.

``` python
#main.py
def main():
    limpiar() # Llamamos la función limpiar para borras y dejar solo lo que queremos en pantalla
    menu() # Llamamos a nuestro menú 

    comando = input(">> ") 
    comando = comando.upper().strip()

    if comando == 'C':
        pass

    elif comando == 'L':
        pass

    elif comando == 'M':
        pass

    elif comando == 'E':
        pass

    elif comando == 'B':
        pass

    elif comando == 'S':
        os._exit(1)

    else:
        print('Comando inválido')
        time.sleep(1)
        main()
```
>💡***Explicación:***
>- Iniciamos llamando a nuestras funciones que acabamos de crear.
>- Definimos una variable `comando` para alojar lo que el usuario decida hacer unamos dos métodos de los `str`, `upper` para asegurarnos de poder evaluar correctamente el comando y `strip` para eliminar los espacios que el usuario pudo digitar por error.
>- Declaramos una cadena de condiciones para poder evaluar la entrada del usuario y redirigirlo a la parte que quiere ir.
>- Y en caso del valor ser errado le informamos al usuario y volvemos a llamar a nuestra función principal. Usamos `os._exit(1)` para interrumpir la ejecución de nuestro programa y sacar al usuario.
>- Por último verás `time.sleep(1)`, es por lo cual importamos el módulo `time` esta función pausa la ejecución de nuestro programa por la cantidad de segundos que le indiquemos como argumento.

Y con esto puedes ver como va quedando nuestro programa actualmente.

``` python
#main.py

import os, time

def limpiar():
    os.system("clear") # Si estas en Linux o Mac
    os.system("cls") # Si estas en Windows
    # Solo deja el del sistema operativo que estés usando, para no generar mensajes indeseados

def menu():
    print("................::::INVENTARIO::::................")
    print("*" * 50)
    print("Selecciona una opción:")
    print("[C]rear producto")
    print("[L]istar todos los productos")
    print("[M]odificar un producto")
    print("[E]liminar un producto")
    print("[B]usacar un producto")
    print("[S]alir")
    print("*" * 50)

def main():
    limpiar() # Llamamos la función limpiar para borras y dejar solo lo que queremos en pantalla
    menu() # Llamamos a nuestro menú 

    comando = input(">> ") 
    comando = comando.upper().strip()

    if comando == 'C':
        pass

    elif comando == 'L':
        pass

    elif comando == 'M':
        pass

    elif comando == 'E':
        pass

    elif comando == 'B':
        pass

    elif comando == 'S':
        os._exit(1)

    else:
        print('Comando inválido')
        time.sleep(1)
        main()
```

Si quieres ejecutarlo llama la función principal al final del archivo y verás algo como esto.

``` python
................::::INVENTARIO::::................
**************************************************
Selecciona una opción:
[C]rear producto
[L]istar todos los productos
[M]odificar un producto
[E]liminar un producto
[B]usacar un producto
[S]alir
**************************************************
>> 
```

Hasta este momento solo realizamos la parte visual y planteamos el comportamiento de nuestro programa, ahora vamos a implementar el `CRUD` para darle poder almacenar y persistir los datos dados por el cliente.

### Crear un producto

En nuestro archivo `main.py` vamos a definir otra función la cual tendrá por nombre crear, y recibirá por parámetros los datos necesarios para la creación del producto, los cuales serán nombre, existencias y valor. Quedando de esta manera.

``` python
def crear(nombre, existencias, valor):
    pass
```

Ahora vamos a implementar la parte para poder leer y escribir en un archivo de texto plano, vamos a hacer uso de la función `open` que su sintaxis es: 

``` python
    <open>(<nombre_del_archivo>.<la_extencion>, <metodo_de_apertura>)  
```
un ejemplo seria

``` python
    open("inventario", "a")
```
Te invito a leer más sobre los modos de apertura en este [link](https://uniwebsidad.com/libros/python/capitulo-9/sobre-el-objeto-file), En mi caso he decidido solo usar el modo `r` y el modo `w`.

``` python
#main.py
def crear(nombre, existencias, valor):
    clear() # Llamamos la función limpiar para borras y dejar solo lo que queremos en pantalla
    lineas=[]
    try:
        f = open("inventario.txt", "r")
        lineas = f.readlines()
        f.close()
    except:
        f = open("inventario.txt", "w")
 
```

>💡***Explicación:***
>- Declaramos una variable tipo lista para alojar toda la información que tenga nuestro archivo.
>- Como ves hago uso de `try` y `except` para manejar los errores que puedan surgir por los modos de apertura que elegí.
>- Con esto le estamos diciendo a Python si el archivo existe ábrelo y dame toda la información en mi lista y cierra el archivo.
>- Si el archivo no existe se va a producir un error y se va a ejecutar lo que este dentro de `except` creando el archivo.
>- El método `readlines` lo que va a hacer es leer cada línea del archivo y sé raparlos en una lista.

Seguimos: 

``` python
#main.py
def crear(nombre, existencias, valor):
    clear() 
    lineas=[]
    try:
        f = open("inventario.txt", "r")
        lineas = f.readlines()
        f.close()
    except:
        f = open("inventario.txt", "w")

    if nombre+"\n" in lineas:
        print("Este producto ya esta en el inventario")
        time.sleep(2)
        main()
    else:
        f = open("inventario.txt", "w")
        lineas.append(nombre)
        lineas.append(existencias)
        lineas.append(valor)
        for linea in lineas:
            f.write(str(linea.strip()+"\n"))
        f.close()
        print("Producto agregado exitosamente.")
        time.sleep(2)
        main()
```

>💡***Explicación:*** 
>- Primero declaramos una condición que verifique si el producto con ese nombre ya existe en nuestra lista, usamos el nombre que nos dan como parámetro, en la lista cada línea al final tiene un salto de línea `\n` necesitamos agregárselo o quitarlo para hacer la comparación yo decidí agregarlo.
>- Si hay alguna conciencia le informamos al usuario y lo mandamos al menú principal.
>- Si no se encuentra ninguna conciencia, seguimos con la ejecución de nuestro programa.
>- Aquí nuestra forma de actuar es simple, como líneas es una lista podemos usar los métodos de las listas para agregar datos.
>- Abrimos el archivo, guardo el enlace en una variable f haciendo referencia a `file` archivo en ingles.
>- Añadimos los datos dados en el orden que queramos, con el método `append` que nos agrega un elemento al final de la lista.
>- Ya tenemos nuestro elemento en la lista, ahora toca pasarlos al archivo.
>- Esto lo hacemos ayudándonos de un ciclo, y usando un método de la función `open` que es `write`.
>- Línea siendo la línea actual tenemos que contemplar que viene con un salto de línea que puede romper nuestro programa así que lo quitamos.
>- Le agregamos a cada uno de las líneas al final un `\n` para dar el salto de línea en el archivo.
>- Mostramos un mensaje y movemos al usuario al menú principal. 

Con esto ya terminamos la función que nos va a permitir crear un nuevo producto en el archivo.

### Listar todos los productos

Hasta el momento ya tenemos una función que nos permite crear un nuevo producto y lo ingresa en el archivo, ahora vamos a ver como podemos mostrar todos y cada uno de los productos en pantalla. Para esto usaremos otra función que la nombraré como `listar` y la cual no recibirá ningún parámetro.

``` python
#main.py
def listar():
    clear()
    print("................::::INVENTARIO::::................")
    print("*" * 50)
    lineas=[]
    try:
        f = open("inventario.txt", "r")
        lineas = f.readlines()
        f.close()
    except:
        f = open("inventario.txt", "w")

    if lineas == []:
        print("No hay productos...")
        time.sleep(2)
        main()
    else:
        for linea in lineas:
            print(linea.strip("\n"))

        while True:
            regresar = input("[R]egresar: ")
            regresar = regresar.upper().strip()
            if regresar == "R":
                main()
```

A partir de aquí verás que se empiezan a repetir algunas partes y debe ser así, porque estamos haciendo consultas que tienen mucho en común.

>💡***Explicación:*** 
>- Usamos el mismo manejo de errores que en la función crear, estoy seguro de que se puede cambiar, te invito a que lo intentes.
>- Hacemos una comparación simple luego de obtener la lista y en caso de estar vacía le informamos al cliente y lo mandamos al inicio.
>- Viene lo interesante de esta parte, con un ciclo `for` y quitando el salto de línea imprimimos la lista en pantalla.
>- Uso un `while` infinito solo para que el usuario decida cuando quiere salir de esa función.

Con esto ya tenemos medio programa, intenta a ejecutarlo y a añadir algunos artículos y verlos con la función que creamos. Antes no te olvides de agregar las funciones a la función principal de esta manera.

``` python
#main.py
def main():
    limpiar() # Llamamos la función limpiar para borras y dejar solo lo que queremos en pantalla
    menu() # Llamamos a nuestro menú 

    comando = input(">> ") 
    comando = comando.upper().strip()

    if comando == 'C':
        nombre = input("Nombre del producto a crear: ")
        existencias = input("Ingresa las existencias del producto: ")
        valor = input("Ingresa el valor del producto: ")
        crear(nombre, existencias, valor)

    elif comando == 'L':
        listar()

    elif comando == 'M':
        pass

    elif comando == 'E':
        pass

    elif comando == 'B':
        pass

    elif comando == 'S':
        os._exit(1)

    else:
        print('Comando inválido')
        time.sleep(1)
        main()
```
Creo que no hace falta decir que hacen los inputs ahí ¿verdad?

### Modificando un producto

Iniciamos la recta final, y si faltan 3 funciones que son las más complejas pero a su vez son muy parecidas así que con una podremos hacer las otras, empecemos.

``` python
#main.py
def modificar(nombre):
    clear()
    lineas=[]
    try:
        f = open("inventario.txt", "r")
        lineas = f.readlines()
        f.close()
    except:
        f = open("inventario.txt", "w")
    if nombre+"\n" not in lineas:
        print("Producto no encontrado")
        time.sleep(2)
        main()
```

Te resulta familiar esta estructura, y debería ser así porque la usamos en las anteriores funciones el principio es el mismo.

``` python
#main.py
def modificar(nombre):
    clear()
    lineas=[]
    try:
        f = open("inventario.txt", "r")
        lineas = f.readlines()
        f.close()
    except:
        f = open("inventario.txt", "w")
    if nombre+"\n" not in lineas:
        print("Producto no encontrado")
        time.sleep(2)
        main()
    else:
        for linea in lineas:
            if linea == nombre+"\n":
                indice = lineas.index(linea)
                
                while True:
                    print(f"[N]ombre: {lineas[indice].strip()}, [E]xistencias: {lineas[indice+1].strip()}, [P]recio: {lineas[indice+2].strip()}, [S]alir al menú principal")
                    comando = input("Que quieres modificar: ")
                    comando = comando.upper().strip()
                    existencias, precio = None, None
                    if comando == "N":
                        nombre = input("Nombre del producto: ")+"\n"
                        lineas[indice] = nombre
                    elif comando == "E":
                        existencias = input("Canditad de existencias del producto: ")+"\n"
                        lineas[indice+1] = existencias
                    elif comando == "P":
                        precio = input("precio del producto: ")+"\n"
                        lineas[indice+2] = precio
                    elif comando == "S":
                        if lineas[indice] == nombre or lineas[indice+1] != existencias or lineas[indice+2] != precio:
                            f = open("inventario.txt", "w")
                            for linea in lineas:
                                f.write(str(linea))
                            f.close()
                            print("Producto modificado exitosamente.")
                            time.sleep(2)
                            main()
                        else:
                            main()
                    else:
                        print("Comando no valido")
```
Y aquí tenemos nuestra función terminada.

>💡***Explicación:*** 
>- Doy por sentado que ya estás familiarizado a este punto con como trabajamos con las listas y vamos a iterar en una lista con un ciclo `for`.
>- Con una condición buscando un valor en específico donde, una vez lo ubicó con el método de las listas `index` obtengo el índice del nombre de mi producto y lo almaceno en una variable, para poder actualizarlo.
>- Una vez es encontrado uso un ciclo while Infinito, con ayuda de un [f-string](https://dev-test.ga/2021/05/20/tipos-de-datos-y-estructuras-de-datos-integradas-en-python/#f-Strings) vamos a mostrar la información en pantalla del producto a modificar.
>- Mostramos un menú para que el usuario pueda indicarnos lo que desea hacer, lo manejamos de la misma manera que hicimos al inicio del programa.
>- Cuando el usuario quiere volver al menú principal surge un problema, y este es ¿modifico algo o no?, yo le di respuesta a esta pregunta de esta manera, declaro dos variables `existencias, precio = None, None` si estás confundido esto se llama [asignación de tupla](https://dev-test.ga/2021/05/20/tipos-de-datos-y-estructuras-de-datos-integradas-en-python/#Asignacion-de-tupla-Tuple-assignment), las inicio sin valor para luego hacer una comparación, no inicio nombre porque ya lo tenemos como parámetro así que no hace falta.
>- La comparación radica en que si algunos de los valores ingresados por el usuario es igual a uno de la lista es porque se realizó una modificación y se procede a hacerlos permanentes.
>- Cabe resaltar que cuando se les pide los valores con la función `input` se le concatena un string que no es más que un salto de línea.

Y de esta manera tendríamos un sistema funcional para editar un producto de nuestro `inventario.txt`

### Eliminando un producto

En esta parte me limitaré a explicar las diferencias con las otras funciones.

``` python
#main.py
def eliminar(nombre):
    clear()
    lineas=[]
    try:
        f = open("inventario.txt", "r")
        lineas = f.readlines()
        f.close()
    except:
        f = open("inventario.txt", "w")
    if nombre+"\n" not in lineas:
        print("Producto no encontrado")
        time.sleep(2)
        main()
    else:
        for linea in lineas:
            if linea == nombre+"\n":
                indice = lineas.index(linea)
                
                while True:
                    print(f"Nombre: {lineas[indice].strip()}, Existencias: {lineas[indice+1].strip()}, Precio: {lineas[indice+2].strip()}")
                    comando = input("Escribe [SI] para eliminar este producto o [NO] para regresar al menú principal: ")
                    comando = comando.upper().strip()

                    if comando == "SI" or comando == "S":
                        lineas.pop(indice+2)
                        lineas.pop(indice+1)
                        lineas.pop(indice)
                        f = open("inventario.txt", "w")
                        for linea in lineas:
                            f.write(str(linea.strip()+"\n"))
                        f.close()
                        print("Producto Eliminado exitosamente.")
                        time.sleep(2)
                        main()
                    elif comando == "No" or comando == "N":
                        main()
                    else:
                        print("Comando no válido")
```

>💡***Explicación:*** 
>- La principal diferencia con el anterior radica en cuando el usuario le da a la opción de querer eliminar el producto
>- Como ya tenemos el índice de ese producto en la lista, lo único que tenemos que hacer es retirarlo, para eso usamos el método `pop` que por parámetro le pasamos el inicio del elemento que queremos retirar.
>- En este caso un producto se compone por 3 elementos que son, su nombre, sus existencias y su valor. Como son 3 vamos a eliminar primero el que tiene un índice mayor luego el del medio y por último el de índice menor.
>- Una vez eliminado de la lista procedemos a hacer permanente los cambios en el archivo. 

Estás entendiendo todo hasta este punto, si no es así por favor dímelo en los comentarios que es lo que se te dificulta para poder ayudarte.

### Buscar un producto

Esta función es algo redundante, porque al tener una que lista todos los productos pasaría a un segundo plano, pero vamos a agregarle algo de valor.

``` python
#main.py 
def buscar(nombre):
    clear()
    lineas=[]
    try:
        f = open("inventario.txt", "r")
        lineas = f.readlines()
        f.close()
    except:
        f = open("inventario.txt", "w")
    if nombre+"\n" not in lineas:
        print("Producto no encontrado")
        time.sleep(2)
        main()
    else:
        for linea in lineas:
            if linea == nombre+"\n":
                indice = lineas.index(linea)
                print(f"Nombre: {lineas[indice].strip()}, Existencias: {lineas[indice+1].strip()}, Precio: {lineas[indice+2].strip()}")
                while True:
                    comando = input("¿Que desea hacer?, [E]liminarlo, [M]odificarlo, [R]eguresar al menú: ")
                    comando = comando.upper().strip()

                    if comando == "E":
                        eliminar(nombre)
                    elif comando == "M":
                        modificar(nombre)
                    elif comando == "R":
                        main()
                    else:
                        print("Comando no válido")

```

>💡***Explicación:*** 
>- La única diferencia con las dos funciones anteriores radica en el menú, desde aquí vamos a llamar a las otras dos funciones según el usuario lo pida.


## Conclusión

Aquí te dejo el código completo en un [repositorio](https://github.com/parziva-1/dev-test.ga-tutoriales/blob/main/python/CRUD-en-Python-Con-Archivos-Y-Listas/main.py) para que lo puedas ver completo 

Espero que este tutorial te haya sido de utilidad para entender el concepto de trabajar con archivos y listas, como leerlos, como modificarlos, como modificar una lista, usar sus métodos en un entorno rea

Claramente este `CRUD` es solo para practicar en un entorno real usaríamos una base de datos y otros para tener la información y no en texto plano, como podría ser un `JSON` o `XML`, Pero todos van con las mismas funciones “Crear, Leer, Actualizar y Borrar”.
Te pareció útil compártelo con tus compañeros, comenta si cambiarias algo, me gustaría leer tu opinión, gracias por llegar hasta aquí, y nos vemos en otros artículos.