from usuarios import acciones

print("""
Acciones disponibles:
    Registro    
    Login
      """)
make = acciones.Acciones()
accion = input("Que quieres hacer?: ")

if accion == "registro":
    make.registro()
    
elif accion == "login":
    make.login()