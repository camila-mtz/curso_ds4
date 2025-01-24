# Archivo con todas las funciones necesarias para la aplicacion linea
def calcular_y(x, m, b):
    '''
    Calcula el valor de y en una línea recta
    x: valor de x
    m: pendiente
    b: intersección en y
    regresa el valor de y
    '''
    return (m * x) + b

def test_linea():
    '''
    Comprobamos calcular_y
    '''
    return calcular_y(0,2,3)

if __name__ == '__main__':
    if test_linea() == 3:
        print('Todo bien')
    else:
        print('Algo salió mal')