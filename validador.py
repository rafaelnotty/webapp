# validador.py

class Contador:
    def __init__(self):
        self.count = 0

    def validar_mensaje(self, mensaje):
        if mensaje.lower() == "hola":
            self.count += 1
            return f"Respuesta {self.count}"
        return None

contador = Contador()