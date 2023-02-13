from time import time
import logging
import re
import os
from bs4 import BeautifulSoup

# * Crear el archivo log.
# * Dependiendo del sistema operativo es donde se va a crear.
enrollment = 'D:\\Descargas\\PYTHONLOVERS.log' if os.name == 'nt' else 'PYTHONLOVERS.log'

# * Configuración para crear el archivo log.
logging.basicConfig(filename=enrollment, filemode='w',
                    encoding='utf-8', level=logging.INFO)

# ! Se comienza a correr el tiempo de ejecucción del programa.
start_time = time()

# * Tiempo total que tardan en abrirse todos los archivos.
sum_total = 0

file_words = []

"""
    Abrir archivos HTML.
    @param file_name: Nombre del archivo HTML.
"""


def open_file(file_name: str):

    # ! Se comienza a correr el tiempo de ejecución de la función.
    start = time()

    # * Windows version
    if (os.name == 'nt'):
        # Ubicación del directorio.
        directory = "D:\Descargas\CS13309_Archivos_HTML"

        # Abrir y leer el archivo, ignoramos cualquier posible error y asignamos un alías.
        with open(directory + "/Files/" + file_name + ".html", "r", errors='ignore') as fileR:
            # Guardamos el resultado en un string para poder leerlo y modificarlo.
            text_html = fileR.read()
            # Quitar el gato de abajo si quieres ver lo que imprime del remove en consola, si no, no
            # print(remove_html_tags(text_html))
            with open(directory + "/Files/" + file_name + ".html", "w", errors='ignore') as fileW:
                # Se eliminan las etiquetas HTML.
                fileW.write(remove_html_tags(text_html))
                with open(directory + "/Files/" + file_name + ".html", "r", errors='ignore') as fileF:
                    new_text = fileF.read()
                    with open(directory + "/Files/" + file_name + ".html", "w", errors='ignore') as fileWr:
                        fileWr.write(str(search_words_sort(str(new_text))))

    else:
        # * IOS version
        # Abrir y leer el archivo, ignoramos cualquier posible error y asignamos un alías.
        with open("./Files/" + file_name + ".html", "r", errors='ignore') as fileR:
            # Guardamos el resultado en un string para poder leerlo y modificarlo.
            text_html = fileR.read()
            # Quitar el gato de abajo si quieres ver lo que imprime del remove en consola, si no, no
            # print(remove_html_tags(text_html))
            with open("./Files/" + file_name + ".html", "w", errors='ignore') as fileW:
                # Se eliminan las etiquetas HTML.
                fileW.write(remove_html_tags(text_html))
                with open("./Files/" + file_name + ".html", "r", errors='ignore') as fileF:
                    new_text = fileF.read()
                    with open("./Files/" + file_name + ".html", "w", errors='ignore') as fileWr:
                        fileWr.write(str(search_words_sort(str(new_text))))

    # ! Fin de ejecución de la función.
    finish = time()
    execution_time = finish - start

    # * Información del tiempo que estará en el archivo log.
    logging.info("El archivo " + file_name + ".html tardo " +
                 "{:.4f}".format(execution_time) + " en abrir.")
    # Imprime por consola la misma información que el archivo log.
    print("El archivo " + file_name + ".html tardo " +
          "{:.4f}".format(execution_time) + " en abrir.")

    # ! Sumar el tiempo que tardan en abrirse todos los archivos.
    global sum_total
    sum_total += execution_time


"""
    Remover etiquetas HTML.
    @param text: Archivo HTML convertido a string.
    @return Texto sin etiquetas HTML.
"""


def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def find_words(text):
    patron = r'[a-zA-Z]+[a-zA-Z]|[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]'
    words = re.findall(patron, text)
    return words


def search_words_sort(text):
    global file_words
    lines = find_words(text)
    for line in lines:
        if line:
            file_words.append(line.split()[0])

# Se recorre la lista de arhcivos.
for i in range(2, 504):
    # Se aplica un formato al string para agregar un cero o dos dependiendo del nombre
    # del archivo.
    print(open_file("%03d" % i))

# ! Se termina de ejecutar el programa.
final_time = time()
elapsed_time = final_time - start_time
file_words.sort()

# * Información del tiempo para crear el archivo log.
logging.info("El tiempo total de los procesos fue de  " +
             "{:.4f}".format(sum_total) + " segundos")
print("El tiempo total de los procesos fue de  " +
      "{:.4f}".format(sum_total) + " segundos")
logging.info("El proceso tardó en ejecutarse " +
             "{:.2f}".format(elapsed_time) + " segundos")
print("El proceso tardó en ejecutarse " +
      "{:.2f}".format(elapsed_time) + " segundos")
print("Lista de todas las palabras ordenadas: " + str(file_words))
with open("D:\\Descargas\\Lista.txt", "w") as f:
    for word in file_words:   
        f.write(word + '\n')

