def leer_opcion():
    while True:
        try:
            print("\n========== MENÚ PRINCIPAL ==========")
            print("1. Stock por plataforma")
            print("2. Búsqueda de juegos por rango de precio")
            print("3. Actualizar precio de juego")
            print("4. Agregar juego")
            print("5. Eliminar juego")
            print("6. Salir")
            print("====================================")
            opc = int(input("Ingrese opción: "))
            if 1 <= opc <= 6:
                return opc
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def validar_codigo(codigo, juegos):
    return bool(codigo.strip()) and (codigo.upper() not in juegos)

def validar_titulo(titulo):
    return bool(titulo.strip())

def validar_plataforma(plataforma):
    return bool(plataforma.strip())

def validar_genero(genero):
    return bool(genero.strip())

def validar_clasificacion(clasificacion):
    return clasificacion.strip().upper() in ['E', 'T', 'M']

def validar_multiplayer(mp_str):
    return mp_str.strip().lower() in ['s', 'n']

def validar_editor(editor):
    return bool(editor.strip())

def validar_precio(precio_str):
    try:
        return int(precio_str) > 0
    except ValueError:
        return False

def validar_stock(stock_str):
    try:
        return int(stock_str) >= 0
    except ValueError:
        return False

def stock_plataforma(juegos, inventario):
    plataforma_buscar = input("Ingrese plataforma a consultar: ").strip().lower()
    total_stock = 0
    for codigo, datos in juegos.items():
        if datos[1].strip().lower() == plataforma_buscar:
            if codigo in inventario:
                total_stock += inventario[codigo][1]
    print(f"El total de stock disponibles es: {total_stock}")

def busqueda_precio(p_min, p_max, juegos, inventario):
    resultados = []
    for codigo, datos in juegos.items():
        titulo = datos[0]
        if codigo in inventario:
            precio = inventario[codigo][0]
            stock = inventario[codigo][1]
            if p_min <= precio <= p_max and stock > 0:
                resultados.append(f"{titulo}-{codigo}")
    if resultados:
        resultados.sort()
        print(f"Los juegos encontrados son: {resultados}")
    else:
        print("No hay juegos en ese rango de precios.")

def actualizar_precio(juegos, inventario):
    while True:
        codigo = input("Ingrese código del juego: ").strip().upper()
        if codigo in juegos:
            while True:
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio > 0:
                        inventario[codigo][0] = nuevo_precio
                        print("Precio actualizado")
                        break
                    else:
                        print("El nuevo precio debe ser un valor entero positivo.")
                except ValueError:
                    print("El nuevo precio debe ser un valor entero positivo.")
        else:
            print("El código no existe")
        resp = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
        if resp != 's':
            break

def agregar_juego(juegos, inventario):
    codigo = input("Ingrese código del juego: ").strip().upper()
    if not validar_codigo(codigo, juegos):
        print("El código ya existe o es inválido")
        return
    titulo = input("Ingrese título: ").strip()
    if not validar_titulo(titulo): return
    plataforma = input("Ingrese plataforma: ").strip()
    if not validar_plataforma(plataforma): return
    genero = input("Ingrese género: ").strip()
    if not validar_genero(genero): return
    clasificacion = input("Ingrese clasificación: ").strip().upper()
    if not validar_clasificacion(clasificacion): return
    mp_str = input("¿Es multiplayer? (s/n): ").strip().lower()
    if not validar_multiplayer(mp_str): return
    editor = input("Ingrese editor: ").strip()
    if not validar_editor(editor): return
    precio_str = input("Ingrese precio: ").strip()
    if not validar_precio(precio_str): return
    stock_str = input("Ingrese stock: ").strip()
    if not validar_stock(stock_str): return
    
    juegos[codigo] = [titulo, plataforma, genero, clasificacion, mp_str == 's', editor]
    inventario[codigo] = [int(precio_str), int(stock_str)]
    print("Juego agregado")

def eliminar_juego(codigo, juegos, inventario):
    if codigo.upper() in juegos:
        del juegos[codigo.upper()]
        del inventario[codigo.upper()]
        return True
    return False

def main():
    juegos = {
        'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
        'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
        'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
        'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
        'G005': ['Mystic Face', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
        'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate']
    }
    
    inventario = {
        'G001': [19990, 7],
        'G002': [15990, 0],
        'G003': [42990, 3],
        'G004': [14990, 5],
        'G005': [17990, 9],
        'G006': [39990, 2]
    }
    
    while True:
        opc = leer_opcion()
        if opc == 1:
            stock_plataforma(juegos, inventario)
        elif opc == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min >= 0 and p_max >= p_min:
                        break
                    else:
                        print("Debe ingresar valores enteros.")
                except ValueError:
                    print("Debe ingresar valores enteros.")
            busqueda_precio(p_min, p_max, juegos, inventario)
        elif opc == 3:
            actualizar_precio(juegos, inventario)
        elif opc == 4:
            agregar_juego(juegos, inventario)
        elif opc == 5:
            cod_elim = input("Ingrese código del juego: ").strip().upper()
            if eliminar_juego(cod_elim, juegos, inventario):
                print("Juego eliminado")
            else:
                print("El código no existe")
        elif opc == 6:
            print("Programa finalizado.")
            break

if __name__ == '__main__':
    main()
