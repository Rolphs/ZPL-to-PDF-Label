import os
import zipfile
from logger import logger

def leer_archivo_zpl(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def extraer_archivos_zip(zip_file_path):
    zpl_files = []
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        extract_dir = os.path.dirname(zip_file_path)
        zip_ref.extractall(extract_dir)
        for file_name in zip_ref.namelist():
            if file_name.lower().endswith(('.zpl', '.txt')):
                zpl_files.append(os.path.join(extract_dir, file_name))
    logger.info(f"Archivos extraídos: {zpl_files}")
    return zpl_files

def guardar_zpl_optimizado(zpl_data, original_file_path):
    optimized_file_path = original_file_path.replace('.txt', '_optimized.txt').replace('.zpl', '_optimized.zpl')
    with open(optimized_file_path, 'w') as file:
        file.write(zpl_data)
    logger.info(f"ZPL optimizado guardado en: {optimized_file_path}")

def manejar_archivo_seleccionado(archivo, seleccionar_ubicacion_guardado, optimize_zpl, convert_zpl_to_pdf, sugerir_nombre_archivo, actualizar_modelo_guardado):
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
        raise e