
# Proyecto de Algoritmos de Clasificación: OneR y ZeroR

Este proyecto implementa los algoritmos de clasificación OneR y ZeroR para realizar predicciones sobre un conjunto de datos. Los algoritmos se han desarrollado en Python y permiten evaluar el rendimiento de estos métodos básicos de clasificación.

## Descripción

Los algoritmos OneR y ZeroR son métodos simples de clasificación:

- **ZeroR**: Predice la clase mayoritaria sin tener en cuenta ningún atributo.
- **OneR**: Selecciona un solo atributo para realizar predicciones basadas en reglas sencillas.

Este proyecto divide el conjunto de datos en particiones y entrena ambos algoritmos utilizando las particiones para generar reglas de clasificación y luego evaluar su precisión.

## Estructura del Proyecto

- `modelos/oneR.py`: Implementación del algoritmo OneR.
- `modelos/zeroR.py`: Implementación del algoritmo ZeroR.
- `datos/manejo.py`: Modulo con funciones útiles para cargar los datos en un dataframe de pandas y para generar subconjuntos disjuntos.
- `README.md`: Explicación del proyecto.
- `main.py`: CLI que permite interactuar con los modelos

## Instrucciones de Uso

1. Clona este repositorio:
    ```
    git clone https://github.com/tu_usuario/nombre_del_proyecto.git
    ```

2. Instala los paquetes requeridos:
    ```
    pip install -r requirements.txt
    ```

3. Ejecuta el CLI:
    ```
    python main.py
    ```

4. Ejecuta una prueba del algoritmo OneR:
    ```
    python oneR.py
    ```

4. Ejecuta una prueba del algoritmo ZeroR:
    ```
    python zeroR .py
    ```

## Estructura
.
├── datos
│   └── manejo.py
├── main.py
├── modelos
│   ├── oneR.py
│   └── zeroR.py
├── REDME.md
└── requerimientos.txt

## Conjuntos de Datos

El proyecto utiliza pandas leer archivos, así que en general pueden probar cualquier conjunto de datos, es una implementación simple y es la primera vez que lo uso así que puede estar sujeto a errores

## Contacto

Si tienes preguntas o sugerencias, no dudes en ponerte en contacto a través de GitHub.
