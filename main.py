import os
import sys
from logger import logger
from menu import main as menu_main  # Importamos el main desde menu.py
from utils.file_manager import manejar_archivo_seleccionado  # Asegurarse de importar correctamente

if __name__ == "__main__":
    menu_main(manejar_archivo_seleccionado)