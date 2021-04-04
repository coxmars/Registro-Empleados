# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 13:28:35 2021

@author: marco
"""

class Registro:
    
    def __init__(self):
        
        self.contactos=[]
        import os
         
    def menu(self):
        
        menu=[
            ['Registro empleados de la empresa'],
            [''],
            ['1- Añadir nuevo empleado al registro'],
            ['2- Acceder a la lista de empleados '],
            ['3- Buscar empleados '],
            ['4- Editar registro de empleados '],
            ['5- Cerrar registro ']
        ]
        print () 
        for x in range(7):
            print (menu[x] [0])
          
        opcion=int(input("Estimado usuario, digite la opción deseada: "))
        if (opcion==1):
            self.anadir()
        elif (opcion==2):
            self.lista()
        elif (opcion==3):
            self.buscar()
        elif (opcion==4):
            self.editar()
        elif (opcion==5):
            print("Saliendo del registro de empleados.......")
            
        self.menu()
        
    def anadir(self):
        print("- - - - - - - - - - -")
        print("Añadir nuevo empleado")
        print("- - - - - - - - - - -")
        seguir="si"
        while (seguir=="si"):
            nombre=str(input("Ingrese su nombre por favor: "))
            telefono=str(input("Digite su número de teléfono: "))
            email=str(input("Introduzca su email: "))
            carrera=str(input("Inserte su puesto en la empresa: "))
            salario=float(input("Ingrese su salario mensual en colones: "))
            if (salario!=0):
                salario_neto=salario*0.09 #Se aplican deducciones 8% CCSS y 1% del Banco Popular
                salario=salario_neto
            self.contactos.append({'nombre':nombre,'teléfono':telefono,'email':email,'carrera':carrera,'salario':salario})
            seguir=str(input("Desea continuar agregando empleados al registro? (si/no): "))
        self.mostrarMenu()
        
    def lista(self):
        print("- - - - - - - - - - - ")
        print("Lista de empleados")
        print("- - - - - - - - - - - ")
        if len(self.contactos)== 0:
            print ("No hay ningun empleado en el registro")
        else:
            for x in range(len(self.contactos)):
                print (self.contactos[x] ['nombre'])
        consulta=str(input("Desea consultar los datos guardados en el archivo .txt (si/no): "))
        if (consulta=="si"):
            self.leerInformacion()
            self.menu()
        else:
            self.menu()
                
    def buscar(self):
        print("- - - - - - - - - - - ")
        print("Motor de busquedas")
        print("- - - - - - - - - - - ")
        nombre=input("Introduzca el nombre del empleado: ")
        if len(self.contactos)== 0:
            print ("No hay ningun empleado con ese nombre en el registro")
        for x in range(len(self.contactos)):
            if nombre==self.contactos[x]['nombre']:
                print ("Datos del empleado buscado")
                print ()
                print ("Nombre: ", self.contactos[x]['nombre'] )
                print ("Teléfono: ",self.contactos[x] ['teléfono'])
                print ("Email: ",self.contactos[x]  ['email'] )
                print ("Puesto: ", self.contactos[x] ['carrera'] )
                print ("Salario neto: ", self.contactos[x] ['salario'] )
                return x 
            
            
    def editar(self):
        print("- - - - - - - - - - - ")
        print("Editar contacto de empleados")
        print("- - - - - - - - - - - ")
        informacion=self.buscar()
        condicion=False
        while condicion == False:
            print ()
            print("Estimado usuario, seleccione lo que desea editar: ")
            print ()
            print("1- Nombre ")
            print("2- Teléfono ")
            print("3- Email ")
            print("4- Puesto ")
            print("5- Salario ")
            print("6- Regresar ")
            
            opcion=int(input("Introduzca la opción deseada: "))
            if (opcion==1):
                nombre=str(input("Introduzca el nuevo nombre: "))
                self.contactos[informacion] ['nombre']=nombre
            elif (opcion==2):
                telefono=str(input("Introduzca el nuevo teléfono: "))
                self.contactos[informacion] ['teléfono']=telefono
            elif (opcion==3):
                email=str(input("Introduzca el nuevo email: "))
                self.contactos[informacion] ['email']=email
            elif (opcion==4):
                carrera=str(input("Introduzca el nuevo puesto: "))
                self.contactos[informacion] ['carrera']=carrera
            elif (opcion==5):
                salario=float(input("Introduzca el nuevo salario: "))
                salario_neto=salario*0.09
                salario=salario-salario_neto
                self.contactos[informacion] ['salario']=salario
            elif (opcion==6):
                self.menu()
                condicion=True
                
                
    def mostrarMenu(self):
        print ()
        menu= [
          ["Menú para guardar datos en archivos .txt"],
          [" "],
          ["1. Crear archivo"],
          ["2. Agregar información"],
          ["3. Salir del sistema "]
        ]
    
        for x in range(5):
            print (menu[x] [0])
          
        opcion=int(input("Estimado usuario, digite la opción deseada: "))
        if (opcion==1):
            self.crearArchivo()
        elif (opcion==2):
            self.agregarInformacion() 
        elif (opcion==3):
            print("Saliendo del sistema de archivos .txt .......")
        self.menu()
        
    def crearArchivo(self):
        file = open("datosempleados.txt", "w")
        file.close()
        decidir=str(input("El archivo esta listo para guardar información, desea continuar (si/no): "))
        if (decidir=="si"):
            self.mostrarMenu()
        else:
            self.menu()

    def agregarInformacion(self):
        nombre=str(input("Ingrese su nombre por favor: "))
        telefono=str(input("Digite su número de teléfono: "))
        email=str(input("Introduzca su email: "))
        carrera=str(input("Inserte su puesto en la empresa: "))
        file = open("datosempleados.txt", "a")
        file.write("Nombre: "+nombre + "\n"+"Teléfono: "+telefono + "\n"+"Email: "+email +"\n"+"Puesto: "+ carrera+"\n"+"---------------------------------"+"\n")
        file.close()
        decidir=str(input("La información fue grabada satisfactoriamente, desea seguir (si/no): "))
        if (decidir=="si"):
            self.mostrarMenu()
        else:
            self.menu()
        
    def leerInformacion(self):
        file = open("datosempleados.txt", "r")
        mensaje=file.read()
        print ()
        print (mensaje)
        file.close()
        decidir=str(input("Ya se mostraron los datos en el archivo .txt, desea ir al menú principal(si/no): "))
        if (decidir=="si"):
            self.menu()
        else:
            self.mostrarMenu()
        
        
registro=Registro()
registro.menu() 
registro.anadir()           
registro.lista()         
registro.buscar()
registro.editar() 