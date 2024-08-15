import os
import zipfile
from logger import logger
from tkinter import filedialog
from generate import convert_zpl_to_pdf
from utils.model_manager import sugerir_nombre_archivo, actualizar_modelo_guardado


def leer_archivo_zpl(ruta_archivo):
    """
    Lee el contenido de un archivo ZPL o TXT.

    :param ruta_archivo: Ruta del archivo a leer.
    :return: Contenido del archivo como una cadena de texto.
    """
    try:
        with open(ruta_archivo, 'r') as archivo:
            return archivo.read()
    except IOError as e:
        logger.error(f"Error al leer el archivo {ruta_archivo}: {e}")
        raise


def extraer_archivos_zip(ruta_zip):
    """
    Extrae archivos de un archivo ZIP y devuelve una lista de rutas a los archivos extraídos.

    :param ruta_zip: Ruta del archivo ZIP.
    :return: Lista de rutas de archivos extraídos.
    """
    extract_dir = os.path.splitext(ruta_zip)[0]
    try:
        with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
            return [os.path.join(extract_dir, name) for name in zip_ref.namelist()]
    except zipfile.BadZipFile as e:
        logger.error(f"El archivo ZIP está corrupto o no es válido: {e}")
        raise


def seleccionar_ubicacion_guardado(directorio, nombre_sugerido):
    """
    Muestra un diálogo para seleccionar la ubicación donde se guardará el archivo PDF.

    :param directorio: Directorio inicial sugerido para guardar.
    :param nombre_sugerido: Nombre de archivo sugerido.
    :return: Ruta completa del archivo seleccionado por el usuario.
    """
    archivo_guardado = filedialog.asksaveasfilename(
        initialdir=directorio,
        title="Guardar archivo como...",
        defaultextension=".pdf",
        initialfile=nombre_sugerido,
        filetypes=[("PDF files", "*.pdf")]
    )
    if not archivo_guardado:
        logger.info("El usuario canceló la selección de archivo.")
    return archivo_guardado


def procesar_y_guardar_pdf(zpl_data, zpl_archivo, pdf_file):
    """
    Realiza la conversión de ZPL a PDF y guarda el archivo generado.

    :param zpl_data: Contenido del archivo ZPL.
    :param zpl_archivo: Ruta del archivo ZPL.
    :param pdf_file: Ruta donde se guardará el archivo PDF.
    """
    try:
        convert_zpl_to_pdf(zpl_data, pdf_file)
        actualizar_modelo_guardado(pdf_file)
        logger.info(f"PDF guardado exitosamente en: {pdf_file}")
    except Exception as e:
        logger.error(f"Error al convertir y guardar el PDF para {zpl_archivo}: {e}")
        raise


def manejar_archivo_seleccionado(archivo):
    """
    Gestiona el proceso completo de lectura, conversión a PDF y guardado de un archivo ZPL/TXT.

    :param archivo: Ruta del archivo ZPL, TXT o ZIP seleccionado.
    """
    try:
        zpl_archivos = extraer_archivos_zip(archivo) if archivo.lower().endswith('.zip') else [archivo]

        for zpl_archivo in zpl_archivos:
            zpl_data = leer_archivo_zpl(zpl_archivo)
            logger.info(f"Archivo leído correctamente. Contenido:\n{zpl_data[:200]}...")

            directorio = os.path.dirname(zpl_archivo)
            nombre_sugerido = sugerir_nombre_archivo(directorio)
            pdf_file = seleccionar_ubicacion_guardado(directorio, nombre_sugerido)

            if pdf_file:
                procesar_y_guardar_pdf(zpl_data, zpl_archivo, pdf_file)
            else:
                logger.warning("No se seleccionó ubicación para guardar el archivo.")
    except Exception as e:
        logger.error(f"Error al procesar el archivo {archivo}. Detalle del error: {e}")
        sys.exit(1)