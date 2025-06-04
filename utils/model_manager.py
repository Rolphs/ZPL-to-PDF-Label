import os
import json

# Ruta donde se guardan las preferencias y el consecutivo
PREFERENCES_FILE = 'preferences.json'
DEFAULT_PREFERENCES_FILE = 'preferences.example.json'


def cargar_datos():
    """
    Carga las preferencias y el consecutivo desde un archivo JSON. Si el archivo
    de usuario no existe, intenta cargar desde ``preferences.example.json``.
    """
    if os.path.exists(PREFERENCES_FILE):
        with open(PREFERENCES_FILE, 'r') as file:
            return json.load(file)
    elif os.path.exists(DEFAULT_PREFERENCES_FILE):
        with open(DEFAULT_PREFERENCES_FILE, 'r') as file:
            return json.load(file)
    else:
        return {"consecutivo": 1, "directorio": "", "nomenclatura": "Etiqueta"}


def guardar_datos(data):
    """
    Guarda las preferencias y el consecutivo en un archivo JSON.
    """
    with open(PREFERENCES_FILE, 'w') as file:
        json.dump(data, file)


def sugerir_nombre_archivo(directorio_actual, lote=False):
    """
    Sugiere un nombre de archivo basado en el consecutivo, la nomenclatura preferida y el directorio.
    :param directorio_actual: El directorio actual donde se guardará el archivo.
    :param lote: Booleano que indica si se está manejando un lote de archivos.
    :return: Nombre sugerido para el archivo.
    """
    datos = cargar_datos()
    consecutivo = datos['consecutivo']
    nomenclatura = datos.get('nomenclatura', 'Etiqueta')

    nombre_sugerido = f"{nomenclatura}_{consecutivo:04d}.pdf"

    if not lote:
        datos['consecutivo'] += 1  # Incrementar el consecutivo solo si no es un lote
        guardar_datos(datos)

    # Guardar el último directorio usado
    if directorio_actual:
        datos['directorio'] = directorio_actual

    return nombre_sugerido


def sugerir_nombres_para_lote(directorio_actual, cantidad):
    """
    Sugiere nombres de archivos para un lote basado en el consecutivo, la nomenclatura preferida y el directorio.
    :param directorio_actual: El directorio actual donde se guardarán los archivos.
    :param cantidad: Cantidad de archivos en el lote.
    :return: Lista de nombres sugeridos para el lote.
    """
    datos = cargar_datos()
    consecutivo = datos['consecutivo']
    nomenclatura = datos.get('nomenclatura', 'Etiqueta')

    nombres_sugeridos = [f"{nomenclatura}_{i:04d}.pdf" for i in range(consecutivo, consecutivo + cantidad)]

    datos['consecutivo'] += cantidad  # Incrementar el consecutivo por la cantidad de archivos en el lote
    guardar_datos(datos)

    # Guardar el último directorio usado
    if directorio_actual:
        datos['directorio'] = directorio_actual

    return nombres_sugeridos


def actualizar_modelo_guardado(pdf_file):
    """
    Actualiza el modelo de guardado con la última ubicación utilizada.
    :param pdf_file: Ruta completa del archivo guardado.
    """
    datos = cargar_datos()
    directorio_actual = os.path.dirname(pdf_file)
    if directorio_actual and directorio_actual != datos['directorio']:
        datos['directorio'] = directorio_actual
        guardar_datos(datos)


def mostrar_etiquetas_generadas():
    """
    Muestra el número total de etiquetas generadas hasta ahora.
    """
    datos = cargar_datos()
    total_etiquetas = datos['consecutivo'] - 1  # Restamos 1 porque ya se incrementó antes
    print(f"Etiquetas generadas: {total_etiquetas}")