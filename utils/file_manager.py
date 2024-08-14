import os
from logger import logger
from tkinter import filedialog
from optimize import optimize_zpl
from generate import convert_zpl_to_pdf
from utils.model_manager import sugerir_nombre_archivo, actualizar_modelo_guardado

def leer_archivo_zpl(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()

def extraer_archivos_zip(ruta_zip):
    # Supongamos que esta función extrae archivos y devuelve una lista de rutas a los archivos extraídos
    pass

def guardar_zpl_optimizado(contenido, ruta_archivo):
    with open(ruta_archivo, 'w') as archivo:
        archivo.write(contenido)

def seleccionar_ubicacion_guardado(directorio, nombre_sugerido):
    archivo_guardado = filedialog.asksaveasfilename(
        initialdir=directorio,
        title="Guardar archivo como...",
        defaultextension=".pdf",
        initialfile=nombre_sugerido,
        filetypes=[("PDF files", "*.pdf")]
    )
    return archivo_guardado

def manejar_archivo_seleccionado(archivo):
    try:
        # Si el archivo es un ZIP, extraerlo
        if archivo.lower().endswith('.zip'):
            zpl_archivos = extraer_archivos_zip(archivo)
        else:
            zpl_archivos = [archivo]

        for zpl_archivo in zpl_archivos:
            # Leer el archivo ZPL/TXT
            zpl_data = leer_archivo_zpl(zpl_archivo)
            logger.info(f"Archivo leído correctamente. Contenido:\n{zpl_data[:200]}...")

            # Optimizar el contenido ZPL
            optimized_zpl = optimize_zpl(zpl_data, original_file_path=zpl_archivo)

            # Sugerir nombre de archivo para guardar
            directorio = os.path.dirname(zpl_archivo)
            nombre_sugerido = sugerir_nombre_archivo(directorio)
            pdf_file = seleccionar_ubicacion_guardado(directorio, nombre_sugerido)

            if pdf_file:
                # Guardar el ZPL optimizado en un archivo de texto
                guardar_zpl_optimizado(optimized_zpl, zpl_archivo)

                # Convertir el ZPL optimizado a PDF
                convert_zpl_to_pdf(optimized_zpl, pdf_file)

                # Actualizar el modelo de guardado
                actualizar_modelo_guardado(pdf_file)
            else:
                logger.warning("No se seleccionó ubicación para guardar el archivo.")
    except Exception as e:
        logger.error(f"Error al procesar el archivo {archivo}. Detalle del error: {e}")
        sys.exit(1)