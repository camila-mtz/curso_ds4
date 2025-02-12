'''
Funciones auziliares del juego ahorcado
'''
import string
import unicodedata
from random import choice

def carga_archivo_texto(archivo:str)->list:
    '''
    Carga un archivo de texto y devuelve una lista con
    las oraciones del archivo
    '''
    with open(archivo, 'r',encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

def carga_plantillas(nombre_plantilla:str)->dict:
    '''Carga las platillas del juego  a partir de un archivo de texto'''    
    plantillas={}
    for i in range(6):
        plantillas[i]= carga_archivo_texto(f'./curso_ds4/ahorcado/plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict, nivel:int):
    '''
    Despliega una plantilla del juego
    '''
    if nivel >=0 and nivel <=5:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon.rstrip())

def obten_palabras(lista:list)->list:
    '''
    Obtiene las palabras de un texto
    '''
    texto = ' '.join(lista[120:]) 
    palabras = texto.split()
    # Cobvertimos a minusculas
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    # Removemos signos de puntuacion y caracteres especiales
    set_palabras = {palabra.strip(string.punctuation) for palabra in set_palabras}
    # Removemos numeros, parentesis, corchetes y otros caracteres
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}
    # Removemos acentos
    set_palabras = {unicodedata.normalize('NFKD', palabra).encode('ascii', 'ignore').decode('ascii') for palabra in set_palabras}
    
    return list(set_palabras)

def adivina_letra(abc:dict, palabra:str, letras_adivinadas:set, turnos:int):
    '''
    Adivina una letra de una palabra
    '''
    palabra_oculta = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += "_"
    print(f'Tienes {turnos} turnos')
    print(f'La palabra es: {palabra}')
    print(f'El abecedario es: {abc}')
    letra = input('Ingresa una letra: ')
    letra = letra.lower()
    if len(letra) !=1 or letra not in abc:
        print('Ingresa una letra valida')
    else:
        if abc[letra] == "*":
            print('Ya ingresaste esa letra')
        else:
            abc[letra] = "*"
            if letra in palabra:
                letras_adivinadas.add(letra)
            else:
                turnos -= 1



if __name__ == '__main__':
    plantilla = carga_plantillas('plantilla')
    despliega_plantilla(plantilla,0)
    lista_oraciones = carga_archivo_texto('./curso_ds4/ahorcado/datos/pg15532.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    print(len(lista_palabras))
    p = choice(lista_palabras)
    print(p)
    abcedario = {letra:letra for letra in string.ascii_lowercase}
    letras_adivinadas = set()
    turnos = 5
    print(f"Tienes {turnos} turnos")
    adivina_letra(abcedario, p, letras_adivinadas, turnos)
    print(f"Tienes {turnos} tunros")
    adivina_letra(abcedario, p, letras_adivinadas, turnos)