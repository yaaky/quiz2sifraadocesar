class Juego:
    
 def __init__(self, usuario_clave):
    self.usuario_clave = usuario_clave
    self.proceso_activo = False
    self.abecedario_base = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "v", "w", "x", "y", "z"]
    self.numero_base = list(range(10))
    self.nivel_seguridad = 0
    self.buffer_encriptado = []
    self.buffer_desencriptado = []

 def encriptar_mensaje(self):
    self.buffer_desencriptado = []
    self.proceso_activo = True
    print(f"\nBienvenido al Modulo de Encriptacion, {self.usuario_clave}!")
    self.nivel_seguridad = int(input(" Nivel de Cifrado (numero): "))
    mensaje = input("Introduce el mensaje a encriptar: ")
        
    for caracter in mensaje:
        if caracter.isdigit():
            indice = self.numero_base.index(int(caracter))
            nuevo = (indice - self.nivel_seguridad) % len(self.numero_base)
            self.buffer_desencriptado.append(str(self.numero_base[nuevo]))
        elif caracter.isalpha():
            caracter = caracter.lower()
        if caracter in self.abecedario_base:
                indice = self.abecedario_base.index(caracter)
                nuevo = (indice - self.nivel_seguridad) % len(self.abecedario_base)
                self.buffer_desencriptado.append(self.abecedario_base[nuevo])
        elif caracter == " ":
            self.buffer_desencriptado.append(" ")

        print("\nMensaje encriptado: ")
        print("----------------------------")
        print("", "".join(self.buffer_desencriptado))
        print("----------------------------")

def desencriptar_mensaje(self):
        self.buffer_encriptado = []
        self.proceso_activo = True
        print(f"\nBienvenido al Modulo de Desencriptación, {self.usuario_clave}!")
        self.nivel_seguridad = int(input(" Nivel de Cifrado usado (número): "))
        mensaje = input("Introduce el mensaje encriptado: ")
        
        for caracter in mensaje:
            if caracter.isdigit():
                indice = self.numero_base.index(int(caracter))
                nuevo = (indice + self.nivel_seguridad) % len(self.numero_base)
                self.buffer_encriptado.append(str(self.numero_base[nuevo]))
            elif caracter.isalpha():
                caracter = caracter.lower()
            if caracter in self.abecedario_base:
                indice = self.abecedario_base.index(caracter)
                nuevo = (indice + self.nivel_seguridad) % len(self.abecedario_base)
                self.buffer_encriptado.append(self.abecedario_base[nuevo])
            elif caracter == " ":
                self.buffer_encriptado.append(" ")

        print("\nMensaje desencriptado: ")
        print("----------------------------")
        print("", "".join(self.buffer_encriptado))
        print("----------------------------")

def cerrar_sesion(self):
    print(f"\n Sesion cerrada, {self.usuario_clave}!")
