from time import time
import logging
import re
import os

enrollment = 'D:\\Descargas\\PYTHONLOVERS.log' if os.name == 'nt' else 'PYTHONLOVERS.log'

logging.basicConfig(filename=enrollment, filemode='w' , encoding='utf-8', level=logging.INFO)
start_time = time()
sum_total = 0

def open_file(file_name: str):
    start = time()
    # !Windows version
    if(os.name == 'nt'):
        directory = "D:\Descargas\CS13309_Archivos_HTML"
        with open(directory + "/Files/" + file_name + ".html", "r", errors='ignore') as fileR:
            text_html = fileR.read()
            #Quitar el gato de abajo si quieres ver lo que imprime del remove en consola, si no, no
            #print(remove_html_tags(text_html))
            with open(directory + "/Files/" + file_name + ".html", "w", errors='ignore') as fileW:
                fileW.write(remove_html_tags(text_html))
                #print('-------------')

    else:
        # !IOS version
        with open("./Files/" + file_name + ".html", "r", errors='ignore') as fileR:
            text_html = fileR.read()
            #Quitar el gato de abajo si quieres ver lo que imprime del remove en consola, si no, no
            #print(remove_html_tags(text_html))
            with open("./Files/" + file_name + ".html", "w", errors='ignore') as fileW:
                fileW.write(remove_html_tags(text_html))
                #print('------')

    finish = time()
    execution_time = finish - start
    logging.info("El archivo " + file_name + ".html tardo " + "{:.4f}".format(execution_time) + " en abrir.")
    print("El archivo " + file_name + ".html tardo " + "{:.4f}".format(execution_time) + " en abrir.")
    global sum_total
    sum_total += execution_time

def remove_html_tags(text):
    CLEANR = re.compile(r'<[^>]+>')
    return CLEANR.sub('', text)

for i in range(2,504):
    print(open_file("%03d" % i))

final_time = time()
elapsed_time = final_time - start_time

logging.info("El tiempo total de los procesos fue de  " + "{:.4f}".format(sum_total) + " segundos")
print("El tiempo total de los procesos fue de  " + "{:.4f}".format(sum_total) + " segundos")
logging.info("El proceso tardó en ejecutarse " + "{:.2f}".format(elapsed_time) + " segundos")
print("El proceso tardó en ejecutarse " + "{:.2f}".format(elapsed_time) + " segundos")