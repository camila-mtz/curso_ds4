# Calculo de coordenadas de lineas
import funciones

def main():
    m = 2
    b = 3
    X = [x for x in range(1,11)]
    Y = [funciones.calcular_y(x, m, b) for x in X]
    print(f'Enteros:')
    coordenadas_enteros = zip(X,Y)
    print(coordenadas_enteros)

if __name__ == '__main__':
    main()