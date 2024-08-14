import os
import datetime


def sugerir_nombre_archivo(directorio):
    fecha_actual = datetime.datetime.now().strftime("%y%m%d")
    contador = 1

    while True:
        nombre_sugerido = f"label_{fecha_actual}_{contador}.pdf"
        ruta_sugerida = os.path.join(directorio, nombre_sugerido)
        if not os.path.exists(ruta_sugerida):
            break
        contador += 1

    return nombre_sugerido

def actualizar_modelo_guardado(file_path):
    # Aquí podrías actualizar el modelo de aprendizaje no supervisado basado en el archivo guardado.
    pass