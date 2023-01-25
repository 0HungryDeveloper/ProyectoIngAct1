from time import time
import logging

enrollment = 'al02841065.log'
logging.basicConfig(filename=enrollment, encoding='utf-8', level=logging.INFO)
start_time = time()

def open_file(file_name: str):
    start = time()
    # !Windows version
    # directory = "D:\Descargas\CS13309_Archivos_HTML"
    # open(directory + "/Files/" + file_name + ".html", "r")
    # !IOS version
    open("./Files/" + file_name + ".html", "r")
    finish = time()
    execution_time = finish - start
    logging.info("El archivo " + file_name + ".html tardo " + "{:.4f}".format(execution_time) + " en abrir.")

for i in range(2,504):
    if (i < 10):
        print(open_file("00"+str(i)))
    elif(i < 100):
        print(open_file("0"+str(i)))
    else:
        print(open_file(str(i)))

final_time = time()
elapsed_time = final_time - start_time
logging.info("El proceso tardó en ejecutarse " + "{:.2f}".format(elapsed_time) + " segundos")