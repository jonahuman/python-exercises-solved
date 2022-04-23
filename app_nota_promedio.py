import os
from pickle import TRUE
from re import T
import sys
import time
#-.-.-.-.-.-.-VARIABLES-.-.-.-.-.-.-
opcion_menu="" # la opción sera caracter
nota_1= 0
nota_2= 0
nota_3= 0
promedio= 0
estado_alumno="" # puede ser "APROBADO" o "REPROBADO"
cant_alumnos_aprobados= 0
cant_alumnos_reprobados= 0
cant_alumnos_atendidos= 0
salir = False # si se sale de la app
#-.-.-.-.-.-.-.-.-.-.-CÓDIGO PRINCIPAL-.-.-.-.-.-.-.-.-.-.-
os.system("cls")

while True:
    os.system("cls")
    opcion_menu= str(input('''
    -.-.-.-.-.-.-MENÚ-.-.-.-.-.-.-
    1.- calcular promedio
    2.- ver resultados estadísticas
    3.- salir
    Elija opción....    '''))
    
    if opcion_menu== "1":
        os.system("cls")
        print("-.-.-.-.-.-.- CÁLCULO DE PROMEDIO -.-.-.-.-.-.-")
        nota_1= float(input("ingrese nota 1:    "))
        # OJO! mientras la nota esta fuera de rango vuelve a solicitar datos
        while nota_1<1 or nota_1>7:
            nota_1= float(input("ingrese nota 1:    "))
        
        nota_2= float(input("ingrese nota 2:    "))
        while nota_2<1 or nota_2>7:
            nota_2= float(input("ingrese nota 2:    "))
        
        nota_3= float(input("ingrese nota 3:    "))
        while nota_3<1 or nota_3>7:
            os.system("cls")
            nota_3 = float(input("ingrese nota 3: "))
        promedio= (nota_1+nota_2+nota_3)/3

        cantidad_alumnos_atendidos= cant_alumnos_atendidos+1

        if promedio >= 4:
            estado_alumno= "APROBADO"
            cant_alumnos_aprobados= cant_alumnos_aprobados+1
        else:
            estado_alumno= "REPROBADO"
        
        cant_alumnos_reprobados= cant_alumnos_reprobados+1

        print(f'''
        -.-.-.-.-.-.-.-.-REPORTE-.-.-.-.-.-.-.-.-
        Nota1: {nota_1} \t Nota2: {nota_2} \t Nota3: {nota_3}
        Promedio: {promedio} \t Estado: {estado_alumno} \n\n''')
        os.system('pause')

    if opcion_menu== "2":
        os.system("cls")
        print(f'''
        -.-.-.-.-.-.-.-.- ESTADÍSTICAS -.-.-.-.-.-.-.-.-
        atendidos:  {cant_alumnos_atendidos}
        aprobados:  {cant_alumnos_aprobados}
        reprobados: {cant_alumnos_reprobados} \n\n''')
        os.system("pause")
    
    if opcion_menu== "3":
        break
    
print("Fin de ejecución !!!")
