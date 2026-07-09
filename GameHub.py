juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate']
}

inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}

#FUNCIONES

def leer_opcion():
    while True:
        try:
            op = int(input("Ingrese una opción (1-6): "))
            break
        except ValueError:
            print("Ingrese un número entero")
    
    if op > 6 or op < 1:
        print("Debe seleccionar una opción válida")
    else:
        return op


def stock_plataforma(plataforma):
    stock_plataforma = 0
    for codigo,consola in juegos.items():
        if consola[1] == plataforma:
            stock_plataforma = stock_plataforma + inventario[codigo][1]

    print(f"El total de stock disponibles es: {stock_plataforma}")


def busqueda_precio(p_min,p_max):
    lista_precios_encontrados = []
    for codigo,precio in inventario.items():
        if precio[0] >= p_min and precio[0] <= p_max:
            lista_precios_encontrados.append(juegos[codigo][0])
    
    print(f"Los juegos encontrados son: {lista_precios_encontrados}")


def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo) == True:
       for codigo,precio in inventario.items():
           precio[0] = nuevo_precio
    else:
        return False


    
def buscar_codigo(codigo):  
    if codigo in inventario:
        return True
    else:
        return False
    
def verif_codigo(codigo):

    if codigo == "":
        return False
    elif codigo in inventario or codigo in juegos:
        return False
    else:
        return True

def verif_titulo(titulo):
    if titulo == "":
        return False
    else:
        True

def verif_plataforma(plataforma):
    if plataforma == "":
        return False
    else:
        return True

def verif_genero(genero):
    if genero == "":
        return False
    else:
        return True

def verif_clasificacion(clasificacion):
    if clasificacion == "E" or clasificacion == "T" or clasificacion == "M":
        return True
    else:
        return False
    
def ver_multiplayer(multiplayer):
    if multiplayer == "s":
        return True
    elif multiplayer == "n":
        return False
    else:
        return 1

def verif_editor(editor):
    if editor == "":
        return False
    else:
        return True

def verif_precio(precio):
    if precio <= 0:
        return False
    else:
        return True
    
def verif_stock(stock):
    if stock <= 0:
        return False
    else:
        return True

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):
    if codigo in juegos or codigo in inventario:
        return False
    else:
        inventario[codigo][precio,stock]
        juegos[codigo][titulo,plataforma,genero,clasificacion,multiplayer,editor]
        return True        


def eliminar_juego(codigo):
    if buscar_codigo(codigo) == True:
        juegos.pop(codigo)
        inventario.pop(codigo)
        return True
    else:
        return False

#Ejercicio principal

while True:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("=====================================")

    opcion = leer_opcion()

    if opcion == 1:
        while True:
            plataforma = input("Ingrese plataforma a consultar (PC,Switch,PS5,Xbox): ").strip().upper()
            if plataforma == "":
                print("¡Ingrese una consola!")
            else:
                break
        stock_plataforma(plataforma)

    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                break
            except ValueError:
                print("Debe ingresar valores enteros")
                
        while True:    
            try:
                p_max = int(input("Ingrese precio máximo: "))
                break
            except ValueError:
                print("Debe ingresar valores enteros")

        busqueda_precio(p_min,p_max)
    
    elif opcion == 3:

        while True:

            codigo = input("Ingrese código del juego: ").upper()
            
            while True:
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                except:
                    print("Debe ingresar un número válido")
                
                if nuevo_precio <= 0:
                    print("Ingrese un número entero positivo")
                else:
                    break

            if actualizar_precio(codigo, nuevo_precio):
                print("Precio actualizado")
            else:
                print("El código no existe")

            repetir = input("¿Desea actualizar otro precio? (s/n): ").lower
            if repetir == "n":
                break

    elif opcion == 4:
        codigo = input("Ingrese código del juego: ").upper().strip()
        titulo = input("Ingrese título: ")
        plataforma = input("Ingrese plataforma: ")
        genero = input("Ingrese género: ")
        clasificacion = input("Ingrese clasificación (E/T/M): ").upper
        multiplayer = input("¿Es multiplayer? (s/n): ").lower
        editor = input("Ingrese editor: ")
        precio = int(input("Ingrese precio: "))
        stock = int(input("Ingrese stock: "))
    
        if verif_codigo(codigo) == False:
            print("Codigo inválido o en uso")
        elif verif_titulo(titulo) == False:
            print("Introduzca titulo")
        elif verif_plataforma(plataforma) == False:
            print("Introduzca plataforma")
        elif verif_genero(genero) == False:
            print("Introduzca género")
        elif verif_clasificacion(clasificacion) == False:
            print("Introduzca una clasificación válida")
        elif ver_multiplayer(multiplayer) == 1:
            print("Ingrese una opción válida (s/n)")
        elif verif_editor(editor) == False:
            print("Introduzca editor")
        elif verif_precio(precio) == False:
            print("Ingrese un número mayor a 0")
        elif verif_stock(stock) == False:
            print("Ingrese un número mayor a 0")
        else:
            agregado = agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock)
            if agregado == False:
                print("El código ya existe")
            else:
                print("Juego agregado")

    elif opcion == 5:
        codigo = input("Ingrese código del juego: ").upper().strip()
        if eliminar_juego(codigo) == True:
            print("Juego eliminado")
        else:
            print("Juego no existe")
    
    elif opcion == 6:
        print("Programa finalizado.")
        break
    