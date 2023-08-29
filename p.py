
import pandas as pd
from colorama import Fore, Style

v_total = 0
v_diaria = 0
index = 0
datos_venta= []



while(index==0): #True

    nombre_cliente = input("Ingrese el nombre del cliente: ")
    rut = input("Ingrese rut de cliente: ")
    direccion = input("Ingrese direccion del cliente: ")
    kilos= int(input("Ingrese la totalidad de kilos: "))


    v_total = kilos * 1000
    v_diaria += v_total
    datos_venta.append([nombre_cliente, rut, direccion, kilos, v_total])
    
    
    v_total==0

    seleccion = int(input("¿ Desea agregar una nueva venta ? , Si = 1 - No = 0 : "))
    
    if(seleccion==0):
        index = index+1
       # print(f"El valor de index es {index}")
        print(f"El total de venta del dia es: {v_diaria} ")
        
        for i in datos_venta:
            print(f"El nombre del cliente es : {i[0]}")
            print(f"El rut del ususario es : {i[1]}")
            print(f"La totalidad de kilos a comprar es de : {i[3]}")
            print(f"El  valor total del cliente {i[0]}, es de {i[4]} {Style.RESET_ALL}\n")
            print("--------------------------------------------------")
      
    else:
        
        index = 0




 # Mostrar los datos
    #print (f"El nombre del cliente es : {nombre_cliente}")
    #print(f"El rut del ususario es : {rut}")
    #print(f"La totalidad de kilos a comprar es de : {kilos}")
    # Operatoria tomando el valor del kilo de pan en 1000 pesos 
    #print(f"El  valor total del cliente {nombre_cliente}, es de {v_total}")

    #Generar arreglo 
    
    
    
