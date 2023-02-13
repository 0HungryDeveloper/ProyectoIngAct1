from time import time
import logging
import re
import os
from bs4 import BeautifulSoup

# ! Importar BeatifulSoup desde la terminal con el siguiente comando ---> pip install beautifulsoup4

# * Crear el archivo log.
enrollment = 'PYTHONLOVERS.log'

# * Configuración para crear el archivo log.
logging.basicConfig(filename=enrollment, filemode='w', encoding='utf-8', level=logging.INFO)

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
    
    file_path = os.path.join(os.getcwd(),'CS13309_Archivos_HTML','Files', file_name + '.html')

    # Abrir y leer el archivo, ignoramos cualquier posible error y asignamos un alías.
    with open(file_path, "r", errors='ignore') as fileR:
        # Guardamos el resultado en un string para poder leerlo y modificarlo.
        text_html = fileR.read()

    # Se eliminan las etiquetas HTML.
    text_without_tags = remove_html_tags(text_html)

    # Buscamos y ordenamos las palabras aceptadas
    accepted_words = search_words_and_sort(text_without_tags)

    #Escribimos el resultado en los archivos
    with open(file_path, "w", errors='ignore') as fileW:
        fileW.write(str(accepted_words))

    # ! Fin de ejecución de la función.
    finish = time()
    execution_time = finish - start

    # * Información del tiempo que estará en el archivo log.
    logging.info(f"El archivo {file_name}.html tardo {execution_time:.4f} en abrir.")
    # Imprime por consola la misma información que el archivo log.
    print(f"El archivo {file_name}.html tardo {execution_time:.4f} en abrir.")

    # ! Sumar el tiempo que tardan en abrirse todos los archivos.
    global sum_total
    sum_total += execution_time


"""
    Remover etiquetas HTML.
    @param text: Archivo HTML convertido a string.
    @return Texto sin etiquetas HTML.
"""

# * Funcion para remover todos los tags de html usando BeatifulSoup
def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

# * Funcion para obtener de un texto unicamente palabras en español y en ingles.
def find_words(text):
    # Creamos un patron para aceptar unicamente esos simbolos
    patron = r'[a-zA-Z]+[a-zA-Z]|[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]'
    words = re.findall(patron, text)
    return words

# * Funcion para buscar y ordenar cada palabra de un texto
def search_words_and_sort(text):
    global file_words
    for found_word in find_words(text):
        if found_word:
            # Si se encuentra una palabra de la funcion find_words la agregamos a la lista cada palabra
            file_words.append(found_word.split()[0])


# Se recorre la lista de arhcivos.
for i in range(2, 504):
    # Se aplica un formato al string para agregar un cero o dos dependiendo del nombre
    # del archivo.
    print(open_file("%03d" % i))

# ! Se termina de ejecutar el programa.
final_time = time()
elapsed_time = final_time - start_time
file_words.sort()

# * Información del tiempo para crear el archivo log
logging.info(f"El tiempo total de los procesos fue de {sum_total:.4f} segundos")
print(f"El tiempo total de los procesos fue de  {sum_total:.4f} segundos")
logging.info(f"El proceso tardó en ejecutarse {elapsed_time:.2f} segundos")
print(f"El proceso tardó en ejecutarse {elapsed_time:.2f} segundos")
# print(f"Lista de todas las palabras ordenadas: {str(file_words)}")
accepted_file_words_path = os.path.join(os.getcwd(), 'Lista.txt')
with open(accepted_file_words_path, "w") as f:
    for word in file_words:
        f.write(word + '\n')
