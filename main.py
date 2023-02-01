from time import time
import logging
import re
import os

# * Crear el archivo log.
# * Dependiendo del sistema operativo es donde se va a crear.
enrollment = 'D:\\Descargas\\PYTHONLOVERS.log' if os.name == 'nt' else 'PYTHONLOVERS.log'

# * Configuración para crear el archivo log.
logging.basicConfig(filename=enrollment, filemode='w' , encoding='utf-8', level=logging.INFO)

# ! Se comienza a correr el tiempo de ejecucción del programa.
start_time = time()

# * Tiempo total que tardan en abrirse todos los archivos.
sum_total = 0

"""
    Abrir archivos HTML.
    @param file_name: Nombre del archivo HTML.
"""
def open_file(file_name: str):

    # ! Se comienza a correr el tiempo de ejecución de la función.
    start = time()

    # * Windows version
    if(os.name == 'nt'):
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
    else:
        # * IOS version
        # Abrir y leer el archivo, ignoramos cualquier posible error y asignamos un alías.
        with open("./Files/" + file_name + ".html", "r", errors='ignore') as fileR:
            # Guardamos el resultado en un string para poder leerlo y modificarlo.
            text_html = fileR.read()
            #Quitar el gato de abajo si quieres ver lo que imprime del remove en consola, si no, no
            #print(remove_html_tags(text_html))
            with open("./Files/" + file_name + ".html", "w", errors='ignore') as fileW:
                # Se eliminan las etiquetas HTML.
                fileW.write(remove_html_tags(text_html))

    # ! Fin de ejecución de la función.
    finish = time()
    execution_time = finish - start

    # * Información del tiempo que estará en el archivo log.
    logging.info("El archivo " + file_name + ".html tardo " + "{:.4f}".format(execution_time) + " en abrir.")
    # Imprime por consola la misma información que el archivo log.
    print("El archivo " + file_name + ".html tardo " + "{:.4f}".format(execution_time) + " en abrir.")

    # ! Sumar el tiempo que tardan en abrirse todos los archivos.
    global sum_total
    sum_total += execution_time


"""
    Remover etiquetas HTML.
    @param text: Archivo HTML convertido a string.
    @return Texto sin etiquetas HTML.
"""
def remove_html_tags(text):
    CLEANR = re.compile(r'<[^>]+>')
    return CLEANR.sub('', text)

# Se recorre la lista de arhcivos.
for i in range(2,504):
    # Se aplica un formato al string para agregar un cero o dos dependiendo del nombre
    # del archivo.
    print(open_file("%03d" % i))

# ! Se termina de ejecutar el programa.
final_time = time()
elapsed_time = final_time - start_time

# * Información del tiempo para crear el archivo log.
logging.info("El tiempo total de los procesos fue de  " + "{:.4f}".format(sum_total) + " segundos")
print("El tiempo total de los procesos fue de  " + "{:.4f}".format(sum_total) + " segundos")
logging.info("El proceso tardó en ejecutarse " + "{:.2f}".format(elapsed_time) + " segundos")
print("El proceso tardó en ejecutarse " + "{:.2f}".format(elapsed_time) + " segundos")