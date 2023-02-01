from time import time
import logging

enrollment = 'PYTHONLOVERS.log' # log file
logging.basicConfig(filename=enrollment, encoding='utf-8', level=logging.INFO)
start_time = time()
sum_total = 0

def open_file(file_name: str):
    start = time()
    # !Windows version
    directory = "D:\Descargas\CS13309_Archivos_HTML"
    open(directory + "/Files/" + file_name + ".html", "r")
    # !IOS version
    #open("./Files/" + file_name + ".html", "r")
    finish = time()
    execution_time = finish - start
    logging.info("El archivo " + file_name + ".html tardo " + "{:.4f}".format(execution_time) + " en abrir.")
    print("El archivo " + file_name + ".html tardo " + "{:.4f}".format(execution_time) + " en abrir.")
    global sum_total
    sum_total += execution_time

for i in range(2,504):
    print(open_file("%03d" % i))

final_time = time()
elapsed_time = final_time - start_time

logging.info("El tiempo total de los procesos fue de  " + "{:.4f}".format(sum_total) + " segundos")
print("El tiempo total de los procesos fue de  " + "{:.4f}".format(sum_total) + " segundos")
logging.info("El proceso tardó en ejecutarse " + "{:.2f}".format(elapsed_time) + " segundos")
print("El proceso tardó en ejecutarse " + "{:.2f}".format(elapsed_time) + " segundos")