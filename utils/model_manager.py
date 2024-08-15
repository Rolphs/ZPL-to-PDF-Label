import os
import json

# Ruta donde se guardan las preferencias y el consecutivo
PREFERENCES_FILE = 'preferences.json'


def cargar_datos():
    """
    Carga las preferencias y el consecutivo desde un archivo JSON.
    """
    if os.path.exists(PREFERENCES_FILE):
        with open(PREFERENCES_FILE, 'r') as file:
            return json.load(file)
    else:
        return {"consecutivo": 1, "directorio": "", "nomenclatura": "Etiqueta"}


def guardar_datos(data):
    """
    Guarda las preferencias y el consecutivo en un archivo JSON.
    """
    with open(PREFERENCES_FILE, 'w') as file:
        json.dump(data, file)


def sugerir_nombre_archivo(directorio_actual):
    """
    Sugiere un nombre de archivo basado en el consecutivo, la nomenclatura preferida y el directorio.
    :param directorio_actual: El directorio actual donde se guardará el archivo.
    :return: Nombre sugerido para el archivo.
    """
    datos = cargar_datos()
    consecutivo = datos['consecutivo']
    nomenclatura = datos.get('nomenclatura', 'Etiqueta')

    nombre_sugerido = f"{nomenclatura}_{consecutivo:04d}.pdf"
    datos['consecutivo'] += 1  # Incrementar el consecutivo para la próxima etiqueta

    # Guardar el último directorio usado
    if directorio_actual:
        datos['directorio'] = directorio_actual

    guardar_datos(datos)

    return nombre_sugerido


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