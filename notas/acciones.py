import notas.nota as modelo

class Acciones:
    
    def crear(self, usuario):
        print(f"{usuario[1]}, vamos a crear una nueva nota. ")
        titulo = input("Ingresa el titulo de tu nota: ")
        descripcion = input("Ingresa el contenido de tu nota: ")
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        if guardar[0]>=1:
            print(f"Has guardado la nota: {nota.titulo}")
            
        else:
            print(f"No se guardo la nota, {usuario.nombre}")
            
        def mostrar(self, usuario):
            print(f"{usuario.nombre}, estas son tus notas: ")
            nota = modelo.Nota(usuario[0], "", "")
            notas = nota.litar()
            for nota in notas:
                print("\n-------------------------------")
                print("Titulo: ", nota[2])
                print("Contenido: ", nota[3])
                print("-------------------------------\n")