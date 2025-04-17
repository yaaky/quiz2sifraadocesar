from quiz2sifraadocesar.cifradoCesar import Juego

def mostrar_menu_principal():
    print("\nSISTEMA DE ENCRIPTACION")
    print("1. Encriptar un mensaje")
    print("2. Desencriptar un mensaje")
    print("3. Salir")
    print("")

def iniciar_sistema():
    Clave_usuario = input("Introduce tu identificador de usuario: ")
    Cifrador = Juego(Clave_usuario)
    activo = True
    while activo:
        mostrar_menu_principal()
        seleccion = input("Selecciona una opción: ")
    if seleccion == "1":
        Cifrador.encriptar_mensaje()
    elif seleccion == "2":
        Cifrador.desencriptar_mensaje()
    elif seleccion == "3":
        Cifrador.cerrar_sesion()
        activo = False
    else:
        print("Opción no válida. Intenta de nuevo")

if __name__ == "__main__":
    iniciar_sistema()

    
    


        
            
         
         
        
    