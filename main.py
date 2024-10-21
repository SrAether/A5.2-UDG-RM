import pandas as pd  # Importamos la librería pandas para trabajar con dataframes
import datos.manejo as manejo
import os  # Importamos la librería os para limpiar la pantalla
import pyfiglet
from modelos.zeroR import modelo_zero_r
from modelos.oneR import modelo_one_r

# VARIABLES GLOBALES PARA COLORES ANSI
RESET = "\033[0m"
NEGRO = "\033[30m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BLANCO = "\033[37m"
NEGRITA = "\033[1m"
SUBRAYADO = "\033[4m"

# Función para limpiar la pantalla según el sistema operativo
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Función para mostrar los datos actuales
def mostrar_datos_actuales(ruta_dataset=None, dataset=None, tam_dataset_prueba=None, modelo_selec=None, clase=None):
    """Muestra los datos agregados al programa."""
    if any([ruta_dataset, dataset, tam_dataset_prueba, modelo_selec, clase]):
        print(CYAN + NEGRITA + "DATOS ACTUALMENTE AGREGADOS" + RESET)
        if ruta_dataset:
            print(MAGENTA + "Ruta dataset: " + RESET, ruta_dataset)
        if dataset is not None:
            print(MAGENTA + "Dataset cargado." + RESET)
        if tam_dataset_prueba:
            print(MAGENTA + "Tamaño dataset prueba: " + RESET, tam_dataset_prueba)
        if modelo_selec:
            print(MAGENTA + "Modelo seleccionado: " + RESET, modelo_selec)
        if clase:
            print(MAGENTA + "Clase seleccionada: " + RESET, clase)
    else:
        print(AMARILLO + "No hay datos agregados." + RESET)

# Función para cargar los datos
def cargar_datos():
    """Carga un dataset en formato CSV."""
    limpiar_pantalla()
    while True:
        print(AZUL + NEGRITA + "CARGAR DATOS" + RESET)
        ruta_dataset = input("Ingrese la ruta del dataset: ")
        try:
            dataset = manejo.cargar_datos(ruta_dataset)
            return ruta_dataset, dataset
        except Exception as e:
            limpiar_pantalla()
            print(ROJO + "Error al cargar el dataset" + RESET)
            print(AMARILLO + str(e) + RESET)

# Función para seleccionar el tamaño del dataset de prueba
def seleccionar_tam_dataset_prueba():
    """Selecciona el tamaño del dataset de prueba."""
    limpiar_pantalla()
    while True:
        try:
            print(AZUL + NEGRITA + "TAMAÑO DEL DATASET DE PRUEBA" + RESET)
            print("Por ejemplo, si se selecciona 0.2, el 20% del dataset se usará para pruebas.")
            tam_dataset_prueba = float(input("Ingrese el tamaño del dataset de prueba (entre 0 y 1): "))
            if 0 < tam_dataset_prueba < 1:
                return tam_dataset_prueba
            else:
                limpiar_pantalla()
                print(ROJO + "El valor debe estar entre 0 y 1" + RESET)
        except ValueError:
            limpiar_pantalla()
            print(ROJO + "Error: Debe ingresar un número válido entre 0 y 1." + RESET)

# Función para mostrar opciones del menú principal
def mostrar_menu_principal():
    """Muestra el menú principal del programa."""
    print(AZUL + NEGRITA + "MENU PRINCIPAL" + RESET)
    print(VERDE + "1. Cargar datos")
    print("2. Porcentaje del dataset para pruebas")
    print("3. Seleccionar modelo")
    print("4. Seleccionar clase")
    print("5. Evaluar Modelo")
    print("6. Salir" + RESET)
    return input("Seleccione una opción: ")

# Función para seleccionar el modelo
def seleccionar_modelo():
    """Función placeholder para seleccionar modelo."""
    limpiar_pantalla()
    while True:
        try:
            print(AZUL + NEGRITA + "SELECCIONAR MODELO" + RESET)
            print(AMARILLO + "Modelos disponibles:" + RESET)
            print(VERDE + "1. ZeroR")
            print("2. OneR" + RESET)
            seleccion = int(input("Seleccione un modelo: "))
            if seleccion == 1:
                return "ZeroR"
            elif seleccion == 2:
                return "OneR"
            else:
                limpiar_pantalla()
                print(ROJO + "Opción no válida" + RESET)
        except ValueError:
            limpiar_pantalla()
            print(ROJO + "Error: Debe ingresar un número válido." + RESET)
       
# Función para seleccionar la clase
def seleccionar_clase(dataset):
    """Función para seleccionar la clase."""
    limpiar_pantalla()
    if dataset is None:
        raise ValueError("No se ha cargado ningún dataset.")
    print(AZUL + NEGRITA + "SELECCIONAR CLASE" + RESET)
    print(AMARILLO + "Columnas disponibles:" + RESET)
    contador = 1
    for columna in dataset.columns:
        print(f"{contador}. {columna}")
        contador += 1
    seleccion = int(input("Seleccione una columna: "))
    return dataset.columns[seleccion - 1]     

# Función para evaluar el modelo (vacía)
def evaluar_modelo(dataset: pd.DataFrame, tam_dataset_prueba, modelo_selec, clase):
    """Función para evaluar el modelo (A implementar)."""
    # Verificamos si se han cargado los datos correctamente
    if dataset.empty:
        raise ValueError("El dataset está vacío o no se ha cargado.")
    if tam_dataset_prueba is None or not (0 < tam_dataset_prueba < 1):
        raise ValueError("El tamaño del dataset de prueba no es válido o no ha sido seleccionado.")
    if not modelo_selec:
        raise ValueError("No se ha seleccionado un modelo.")
    if not clase:
        raise ValueError("No se ha especificado la clase a predecir.")
    print(AZUL + NEGRITA + "EVALUAR MODELO" + RESET) 
    
    # Preguntamos si desea continuar
    continuar = input("¿Desea continuar con la evaluación del modelo? (s/n): ")
    if continuar.lower() != "s" and continuar.lower() != "si" and continuar.lower() != "y":
        return
    # Pedimos el número de iteraciones
    while True:
        try:
            iteraciones = int(input("Ingrese el número de iteraciones: "))
            break
        except ValueError:
            print(ROJO + "Error: Debe ingresar un número válido." + RESET)
    # Evaluamos el modelo
    arregloResultados = []
    arregloPrediccionExitosa = []
    for i in range(iteraciones):
        datos_entrenamiento, datos_prueba = manejo.generador_de_subconjuntos(dataset, tam_dataset_prueba, i)
        if modelo_selec == "ZeroR":
            resultado = modelo_zero_r(datos_entrenamiento, clase)
            # Calculamos la precisión del modelo usando los datos de prueba
            prediccion_exitosa = datos_prueba[clase] == resultado
            precision = prediccion_exitosa.sum() / len(prediccion_exitosa)
            arregloPrediccionExitosa.append(precision)
            arregloResultados.append(resultado)
        elif modelo_selec == "OneR":
            resultado = modelo_one_r(datos_entrenamiento, clase)
            # estructura de resultado: (mejor_columna, mejor_reglas)
            # mejor_reglas: [[valor, clase_predicha], [valor, clase_predicha], ...]
            mejor_columna, mejor_reglas = resultado
            arregloResultados.append(mejor_columna + " -> " + str(mejor_reglas))
            # Calcular la precisión del modelo usando los datos de prueba
            prediccion_exitosa = datos_prueba[mejor_columna].map(dict(mejor_reglas)) == datos_prueba[clase]
            precision = prediccion_exitosa.sum() / len(prediccion_exitosa)
            arregloPrediccionExitosa.append(precision)
        
        else:
            raise ValueError("Modelo no válido.")
        
    print("Resultados de las iteraciones:")
    for i in range(iteraciones):
        print(f"Iteración {i + 1}: {arregloResultados[i]}")
        print(f"Precisión: {arregloPrediccionExitosa[i]}")
        
    # Generar archivo de resultados
    guardar_resultados = input("¿Desea guardar los resultados en un archivo? (s/n): ")
    if guardar_resultados.lower() == "s" or guardar_resultados.lower() == "si" or guardar_resultados.lower() == "y":
        nombre_archivo = input("Ingrese el nombre del archivo (sin extensión): ")
        try:
            with open(f"{nombre_archivo}.txt", "w") as archivo:
                for i in range(iteraciones):
                    archivo.write(f"Iteración {i + 1}: {arregloResultados[i]}\n")
                    archivo.write(f"Precisión: {arregloPrediccionExitosa[i]}\n\n")
            print(VERDE + "Resultados guardados exitosamente." + RESET)
        except Exception as e:
            print(ROJO + "Error al guardar los resultados." + RESET)
            print(AMARILLO + str(e) + RESET)
    # presione cualquier tecla para continuar
    input("Presione cualquier tecla para continuar...")
    

# Ciclo principal del programa
def main():
    # Variables locales
    ruta_data_set = None
    dataset = None
    tam_dataset_prueba = None
    modelo_selec = None
    clase = None
    
    # Limpiar pantalla inicial
    limpiar_pantalla()
    
    # Ciclo principal del menú
    while True:
        try:
            # Mostrar datos actuales
            mostrar_datos_actuales(ruta_data_set, dataset, tam_dataset_prueba, modelo_selec, clase)
            
            # Mostrar menú y obtener la opción seleccionada
            seleccion = mostrar_menu_principal()
            
            # Procesar la selección del usuario
            if seleccion == "1":
                ruta_data_set, dataset = cargar_datos()
                limpiar_pantalla()

            elif seleccion == "2":
                tam_dataset_prueba = seleccionar_tam_dataset_prueba()
                limpiar_pantalla()

            elif seleccion == "3":
                modelo_selec = seleccionar_modelo()
                limpiar_pantalla()
                
            elif seleccion == "4":
                clase = seleccionar_clase(dataset)
                limpiar_pantalla()

            elif seleccion == "5":
                limpiar_pantalla()
                mostrar_datos_actuales(ruta_data_set, dataset, tam_dataset_prueba, modelo_selec, clase)
                evaluar_modelo(dataset, tam_dataset_prueba, modelo_selec, clase)
                limpiar_pantalla()

            elif seleccion == "6":
                print(AMARILLO + "Saliendo..." + RESET)
                ascii_art = pyfiglet.figlet_format("Desarrollado por:")
                print(ROJO + ascii_art + RESET)
                ascii_art = pyfiglet.figlet_format("Aether")
                print(CYAN + ascii_art + RESET)
                break

            else:
                limpiar_pantalla()
                print(ROJO + "Opción no válida" + RESET)

        except Exception as e:
            # En caso de cualquier excepción, limpiamos la pantalla y mostramos un error legible
            limpiar_pantalla()
            print(ROJO + "Informe de error" + RESET)
            print(str(e))  # Convertimos la excepción a cadena para mostrarla correctamente

    return 0


# Iniciar programa
if __name__ == "__main__":
    main()
