
import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta = 'C:\\Users\\HP\\Desktop\\PYTHON\\dia9\\practica\\Extraccion\\Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'

hoy = datetime.date.today()
nros_encontrados = []
archivos_encontrados = []

def buscar_numero(archivo,patron):

    '''
    buscara los numeros de serie en un determinado archivo
    '''

    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron,texto) :
        return re.search(patron,texto)
    else:
        return ''

def crear_listas():

    '''
    crear lista con los numeros de serie que encuentre y con los nombres de archivos que contengan
    esos numeros de seria
    '''

    for carpeta,subcarpeta,archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta,a), mi_patron)
            if resultado != '':
                nros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())


def mostar_todo():
    indice = 0
    print('-'*50)
    print(f'fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')

    for a in archivos_encontrados:
        print(f'{a}\t{nros_encontrados[indice]}')
        indice += 1

    print('\n')
    print(f'Numero encontrados: {len(nros_encontrados)}')
    fin = time.time()
    duracion = fin-indice
    print(f'Duracion de la busqueda: {math.ceil(duracion)} segundos')
    print('-'*50)


crear_listas()
mostar_todo()


