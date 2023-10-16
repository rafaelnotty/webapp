def preguntar():
    while True:
        respuesta = input("¿Cumple con el requisito? (1: Sí, 2: No): ")
        if respuesta == "1":
            print("Requisito cumplido.")
            break
        elif respuesta == "2":
            print("Requisito no cumplido. Finalizando...")
            # Realiza cualquier acción de limpieza o manejo de errores aquí
            break
        else:
            print("Respuesta no válida. Por favor, elija 1 o 2.")

if __name__ == "__main__":
    preguntar()
