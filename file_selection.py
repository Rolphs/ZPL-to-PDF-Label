import os
import datetime

# Función para sugerir un nombre de archivo basado en la fecha y un número consecutivo
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

# Función para seleccionar la ubicación de guardado
def seleccionar_ubicacion_guardado(directorio_sugerido, nombre_archivo_sugerido):
    default_name = os.path.join(directorio_sugerido, nombre_archivo_sugerido)
    archivo_guardado = filedialog.asksaveasfilename(
        title="Guardar archivo PDF como...",
        initialdir=directorio_sugerido,
        initialfile=nombre_archivo_sugerido,
        filetypes=[("PDF Files", "*.pdf")]
    )
    return archivo_guardado if archivo_guardado else None