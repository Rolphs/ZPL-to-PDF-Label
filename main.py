import os
import sys
from logger import logger
from menu import seleccionar_ubicacion_guardado, main as menu_main  # Importamos desde menu.py
from optimize import optimize_zpl
from generate import convert_zpl_to_pdf
from utils.file_manager import leer_archivo_zpl, extraer_archivos_zip, guardar_zpl_optimizado
from utils.model_manager import sugerir_nombre_archivo, actualizar_modelo_guardado

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

if __name__ == "__main__":
    menu_main(manejar_archivo_seleccionado)