from time import time

start_time = time()

def open_file(file_name: str):
    start = time()
    directory = "D:\Descargas\CS13309_Archivos_HTML" 
    open(directory + "/Files/" + file_name + ".html", "r")
    finish = time()
    execution_time = finish - start
    return "El archivo " + file_name + ".html tardo " + "{:.4f}".format(execution_time) + " en abrir."

for i in range(2,504):
    if (i < 10):
        print(open_file("00"+str(i)))
    elif(i < 100):
        print(open_file("0"+str(i)))
    else:
        print(open_file(str(i)))

final_time = time()
elapsed_time = final_time - start_time
print("El proceso tardó en ejecutarse " + "{:.2f}".format(elapsed_time) + " segundos")