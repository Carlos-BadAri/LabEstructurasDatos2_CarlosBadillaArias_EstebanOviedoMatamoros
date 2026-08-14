from ListaDoblemente import ListaDoblemente

if __name__ == "__main__":
    # Crear la lista doblemente enlazada
    lista = ListaDoblemente()
    try:
        with open("datos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                # Evitar líneas vacías
                if linea != "":
                    valor = linea
                    # Insertar el valor en la lista
                    lista.insertarAlInicio(valor)
                    lista.imprimirAdelante()
                    print(f"Cantidad de elementos: {lista.cantidadElementos()}")

    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")
        exit()