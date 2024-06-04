import usuarios.usuario as modelo
import notas.acciones


class Acciones:
    def registro(self):
        print("Ingresando al registro.")
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        email = input("Ingresa tu email: ")
        password = input("Ingresa tu contraseña")
        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()
        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")
            
            
    def login(self):
        print("Ingresando al login.")
        try:
            email = input("Ingresa tu email: ")
            password = input("Ingresa tu contraseña")
            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificar()
            
            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print("Intento incorrecto, intentalo mas tarde")
            
        def proximasAcciones(self, usuario):
            print("""
                  Acciones disponibles: 
                  - Crear nota (nota)
                  - Mostrar nota (mostrar)
                  - Eliminar nota (eliminar)
                  -Salir (salir)
            """)
            
            accion = input("Ingresa la accion que deseas realizar: ")
            make = notas.acciones.Acciones()
            if accion == "crear":
                make.crear(usuario)
                self.proximasAcciones(usuario)
            elif accion == "mostrar":
                make.mostrar(usuario)
                self.proximasAcciones(usuario)
            elif accion == "eliminar":
                print("Eliminando nota: ")
                self.proximasAcciones(usuario)
            elif accion == "salir":
                exit()