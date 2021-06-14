Contador_Dias = 0
Dias_Error = 0
Contador_Min = 0
Contador_Max = 0
Contador_Ambos = 0
Media_Max = 0
Media_Min = 0
Porcentaje_Dias_Error  = 0


while True:
    temperatura_Max = int(input("por favor digite la temperatura 1:\n  "))
    temperatura_Min = int(input("por favor digite la temperatura 2:\n  "))
    
    if temperatura_Max == 0 and temperatura_Min == 0:
        print("datos registrados satisfactoriamente.  ")
        break
    
    if temperatura_Max < 5 and temperatura_Min>35:
        Contador_Dias += 1
        temperatura_Max += 1
        temperatura_Min += 1
    else:
        Contador_Ambos+= 1
        if temperatura_Max <5:
            Media_Min += 1
        if temperatura_Min >35:
            Media_Max += 1
        if temperatura_Max <5 and temperatura_Min >35:
            Contador_Ambos+= 1
            
Contador_Ambos= (Media_Min + Media_Max)-1
Contador_Dias  = Contador_Dias + Contador_Ambos
dias_error = (Contador_Ambos* 100)/ Contador_Dias

print(f"estuvieron en el campo {Contador_Dias} dias ")
print(f"dias con temperaturas menores de 5°: {Media_Min}  ")
print(f"dias con temperaturas mayores  35°: {Media_Max}  ")
print(f"dias  con temperatura de 5° y 35° {Contador_Ambos}  ")
print(f"el porcentaje de error fue de  {dias_error}  ")
print(f"los dias totales con error fueron {Contador_Ambos} ")