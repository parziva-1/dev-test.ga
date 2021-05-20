''' # int

print(type(5))

# float

print(type(5.2))

# complex

print(type(complex(2,-3)))

print("hola \"mundo\" ,soy \b jaime")

lista = []

print(type(lista)) '''

''' semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print(semana[1:4]) '''

''' my_tuple = (1,2,3,4,1,"","","jaime","jaime")

print(my_tuple)
 '''

valorProducto = 50000 # Si ejecutaramos la funcion type(), nos daria un 'int'
iva = 0.19 # Aqui nos diaria que es 'float'

# podriamos declarar otra variable para el valor total del producto con el impuesto
# pero de manera educativa no lo vamos a hacer, vamos a alteral su valor

valorProducto = valorProducto+(valorProducto * iva) 

print(valorProducto)
print(type(valorProducto))