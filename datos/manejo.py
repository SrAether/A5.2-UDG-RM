import pandas as pd  # Importamos la librería pandas para trabajar con dataframes


def cargar_datos(ruta_datos: str) -> pd.DataFrame:
    """
    Carga un archivo CSV desde la ruta especificada.

    Args:
        ruta_datos: La ruta del archivo CSV a cargar.

    Returns:
        El DataFrame cargado.

    Raises:
        FileNotFoundError: Si el archivo no se encuentra en la ruta especificada.
        pd.errors.EmptyDataError: Si el archivo está vacío.
        pd.errors.ParserError: Si ocurre un error al analizar el archivo CSV.
        Exception: Para cualquier otro error inesperado.
    """
    try:
        # Leemos el archivo CSV con la ruta especificada
        datos = pd.read_csv(ruta_datos)

        # Verificamos si el DataFrame está vacío
        if datos.empty:
            raise pd.errors.EmptyDataError(f"El archivo CSV en la ruta '{ruta_datos}' está vacío.")

        return datos  # Retornamos el DataFrame
    except FileNotFoundError as e:
        mensaje = f"No se encontró el archivo en la ruta especificada: {ruta_datos}"
        raise FileNotFoundError(mensaje) from e
    except pd.errors.EmptyDataError as e:
        mensaje = f"El archivo CSV está vacío: {ruta_datos}"
        raise pd.errors.EmptyDataError(mensaje) from e
    except pd.errors.ParserError as e:
        mensaje = f"Error al analizar el archivo CSV en la ruta '{ruta_datos}': {e}"
        raise pd.errors.ParserError(mensaje) from e
    except Exception as e:
        mensaje = f"Se produjo un error desconocido al cargar el archivo '{ruta_datos}': {e}"
        raise Exception(mensaje) from e


def generador_de_subconjuntos(datos: pd.DataFrame, fraccion: float, semilla: int):
    """
    Divide el conjunto de datos en dos subconjuntos: entrenamiento y prueba de manera aleatoria.

    Parámetros:
    datos (pd.DataFrame): El conjunto de datos a dividir.
    fraccion (float): La proporción del conjunto de datos a usar para el entrenamiento (entre 0 y 1).
    semilla (int): La semilla para el generador de números aleatorios (para reproducibilidad).

    Retorna:
    pd.DataFrame, pd.DataFrame: Dos subconjuntos, uno para entrenamiento y otro para prueba.
    """
    try:
        if not 0 < fraccion < 1:
            raise ValueError("La fracción debe estar entre 0 y 1.")

        # Barajar (shuffle) los datos para evitar sesgo
        datos_barajados = datos.sample(frac=1, random_state=semilla).reset_index(drop=True)

        # Calcular el tamaño del subconjunto de entrenamiento
        tamano_entrenamiento = int(len(datos) * fraccion)

        # Crear los subconjuntos de entrenamiento y prueba
        datos_entrenamiento = datos_barajados[:tamano_entrenamiento]
        datos_prueba = datos_barajados[tamano_entrenamiento:]

        # Retornar los subconjuntos como una tupla
        return datos_entrenamiento, datos_prueba

    except Exception as e:
        mensaje = f"Error al generar subconjuntos: {e}"
        raise Exception(mensaje) from e

# Ejemplo de uso:
# datos = cargar_datos('ruta/a/archivo.csv')
# datos_entrenamiento, datos_prueba = generador_de_subconjuntos(datos, 0.8, 42)
