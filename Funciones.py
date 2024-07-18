import random
import statistics
import csv 
import os 
sueldos_total=0
sueldo_menor=0
sueldo_mayor=0
sueldo_aprox=0
sueldo_total=0
sueldo_promedio=0
sueldos=0

i=1

empleados ={'Juan Perez', 'Maria Garcìa', 'Carlos López', 'Ana Martinez', 'Pedro Rodriguez', 'Laura Hernández', 'Miguel Sánchez', 'Isabel Gómez', 'Francisco Díaz', 'Elena Fernández'}   

def asignar_sueldos_aleatorios():
    for i in len(empleados): 
        sueldo_aprox = {empleado:random.randint(300000, 2500000)
                        for empleado in empleados } 
        sueldo_total=sueldo_total+sueldo_aprox

        if sueldo_mayor < sueldo_aprox:
            sueldo_mayor=sueldo_aprox
        
        elif sueldo_menor > sueldo_aprox:
            sueldo_menor=sueldo_aprox

def busca_sueldo_menor():
    for empleado in empleados:
        if empleados.get('sueldo') < 800000:
            return empleados


def ver_estadistica():
    sueldo_promedio= sueldo_aprox/10

    print("El sueldo mas bajo es",sueldo_menor)
    print("El sueldo mas alto es",sueldo_mayor)
    print("El sueldo promedio es",sueldo_promedio)
    print("La media geometrica es", statistics.geometric_mean(sueldo_aprox))


def lista_sueldo():
    print("Nombre empleado: "+"      "+ "Sueldo")
    for sueldo_aprox in empleados:
        if sueldo_aprox.item()< 800000:
            total_lista=len(sueldo_aprox)
            print(empleados.item())
            print(sueldo_aprox.item())
            print(total_lista)
        elif sueldo_aprox.item() > 800000 and sueldo_aprox.item() < 2000000:
            total_lista=len(sueldo_aprox)
            print(empleados.item())
            print(sueldo_aprox.item())
            print(total_lista)
        elif sueldo_aprox.item() > 2000000:
            total_lista=len(sueldo_aprox)
            print(empleados.item())
            print(sueldo_aprox.item())
            print(total_lista)
        print(sueldo_total)
        
def crea_csv(empleado):
    with open(empleado+'.csv', 'w') as archivo:
	    archivo.write(empleados)



def reporte_sueldos():
    print("Nombre empleado" +"      "+ "Sueldo base"+"      "+   "Descuento salud"+"      "+ "Descuento Salud" +"      "+ "Descuento AFP"+"      "+"Sueldo Liquido" )
    for i in len(empleados):  
        print(empleados, sueldo_aprox.item(), sueldo_aprox.item()*0.07, sueldo_aprox.item()*0.12, sueldo_aprox.item() - (sueldo_aprox.item()*0.07+ sueldo_aprox.item()*0.12))
        
        empleado = {
            "Nombre empleado": empleados,
            "Sueldo base": sueldo_aprox.item(),
            "Descuento Salud": sueldo_aprox.item()*0.07,
            "Descuento AFP":  sueldo_aprox.item()*0.12,
            "Sueldo Liquido": sueldo_aprox.item() - (sueldo_aprox.item()*0.07+ sueldo_aprox.item()*0.12)
        }








        




        






            


def agrega_sueldo_empleado():
                
        Trabajadores = {
            "Nombre Empleado": empleados,
            "Sueldo": sueldo_aprox
            
        }


# Función para generar un informe de todos los guías turísticos
def generar_informe():
    try:
        if os.path.exists("empelados.csv"):
            with open("empelados.csv", 'r', encoding='utf-8') as file:
                empleados = csv.reader(file)
            
            # Guarda todos los datos de los guías en un nuevo archivo CSV
            with open("empelados.csv", 'w', encoding='utf-8') as outfile:
                csv.writer(empleados, outfile)
            print("Informe generado con éxito.")
        else:
            print("No hay datos de guías turísticos disponibles.")
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo 'guias_turisticos.json'.")
    except csv.Error:
        print("Error: El archivo 'guias_turisticos.json' tiene un formato inválido.")

