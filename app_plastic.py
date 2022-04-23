#app plastic by fler

import os

import time

#------------- VARIABLES ---------------------------

opcion_menu_principal=""

opcion_menu_ventas=""  # puede ser 1,2 o 3 como texto!!!!!!!!

nombre_producto=""

precio_producto=0

cantidad=0

es_mayorista= False  # Por defecto NO es mayorista

total_pagar=0

#--------- variables estadísticas---------

cant_ventas=0  # contador de ventas

monto_total_ventas=0   # acumulador de ventas

cant_ventas_mayoristas=0    #  contador de ventas mayoristas

monto_total_ventas_mayoristas=0 # acumulador ventas mayoristas


forma_pago=""

 

#------------- CÓDIGO PRINCIPAL ---------------------------


while True:

    os.system("cls")

    opcion_menu_principal= str(input('''

    -------------- APP PLASTIC -----------------                          

    1-- Realizar venta

    2.- Ver estadísticas de ventas

    3.- Salir

     

    Elija opcion de menu: '''))

   

    if opcion_menu_principal=="1":

        os.system("cls")

        print("------------ventas------------")

        opcion_menu_ventas= str(input('''

            Producto \t Valor Unitario

            1.- Tazón \t $ 500

            2.- Llavero \t $ 200

            3.- Polera estampada \t $ 3.000

       

            Elija opcion:  '''))

       

        cantidad= int(input("Ingrese cantidad: "))

       

        if opcion_menu_ventas=="1":

            nombre_producto="Tazón"

            if cantidad>=100:

                precio_producto=300

                es_mayorista=True

            else:

                precio_producto=500                

       

        if opcion_menu_ventas=="2":

            nombre_producto="LLavero"

            if cantidad>=300:

                precio_producto=150

                es_mayorista=True

            else:

                precio_producto=200

       

        if opcion_menu_ventas=="3":

            nombre_producto="Polera estampada"

            if cantidad>=50:

                precio_producto=2000

                es_mayorista=True

            else:

                precio_producto=3000


        total_pagar= precio_producto*cantidad

        print(f" TOTAL PAGAR ${total_pagar}")

       

        if es_mayorista:

            print(f'''

            Si cancela en efectivo tiene un 10% descuento,

            es decir, total ${total_pagar*0.9}      ''')

       

        forma_pago= str(input("¿Cancela en efectivo? S/N "))                

        if es_mayorista and forma_pago.upper()=="S":

            total_pagar= total_pagar*0.9


        ####  carga de estadísticas ####

        cant_ventas= cant_ventas+1

        monto_total_ventas= monto_total_ventas+total_pagar

        print(f'''

              -------------- BOLETA -------------

              Producto: {nombre_producto}

              {cantidad} unidades X {precio_producto} c/u

              ${total_pagar}  

        ''')                

        os.system("pause")

       

    if opcion_menu_principal=="2":

        os.system("cls")

        print("------------estadísticas-----------")

        print(f'''

             Cant. ventas realizadas: {cant_ventas}

             Monto total recaudado ${monto_total_ventas}

              ''')

       

        os.system("pause")

       

    if opcion_menu_principal=="3":

        opcion = str(input('''

         ¿Estas seguro de salir?   S/N  ''')).upper()

       

        if opcion=="S":

            print("Saliendo de la app.....")

            time.sleep(1.5)  # delay de 1.5 seg

            break