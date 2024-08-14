Aquí te dejo un borrador del `README.md` que detalla todo lo que hemos hecho y los pasos necesarios para usar el proyecto. Este documento está diseñado para proporcionar una guía completa para cualquier persona que quiera utilizar o contribuir al proyecto.

---

# ZPL to PDF Converter

## Descripción

Este proyecto es una herramienta para convertir archivos de etiquetas en formato ZPL a archivos PDF. Además de la conversión, la herramienta optimiza las etiquetas ZPL para asegurarse de que se ajusten correctamente a un formato de etiqueta de 4x6 pulgadas con una resolución de 300 DPI. La herramienta también proporciona una interfaz gráfica de usuario (GUI) que permite a los usuarios seleccionar, procesar y guardar archivos ZPL, TXT o ZIP de forma intuitiva.

## Características

- **Conversión de ZPL a PDF**: Convierte etiquetas en formato ZPL a archivos PDF utilizables.
- **Optimización de etiquetas**: Ajusta y optimiza las posiciones de los elementos ZPL para asegurar que se impriman correctamente en una etiqueta de 4x6 pulgadas.
- **Interfaz gráfica**: GUI fácil de usar construida con `Tkinter`, que permite seleccionar archivos y configurar opciones de guardado.
- **Soporte para múltiples archivos**: Procesa uno o varios archivos ZPL, TXT o ZIP.
- **Aprendizaje no supervisado básico**: El programa sugiere nombres de archivos basados en patrones de guardado anteriores y mejora con el tiempo.

## Requisitos del Sistema

- **Python 3.9+**
- Paquetes Python requeridos (pueden ser instalados con `pip`):

  ```sh
  pip install -r requirements.txt
  ```

  El archivo `requirements.txt` debería contener:

  ```
  requests
  easygui
  tkinter
  ```

## Estructura del Proyecto

```
zpl_to_pdf/
│
├── main.py
├── menu.py
├── generate.py
├── optimize.py
├── utils/
│   ├── file_manager.py
│   ├── model_manager.py
├── logger.py
├── README.md
└── icon.icns
```

### Archivos y Directorios Clave

- **main.py**: Archivo principal que inicia la aplicación y maneja la lógica principal.
- **menu.py**: Gestiona la interfaz gráfica y la interacción del usuario.
- **generate.py**: Gestiona la conversión de ZPL a PDF utilizando la API de Labelary.
- **optimize.py**: Optimiza los archivos ZPL para que se ajusten correctamente a las etiquetas de 4x6 pulgadas.
- **utils/file_manager.py**: Contiene funciones para la gestión de archivos, como la lectura de archivos ZPL y la extracción de ZIP.
- **utils/model_manager.py**: Implementa el modelo de aprendizaje no supervisado para sugerir nombres de archivos.
- **logger.py**: Configura y gestiona el registro de eventos (logging) en la aplicación.
- **icon.icns**: Icono utilizado en la GUI de la aplicación.

## Instalación y Ejecución

### 1. Clonar el repositorio

```sh
git clone https://github.com/tuusuario/zpl_to_pdf.git
cd zpl_to_pdf
```

### 2. Instalar dependencias

```sh
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación

```sh
python main.py
```

## Compilación a un Ejecutable

### En macOS

Puedes compilar el proyecto en un ejecutable `.app` utilizando `PyInstaller`:

```sh
pyinstaller --onefile --windowed --icon=icon.icns main.py
```

### Cambiar el Icono de la Aplicación

El icono de la aplicación está configurado en `icon.icns`. Puedes cambiarlo por cualquier icono que desees utilizando el comando anterior.

## Uso de la Aplicación

1. **Seleccionar Archivos**: Puedes seleccionar uno o varios archivos `.txt`, `.zpl` o `.zip` desde la interfaz gráfica.
2. **Optimización y Conversión**: La aplicación optimizará automáticamente el contenido ZPL y lo convertirá a PDF.
3. **Guardar Archivos**: La aplicación sugiere un nombre para el archivo de salida y permite seleccionar el directorio donde guardar el PDF.
4. **Aprendizaje del Sistema**: Con cada archivo guardado, el sistema aprende y mejora las sugerencias de nombres y ubicaciones de guardado.

## Notas Importantes

- **Problemas conocidos**: Si los archivos ZPL no se optimizan correctamente, revisa la configuración de DPI y asegúrate de que los archivos ZPL originales no contengan errores que puedan dificultar la conversión.
- **Errores de importación circular**: Se resolvieron los errores de importación circular estructurando adecuadamente el flujo de datos entre los diferentes módulos. Si encuentras problemas similares, revisa las importaciones.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un error o tienes una mejora, no dudes en crear un `pull request` o abrir un `issue`.

## Créditos

Este proyecto fue desarrollado con el objetivo de facilitar la gestión de etiquetas ZPL y su conversión a PDF. Agradecimientos especiales a Raúl Mercado por su colaboración y dedicación en la creación de este proyecto.
