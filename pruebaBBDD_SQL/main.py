from time import sleep
from usuarios import acciones

#Llamar a las ACCIONES o FUNCIONES registro y login:

accionFuncion = acciones.Acciones()

espacio = "//////////////////////////PRUEBA MURCIANO////////////////////////////\n"

accion = int(input("¿Que quieres hacer?: 1-REGISTRO, 2-LOGIN ::  "))

if accion == 1:
    print("OK!! Vamos a registrarte en el sistema... \n")
    sleep(0.5)
    print(espacio)
    accionFuncion.registro()
    
    
elif accion == 2:
    print("Vale! Vamos a la identificación de USUARIO en el sistema. \n")
    sleep(0.5)
    print(espacio)
    accionFuncion.login()