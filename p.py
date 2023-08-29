
v_total = 0
v_diaria = 0
index = 0


while(index==0):

    nombre_cliente = input("Ingrese el nombre del cliente: ")
    rut = input("Ingrese rut de cliente: ")
    kilos= int(input("Ingrese la totalidad de kilos: "))

        # Mostrar los datos

    print (f"El nombre del cliente es : {nombre_cliente}")
    print(f"El rut del ususario es : {rut}")
    print(f"La totalidad de kilos a comprar es de : {kilos}")


        ## Operatoria tomando el valor del kilo de pan en 1000 pesos 


    v_total = kilos * 1000
    print(f"El  valor total del cliente {nombre_cliente}, es de {v_total}")
    v_diaria = v_diaria + v_total
    v_total==0

    seleccion = int(input("¿ Desea agregar una nueva venta ? , Si = 1 - No = 0 : "))
    
    if(seleccion==0):
        index = index+1
        print(f"El valor de index es {index}")
        print(f"El total de venta del dia es: {v_diaria} ")
    else:
        
        index = 0