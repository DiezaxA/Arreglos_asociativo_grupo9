import sys
# 1. ARREGLO ASOCIATIVO PRINCIPAL (Estructura de Filas y Columnas)
# Las filas están representadas por un ID único (ej. 'REG01') 
# Las columnas corresponden a las llaves internas: 'Nombre', 'Prueba' y 'Tiempo'
registro_rendimiento = {}


# 3. VALIDACIONES DE TIPOS DE DATOS
def validar_id(mensaje, nuevo_registro=True):
    """Valida que el ID tenga un formato correcto y maneja su unicidad."""
    while True:
        id_reg = input(mensaje).strip().upper()
        if not id_reg:
            print(" Error: El ID no puede estar vacío.")
            continue
        
        if nuevo_registro and id_reg in registro_rendimiento:
            print(f" Error: El ID '{id_reg}' ya existe. Use otro o modifique el existente.")
            continue
        elif not nuevo_registro and id_reg not in registro_rendimiento:
            print(f" Error: El ID '{id_reg}' no se encuentra en el sistema.")
            continue
            
            
        return id_reg

def validar_texto(mensaje):
    """Valida que la entrada de texto no esté vacía y contenga caracteres válidos."""
    while True:
        texto = input(mensaje).strip()
        if len(texto) < 2:
            print(" Error: El campo debe contener al menos 2 caracteres.")
            continue
        return texto

def validar_tiempo(mensaje):
    """Valida que el tiempo ingresado sea un número flotante positivo."""
    while True:
        try:
            tiempo = float(input(mensaje))
            if tiempo <= 0:
                print(" Error: El tiempo debe ser un valor mayor a cero.")
                continue
            return tiempo
        except ValueError:
            print(" Error: Entrada inválida. Ingrese un número decimal (ejemplo: 13.50 o 10.14).")


# 2. FUNCIONES DEL MENÚ
def introducir_registro():
    """Opción 1: Captura y valida nuevos datos para agregar al arreglo asociativo."""
    print("\n--- [NUEVO REGISTRO DE RENDIMIENTO] ---")
    id_reg = validar_id("Ingrese el ID del registro (ej. REG01, REG02): ", nuevo_registro=True)
    
    nombre = validar_texto("Nombre del Atleta: ")
    prueba = validar_texto("Tipo de Prueba / Distancia (ej. 100m, 2.4km): ")
    tiempo = validar_tiempo("Tiempo registrado (en segundos o minutos): ")
    
    # Inserción en el arreglo asociativo
    registro_rendimiento[id_reg] = {
        "Nombre": nombre,
        "Prueba": prueba,
        "Tiempo": tiempo
    }
    print(f" ¡Registro '{id_reg}' guardado exitosamente!")

def modificar_registro():
    """Opción 2: Busca un ID existente y permite sobreescribir sus columnas con validación."""
    print("\n--- [MODIFICAR REGISTRO EXISTENTE] ---")
    if not registro_rendimiento:
        print("⚠ No hay registros guardados en el sistema para modificar.")
        return
        
    id_reg = validar_id("Ingrese el ID del registro que desea modificar: ", nuevo_registro=False)
    
    print(f"\nDatos actuales del registro {id_reg}:")
    print(f"  • Nombre: {registro_rendimiento[id_reg]['Nombre']}")
    print(f"  • Prueba: {registro_rendimiento[id_reg]['Prueba']}")
    print(f"  • Tiempo: {registro_rendimiento[id_reg]['Tiempo']}")
    print("\nIngrese los nuevos datos:")
    
    nombre = validar_texto("Nuevo Nombre del Atleta: ")
    prueba = validar_texto("Nueva Prueba / Distancia: ")
    tiempo = validar_tiempo("Nuevo Tiempo registrado: ")
    
    # Actualización de los datos en el arreglo asociativo
    registro_rendimiento[id_reg] = {
        "Nombre": nombre,
        "Prueba": prueba,
        "Tiempo": tiempo
    }
    print(f" ¡Registro '{id_reg}' actualizado correctamente!")

def imprimir_lista_registros():
    """Opción 3: Despliega de forma tabulada la matriz de datos guardada."""
    print("\n--- [LISTA DE REGISTROS ALMACENADOS] ---")
    if not registro_rendimiento:
        print("Imposible imprimir: El arreglo asociativo está vacío.")
        return
    
    # Cabecera de la tabla con formato de alineación
    print(f"{'ID (Fila)':<12} | {'Nombre Atleta':<20} | {'Prueba/Distancia':<18} | {'Tiempo':<10}")
    print("-" * 68)
    
    # Lectura del arreglo asociativo
    for id_reg, columnas in registro_rendimiento.items():
        print(f"{id_reg:<12} | {columnas['Nombre']:<20} | {columnas['Prueba']:<18} | {columnas['Tiempo']:<10.2f}")
    print("-" * 68)


# ALGORITMO PRINCIPAL Y MENÚ DE INTERFAZ
def ejecutar_sistema():
    """Maneja el bucle principal del menú de opciones."""
    while True:
        print("\n==================================================")
        print("   SISTEMA DE REGISTRO DE ATLETAS DE GUATIRE       ")   
        print("==================================================")
        print(" 1. Introducir Registro")
        print(" 2. Modificar Registro")
        print(" 3. Imprimir Lista de Registros")
        print(" 4. Salir del Sistema")
        print("==================================================")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            introducir_registro()
        elif opcion == "2":
            modificar_registro()
        elif opcion == "3":
            imprimir_lista_registros()
        elif opcion == "4":
            print("\nCerrando sesión. Programa finalizado correctamente.")
            sys.exit()
        else:
            print(" Opción inválida. Por favor, digite un número entre 1 y 4.")

if __name__ == "__main__":
    ejecutar_sistema()      