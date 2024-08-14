import requests
import shutil
from logger import logger

def convert_zpl_to_pdf(zpl_data, output_pdf_path):
    """
    Convierte una cadena ZPL a un archivo PDF utilizando la API de Labelary.
    """
    logger.info(f"Enviando solicitud a http://api.labelary.com/v1/printers/12dpmm/labels/4x6/0/...")
    url = 'http://api.labelary.com/v1/printers/12dpmm/labels/4x6/0/'
    headers = {'Accept': 'application/pdf'}
    files = {'file': zpl_data}

    response = requests.post(url, headers=headers, files=files, stream=True)

    if response.status_code == 200:
        with open(output_pdf_path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        logger.info(f"PDF guardado exitosamente en: {output_pdf_path}")
    else:
        logger.error(f"Error al convertir ZPL a PDF: {response.status_code}")
        logger.error(f"Detalles del error: {response.text}")