# Función para agregar nuevas traducciones al archivo
def agregar_traduccion(archivo, palabra_origen, palabra_destino):
    with open(archivo, 'a') as f:
        f.write(f'{palabra_origen}={palabra_destino}\n')

# Función para traducir una palabra de un idioma al otro
def traducir(archivo, idioma_origen, idioma_destino, palabra):
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    for linea in lineas:
        origen, destino = linea.strip().split('=')
        if idioma_origen == origen and idioma_destino == destino:
            return palabra
        elif idioma_origen == destino and idioma_destino == origen:
            return palabra

    return "Traducción no encontrada"

# Nombre del archivo de traducción
archivo = "EN-ES.txt"

while True:
    print("Seleccione una opción:")
    print("1. Agregar nueva traducción")
    print("2. Traducir")
    print("3. Salir")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        palabra_origen = input("Palabra en el idioma origen: ")
        palabra_destino = input("Palabra en el idioma destino: ")
        agregar_traduccion(archivo, palabra_origen, palabra_destino)
        print("Traducción agregada con éxito.")
    elif opcion == "2":
        idioma_origen = input("Idioma origen (EN o ES): ")
        idioma_destino = input("Idioma destino (EN o ES): ")
        palabra = input("Palabra a traducir: ")
        traduccion = traducir(archivo, idioma_origen, idioma_destino, palabra)
        if traduccion:
            print(f"{idioma_origen}-{idioma_destino} {palabra} --> {traduccion}")
        else:
            print("Traducción no encontrada.")
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Intente nuevamente.")
