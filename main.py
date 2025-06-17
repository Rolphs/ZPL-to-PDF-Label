from logger import logger
from menu import main as menu_main  # Importamos el main desde menu.py
from utils.model_manager import mostrar_etiquetas_generadas

def main():
    try:
        menu_main()  # Llama a la función main del menú sin argumentos
    except Exception as e:
        logger.error(f"Error en la ejecución del programa: {e}")
    finally:
        mostrar_etiquetas_generadas()

if __name__ == "__main__":
    main()
