import pandas as pd

def modelo_one_r(datos: pd.DataFrame, clase: str) -> tuple:
  """
  Implementa el algoritmo One-R.

  Args:
    datos: Un DataFrame de pandas que contiene los datos.
    clase: El nombre de la columna que contiene la clase.

  Returns:
    Una tupla que contiene:
      - El nombre de la columna con la mejor regla.
      - Un arreglo de arreglos, donde cada arreglo interno representa una regla 
        y contiene el valor de la característica y la clase predicha.
  """

  mejor_columna = None
  mejor_reglas = None
  mejor_precision = 0

  for columna in datos.columns:
    if columna == clase:
      continue

    reglas = {}
    for valor in datos[columna].unique():
      # Contar las ocurrencias de cada clase para el valor actual de la característica
      conteo_clases = datos[datos[columna] == valor][clase].value_counts()
      # Predecir la clase más frecuente para ese valor de la característica
      clase_predicha = conteo_clases.index[0]
      reglas[valor] = clase_predicha

    # Calcular la precisión de las reglas para la columna actual
    predicciones = datos[columna].map(reglas)
    precision = (predicciones == datos[clase]).mean()

    # Actualizar la mejor regla si la precisión actual es mayor
    if precision > mejor_precision:
      mejor_precision = precision
      mejor_columna = columna
      mejor_reglas = [[valor, clase_predicha] for valor, clase_predicha in reglas.items()]

  return mejor_columna, mejor_reglas

if __name__ == '__main__':
    # Crear un DataFrame de ejemplo
    datos = pd.DataFrame({
        'clima': ['soleado', 'nublado', 'lluvioso', 'soleado', 'soleado', 'nublado'],
        'temperatura': ['caliente', 'templado', 'frio', 'caliente', 'caliente', 'templado'],
        'viento': ['debil', 'fuerte', 'debil', 'debil', 'fuerte', 'fuerte'],
        'jugar': ['no', 'no', 'si', 'si', 'si', 'no']
    })

    # Obtener la mejor regla de One-R
    columna, reglas = modelo_one_r(datos, 'jugar')

    # Imprimir la columna y las reglas
    print(f"La mejor regla de One-R se basa en la columna: {columna}")
    print("Reglas:")
    for regla in reglas:
      print(f"Si {columna} es {regla[0]}, entonces jugar es {regla[1]}")