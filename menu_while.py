import os
import time

dibujo_1='''
(\ /)
( . .)
C(")(")'''

while True:
    op = str(input('''
        =======================MENU======================
        1.- ver CONEJO
        2.- OPCION 2
        3.- Salir
        
        Ingrese opción  '''))
    if op == '1':
        print('>>>opcion1<<<')
        print(dibujo_1)
    if op == '2':
        print('>>>opcion2<<<')
    if op == '3':
        print('>>>>salir<<<<')
        break   #-.-.-.-.-.-.-.-IMPORTANTE SIEMPRE PONER BREAK-.-.-.-.-.-.-.-.-
