from timeit import repeat
import usuarios.usuario as modelo
from notas import acciones as accionesNOTAS

class Acciones:
    def registro(self):
        nombre=input("¿Como te llamas?: ")
        apellidos=input("¿Cuales son tus apellidos?: ")
        email=input("Introduce un EMAIL: ")
        password=input("Introduce un PASSWORD: ")
        
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        if registro[0] >= 1:
            print("\n")
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
            print("\n")
        else:
            print("\n")
            print("No te has registrado bien, porque el EMAIL ya fue REGISTRADO.")
            print("\n")
            
    def login(self):
        
              
        try:
            email=input("Introduce tu EMAIL: ")
            password=input("Introduce tu PASSWORD: ")
            
            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()
            
            nombreUser=login[1]
            apellidosUser=login[2]
            emailUser = login[3]
            passwordUser = login[4]
            fechaRegistroAltaBBDD = login[5]
            
            if email == login[3]:
                print(f"Bienvendio {nombreUser} {apellidosUser}, \n (-ALTA en BBDD día: {fechaRegistroAltaBBDD})")
                self.proximasAcciones(login)
                
        except Exception as e: 
            print(type(e))
            print(type(e).__name__)
            print("Error en el login.")
            
    def proximasAcciones(self, usuario):
        
        accionesNotas = accionesNOTAS.Acciones()
        
        nombreUser=usuario[1]
        apellidosUser=usuario[2]
        emailUser = usuario[3]
        passwordUser = usuario[4]
        fechaRegistroAltaBBDD = usuario[5]
        
        try:
            seleccion=int(input("Acciones Disponibles: 1-Crear Nota || 2-Mostrar tus Notas || 3-Eliminar Nota || 4-Salir ::  "))
        except:
            print("Solo vale INTRODUCIR números ENTEROS.")
            self.proximasAcciones(usuario)

        
        if seleccion == 1:
            accionesNotas.crear(usuario)
            self.proximasAcciones(usuario)
        elif seleccion == 2:
            accionesNotas.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif seleccion == 3:
            accionesNotas.borrar(usuario)
            self.proximasAcciones(usuario)
        elif seleccion == 4:
            print(f"Hasta pronto {nombreUser} !!!!")
            exit()
        else:
            self.proximasAcciones(usuario)
            repeat()
        
        return None