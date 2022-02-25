from datetime import datetime
from dateutil.relativedelta import relativedelta
import psycopg2
import random

try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "contraseña",
        dbname = "parcial1"
    )
    print("¡Conexión Exitosa!\n") 
except psycopg2.Error as e:
    print("Ocurrir un error en la conexión\n")
    print("Vefifique los parametros")

def primerproblema():
    prueba = False
    cursor = conexion.cursor()
    while(not prueba):
        try:
            n1 = int(input("Ingrese el día: "))
            n2 = int(input("Ingrese su mes: "))
            n3 = int(input("Ingrese el año: "))
            edad = relativedelta(datetime.now(), datetime(n3, n2, n1))
        except ValueError:
            print("Debes ingresar los valores correctos")
        if(edad.months == n2 and edad.days == n1):
            print(f"Hoy es su cumpleaños y cumple {edad.years}")
            cursor.execute("insert into datos(dia, mes, año, edad) values(%s,%s,%s,%s);",(n1,n2,n3,edad.years))
            conexion.commit()            
        elif(edad.months < n2):
            print(f"Esta persona cumple {edad.years} este año y no ha cumplido años aún.")
            cursor.execute("insert into datos(dia, mes, año, edad) values(%s,%s,%s,%s);",(n1,n2,n3,edad.years))
            conexion.commit()
        elif( edad.months > n2):
            print(f"Esta persona cumple {edad.years} este año y ya los cumplio.")
            cursor.execute("insert into datos(dia, mes, año, edad) values(%s,%s,%s,%s);",(n1,n2,n3,edad.years))
            conexion.commit()
###########################################################################################################################################################
def segundoproblema():
    prueba1 = False
    cursor = conexion.cursor()
    while(not prueba1):
        try:
            an1 = int(input("Ingrese el primer ángulo: "))
            an2 = int(input("Ingrese el segundo ángulo: "))
            z = 180-an1-an2
        except ValueError:
            print("Debes ingresar un ángulo")
        print("El tercer ángulo es: ",z)
        cursor.execute("insert into datos2(angulo1, angulo2, angulo3) values(%s,%s,%s);",(an1,an2,z))
        conexion.commit()
        break 
###########################################################################################################################################################
def tercerproblema():
    cursor = conexion.cursor()
    try:
        num = int(input("Ingrese un número entre 1 y 999:\n"))
    except ValueError:
        print("Ingrese un número")
    cen = (num -(num%100))/100
    res = num%100
    dec = (res-(res%10))/10
    uni = res%10
    print("Centena: ",int(cen),"Decena: ",int(dec),"Unidad: ",int(uni))
    cursor.execute("insert into datos3(unidades, decenas, centenas, numero) values(%s,%s,%s,%s);",(int(uni),int(dec),int(cen),num))
    conexion.commit()    
###########################################################################################################################################################
def cuartoproblema():
    cursor = conexion.cursor()
    sali = False
    while not sali:
        print("1 para tirar los datos. \n2 para salir")
        opc = int(input(""))
        if (opc == 1):
            while True:
                    d1 = random.randint(1,6)
                    d2 = random.randint(1,6)
                    print("El dado uno tiene: ",d1)
                    print("El dado dos tiene: ",d2)
                    try:
                        if d1 + d2 == 8:
                            print("Usted ha ganado")
                            a = "Gano"
                            cursor.execute("insert into datos4(dado1, dado2, resultado) values(%s,%s,%s);",(d1,d2,a))
                            conexion.commit()    
                            break
                        elif d1 + d2 == 7:
                            print("Usted ha perdido")
                            a = "Perdio"
                            cursor.execute("insert into datos4(dado1, dado2, resultado) values(%s,%s,%s);",(d1,d2,a))
                            conexion.commit()    
                            break
                        else:
                            print("Sigue lanzando")
                    except:
                        break
        else:
            break 
###########################################################################################################################################################
def Menu1():#Solicitando valores para menú principal
    correcto = False
    num = 0
    while(not correcto):
        try:
            correcto = True
            num = int(input("Ingrese una opción: "))
        except ValueError:
            print("Seleccione una opción valida")
    return num 
###########################################################################################################################################################
salir = False
while not salir:#Selección de opción del menu principal
    print("\n1. Primer Problema \n2. Segundo Problema")
    print("3. Tercer Problema \n4. Dados" )
    print("5. para salir")
    opcion = Menu1()
    if opcion == 1:
        primerproblema()
        break 
    elif opcion == 2:
        segundoproblema()
    elif opcion == 3:
        tercerproblema()
    elif opcion == 4:
        cuartoproblema()
    elif opcion == 5:
        salir = True
    else:
        print("\nIngrese una opción valida")
