'''
Programa principal del juego del ahorcado
'''
import os
import string
import unicodedata
import argparse
from random import choice
import funciones as fn

def main(archivo_texto:str, nombre_plantilla='plantilla'):
    '''
    Programa principal
    '''
    # Cargamos las plantillas
    plantillas = fn.carga_plantillas(nombre_plantilla)
    # Cargamos las oraciones
    oraciones = fn.carga_archivo_texto(archivo_texto)
    # Obtenemos las palabras
    palabras = fn.obten_palabras(oraciones)
    o = 5 # Oportunidades
    p = choice(palabras) # Elegimos una palabra al azar
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o > 0:
        fn.despliega_plantilla(plantillas, o)
        o = fn.adivina_letra(abcdario, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Felicidades, adivinaste la palabra ^_^')
            break
    fn.despliega_plantilla(plantillas, o)
    print(f'La palabra era: {p}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Juego del ahorcado')
    parser.add_argument('-a', '--archivo', help='Archivo de texto con palabras', default='./curso_ds4/ahorcado/datos/pg15532.txt')
    args = parser.parse_args()
    archivo = args.archivo
    if os.stat(archivo) == False:
        print('El archivo no existe')
        exit()
    main(archivo)