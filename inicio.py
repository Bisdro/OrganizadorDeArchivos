import os
from tkinter import *
from tkinter import filedialog
import zipfile
from tkinter.filedialog import *
def obtenerArchivos(ruta,extension):
    #creamos una lista vacia y le asigamos los archivos que terminen con la extension indicada 
    # la funcion retorna una lista con los archivos + su ruta 
    #
    #
    listaDearchivos = []
    for file in os.listdir(ruta):
     if file.endswith(extension):
         listaDearchivos.append(os.path.join(ruta,file)) # se puede cambiar el parametro a solo  file para obtener el nombre del archivo sin su ruta
    return listaDearchivos
    
def descomprimirArchivos():
    try:
         archivoZip = zipfile.ZipFile(filedialog.askopenfilename(),"r")
         rutaDeDesomprimir = filedialog.askdirectory()
    
         archivoZip.extractall(rutaDeDesomprimir)
         archivoZip.close()
    except:
        print("ha ocurrido un error!")

def crearCarpeta(rutaCarpeta, nombre):
    try:
        os.mkdir(rutaCarpeta+"\\"+nombre)
        print("carpeta creada con exito")
    except:
        print("no  se a podido crear la carpeta")

    
def obtenerCarpetas(ruta):
    listarCarpetas =[]
    for file in os.listdir(ruta):
        if os.path.isdir(os.path.join(ruta,file)):
            listarCarpetas.append(file)
    
    return listarCarpetas
root = Tk()
root.title("Organizador de archivos v0.01")
btnElegirCarpeta = Button(text="Elegir archivo",command=descomprimirArchivos).pack()
root.mainloop()
#print(obtenerCarpetas("C:\\Users\\Programacion\\Desktop\\Nuevacarpeta"))
# descomprimirArhivos("C:\\Users\\Programacion\\Desktop\\Nuevacarpeta\\a.zip","C:\\Users\\Programacion\\Desktop\\Nuevacarpeta")
# print(obtenerArchivos("C:\\Users\\Programacion\\Desktop\\Nuevacarpeta",".jpg"))
# crearCarpeta("C:\\Users\\Programacion\\Desktop\\Nuevacarpeta", "carpeta nueva by python")
