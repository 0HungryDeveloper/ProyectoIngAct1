import time
from math import e

def open_file(file_name: str):
    start = time.time()
    open("./Files/" + file_name + ".html", "r")
    finish = time.time()
    execution_time = finish - start
    return "El archivo " + file_name + ".html tardo " + "{:.2f}".format(e**execution_time) + " en abrir."

for i in range(2,504):
    if (i < 10):
        print(open_file("00"+str(i)))
    elif(i < 100):
        print(open_file("0"+str(i)))
    else:
        print(open_file(str(i)))