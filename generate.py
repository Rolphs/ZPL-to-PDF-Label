import requests
import shutil
from logger import logger

def convert_zpl_to_pdf(zpl_data, pdf_output_path):
    try:
        # URL de la API de Labelary para la conversión de ZPL a PDF con 12dpmm (300 DPI)
        url = 'http://api.labelary.com/v1/printers/12dpmm/labels/4x6/0/'
        files = {'file': zpl_data}
        headers = {'Accept': 'application/pdf'}  # Solicitar un archivo PDF en la respuesta

        # Realizar la solicitud POST a la API
        response = requests.post(url, headers=headers, files=files, stream=True)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Decodificar el contenido de la respuesta
            response.raw.decode_content = True
            with open(pdf_output_path, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            logger.info(f"PDF guardado exitosamente en: {pdf_output_path}")
        else:
            logger.error(f"Error al convertir ZPL a PDF: {response.status_code}")
            logger.error(f"Detalles del error: {response.text}")
    except Exception as e:
        logger.error(f"Error durante la conversión de ZPL a PDF: {e}")
        raise