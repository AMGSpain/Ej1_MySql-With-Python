import notas.notas as objetoNota

class Acciones:
    def crear(self, usuario):
        print("\n")
        print(f"OK {usuario[1]}, Vamos a crear una nueva NOTA.")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Mete el contenido de tu nota: ")
        
        nota = objetoNota.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        
        if guardar[0] >=1:
            print("\n")
            print(f"Perfecto has guardo la nota: {nota.titulo}")
        else:
            print("\n")
            print(f"No se ha guardado la nota, lo siento {usuario[1]}")
            
    
    def mostrar(self, usuario):
        print(f"\n Vale {usuario[1]}, Aqui tienes tus notas: ")
        
        nota = objetoNota.Nota(usuario[0], "", "")
        notas = nota.listar()
        
        for nota in notas:
            print("\n//////////////***************** ->")
            print(nota[2])
            print(nota[3])
        
    def borrar(self, usuario):
        print(f"\nOK {usuario[1]}, Vamos a borrar NOTAS")
        
        titulo = input("Introduce el titulo de la nota a borrar: ")
        
        nota = objetoNota.Nota(usuario[0], titulo, "")
        eliminar = nota.eliminar()
        
        if eliminar[0] >=1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print(f"No se ha borrado lo nota {nota.titulo}")
        
        
    