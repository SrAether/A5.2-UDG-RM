import pandas as pd

def modelo_zero_r(datos: pd.DataFrame, clase: str) -> str:
    """
    Implementa el modelo ZeroR, que predice la clase mayoritaria en los datos.

    Args:
        datos (pd.DataFrame): El DataFrame que contiene los datos.
        clase (str): El nombre de la columna que contiene las etiquetas de clase.

    Returns:
        str: La clase mayoritaria en los datos.
    """
    # Verificamos si la columna de clase existe en el DataFrame
    if clase not in datos.columns:
        raise ValueError(f"La columna '{clase}' no se encuentra en los datos.")
    
    # Contamos la frecuencia de cada valor en la columna de clase
    clase_mayoritaria = datos[clase].mode()[0]
    
    return clase_mayoritaria

if __name__ == "__main__":
    # Creamos un DataFrame de ejemplo
    datos_ejemplo = pd.DataFrame({
        'Atributo1': [1, 2, 3, 4, 5],
        'Atributo2': ['X', 'Y', 'X', 'Y', 'X'],
        'Clase': ['Positivo', 'Negativo', 'Positivo', 'Positivo', 'Negativo']
    })
    
    # Definimos la columna de clase
    columna_clase = 'Clase'
    
    # Llamamos a la función modelo_zero_r
    clase_predicha = modelo_zero_r(datos_ejemplo, columna_clase)
    
    # Mostramos la clase mayoritaria predicha
    print(f"La clase mayoritaria predicha es: {clase_predicha}")