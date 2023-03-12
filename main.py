from time import time
import logging
import re
import os
# ! Importar BeatifulSoup desde la terminal con el siguiente comando ---> pip install beautifulsoup4
from bs4 import BeautifulSoup
from collections import Counter


# * Crear el archivo log.
enrollment = 'PYTHONLOVERS.log'

# * Configuración para crear el archivo log.
logging.basicConfig(filename=enrollment, filemode='w', encoding='utf-8', level=logging.INFO)

# ! Se comienza a correr el tiempo de ejecucción del programa.
start_time = time()

# * Tiempo total que tardan en abrirse todos los archivos.
sum_total = 0

file_words = []

# diccionario para almacenar el recuento de palabras en todos los archivos
word_count_all = {}

# * Abrir archivos HTML.
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

    # Cuenta las palabras del texto y guardarlas en un diccionario.
    count_words_save(text_without_tags)
    global word_count_all
    word_count_all = dict(sorted(word_count_all.items()))

    # ! Fin de ejecución de la función.
    finish = time()
    execution_time = finish - start

    # * Información del tiempo que estará en el archivo log.
    logging.info(f"El archivo {file_name}.html tardo {execution_time:.4f} en abrir.")
    # Imprime por consola la misma información que el archivo log.
    # print(f"El archivo {file_name}.html tardo {execution_time:.4f} en abrir.")

    # ! Sumar el tiempo que tardan en abrirse todos los archivos.
    global sum_total
    sum_total += execution_time

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

# * Funcion para contar las palabras del documento y agregarlas al archivo.
def count_words_save(text):

    # Buscamos y ordenamos las palabras aceptadas
    tokens = find_words(text)

    # Contamos cuántas veces aparece cada palabra
    word_count = Counter(tokens)

    # agregar el recuento de palabras al diccionario global
    for word, count in word_count.items():
        if word in word_count_all:
            word_count_all[word.lower()] += count
        else:
            word_count_all[word.lower()] = count

    # guardar los resultados en un archivo de texto
    with open("resultados.txt", "w") as output_file:
        for word, count in word_count_all.items():
            count_file = count_word_on_file(word)
            output_file.write(f"{word}\t{count}\t{count_file}\n")

def count_word_on_file(word_to_count):
    counter = 0
    files = [
        'simple', 'medium', 'hard'
    ]

    file_path = os.path.join(os.getcwd(), 'CS13309_Archivos_HTML', 'Files') + os.sep

    for file in files:
        with open(file_path + file + '.html', 'r', errors='ignore') as fileR:
        # Guardamos el resultado en un string para poder leerlo y modificarlo.
            text_html = fileR.read()

        text = remove_html_tags(text_html)
        text_lower = " ".join(word.lower() for word in text.split())

        with open(file_path + file, 'w') as file_writer:
            file_writer.write(text_lower)

    for file in files:
        with open(file_path + file, 'r') as f:
            text = f.read()
            # Buscamos la palabra exacta en el archivo usando una expresión regular
            matches = re.findall(rf'\b{word_to_count}\b', text)
            if matches:
                counter += 1

    return counter

def clean_html_files():

    file_path = os.path.join(os.getcwd(), 'CS13309_Archivos_HTML', 'Files') + os.sep
    for i in range(2,504):
        with open(file_path + "%03d"%i + '.html', 'r', errors='ignore') as fileR:
        # Guardamos el resultado en un string para poder leerlo y modificarlo.
            text_html = fileR.read()

        text = remove_html_tags(text_html)
        text_lower = " ".join(word.lower() for word in text.split())

        with open(file_path + "%03d"%i + '.html', 'w') as file_writer:
            file_writer.write(text_lower)

if __name__ == '__main__':
    # clean_html_files()
    # Se recorre la lista de arhcivos.
    for i in range(2, 504):
        # Se aplica un formato al string para agregar un cero o dos dependiendo del nombre
        # del archivo.
        open_file("%03d" % i)

    open_file('simple')
    open_file('medium')
    open_file('hard')

    # ! Se termina de ejecutar el programa.
    # final_time = time()
    # elapsed_time = final_time - start_time
    # file_words.sort()

    # # * Información del tiempo para crear el archivo log
    # logging.info(f"El tiempo total de los procesos fue de {sum_total:.4f} segundos")
    # print(f"El tiempo total de los procesos fue de  {sum_total:.4f} segundos")
    # logging.info(f"El proceso tardó en ejecutarse {elapsed_time:.2f} segundos")
    # print(f"El proceso tardó en ejecutarse {elapsed_time:.2f} segundos")
