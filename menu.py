import tkinter as tk
from tkinter import filedialog, messagebox
from utils.file_manager import manejar_archivo_seleccionado
from logger import logger

class ZPLToPDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ZPL to PDF Converter")

        # Configurar el tamaño de la ventana: más alta y permitir redimensionar
        self.root.geometry("500x600")  # Ajustado para más altura
        self.root.resizable(True, True)

        # Lista para guardar los archivos seleccionados
        self.archivos_seleccionados = []

        # Crear los elementos de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta de instrucción
        self.instruction_label = tk.Label(self.root, text="Selecciona uno o más archivos ZPL, TXT o ZIP")
        self.instruction_label.pack(pady=10)

        # Botón para seleccionar archivos
        self.select_button = tk.Button(self.root, text="Seleccionar Archivos", command=self.seleccionar_archivos)
        self.select_button.pack(pady=10)

        # Lista de archivos seleccionados
        self.archivos_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, width=60, height=20)  # Aumentado para más visibilidad
        self.archivos_listbox.pack(pady=10)

        # Botón para procesar archivos
        self.process_button = tk.Button(self.root, text="Procesar y Guardar", command=self.procesar_archivos)
        self.process_button.pack(pady=10)

        # Botón para salir
        self.exit_button = tk.Button(self.root, text="Salir", command=self.root.quit)
        self.exit_button.pack(pady=10)

    def seleccionar_archivos(self):
        filetypes = [("Archivos ZPL, TXT o ZIP", "*.txt *.zpl *.zip")]
        archivos = filedialog.askopenfilenames(title="Selecciona uno o más archivos", filetypes=filetypes)
        if archivos:
            self.archivos_seleccionados = list(archivos)
            self.archivos_listbox.delete(0, tk.END)  # Limpiar la lista antes de agregar nuevos elementos
            for archivo in archivos:
                self.archivos_listbox.insert(tk.END, archivo)
            self.instruction_label.config(text=f"Seleccionados: {len(self.archivos_seleccionados)} archivos")

    def procesar_archivos(self):
        if not self.archivos_seleccionados:
            messagebox.showwarning("Advertencia", "Por favor selecciona al menos un archivo.")
            return

        try:
            for archivo in self.archivos_seleccionados:
                manejar_archivo_seleccionado(archivo)

            messagebox.showinfo("Éxito", "Archivos procesados y guardados exitosamente.")
        except Exception as e:
            logger.error(f"Error al procesar los archivos: {e}")
            messagebox.showerror("Error", f"Error al procesar los archivos: {e}")


def seleccionar_ubicacion_guardado(directorio, nombre_sugerido):
    return filedialog.asksaveasfilename(initialdir=directorio, initialfile=nombre_sugerido, defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

def main():
    root = tk.Tk()
    app = ZPLToPDFApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()