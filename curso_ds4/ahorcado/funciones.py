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

if __name__ == '__main__':
    plantilla = carga_plantillas('plantilla')
    despliega_plantilla(plantilla,3)
    lista_oraciones = carga_archivo_texto('./curso_ds4/ahorcado/datos/pg15532.txt')
    print(lista_oraciones[110:115])
    texto = "".join(lista_oraciones[110:])
    print(texto[:100])