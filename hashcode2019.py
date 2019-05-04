import sys
import operator

import matplotlib.pyplot as plt

def sort_dic_value(d):
    for key, value in sorted(d.items(), key=lambda a: (-a[1][0])):
        yield key, value

def maxDictValue(d):
    return max(d.items(), key=operator.itemgetter(1))[0]

def vertiHorizHisto(lines):
    horizontales = {}
    verticales = []
    x = []
    for e in lines:
        tags = e[0][3:].split()
        tam = len(tags)
        numfoto = e[1]
        if e[0][0] == 'H':
            horizontales.update({numfoto : (tam, tags)})
            x.append(tam)
        else:
            verticales.append((numfoto, tam, tags))
    return (verticales, horizontales, x)

if __name__ == "__main__":
    #1 calcular moda
    #2 juntar fotos verticales en funcion de la moda
    #3 tener todas las fotos (horizontales verticales)
    #   como si fueran todas horizontales
    #4 Ordenar las fotos por numero de tags
    #5 Reordenar las fotos con el mismo numero de tags

    r = sys.argv[1]
    s = sys.argv[2]
    fichero = open(r,'r')
    fichero_salida = open(s, 'w+')
    nump = fichero.readline()
    cont = -1
    lines = []

    for line in fichero:
        cont += 1
        lines.append((line.rstrip('\n'), cont))

    (horizontales, verticales, histograma) = vertiHorizHisto(lines)
    plt.hist(histograma)
    print(max(histograma))
    plt.xticks(range(min(histograma), max(histograma)+1))
    plt.show()

    valmoda = 0
    if len(histograma) > 0:
        valmoda = maxDictValue(histograma)

    res = " \n"
    
    print(verticales)

    fichero_salida.write(res)
    fichero.close()
    fichero_salida.close()