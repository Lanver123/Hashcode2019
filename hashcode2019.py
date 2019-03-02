import sys
import operator

def sort_dic_value(d):
    for key, value in sorted(d.items(), key=lambda a: (-a[1][0])):
        yield key, value

def maxDictValue(d):
    return max(d.iteritems(), key=operator.itemgetter(1))[0]


if _name_ == "_main_":
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
    horizontales = {} #Format = {numfoto : (tam, tags)}
    verticales = []
    moda = {}
    for e in lines:
        tags = e[0][3:].split()
        tam = len(tags)
        numfoto = e[1]
        if e[0][0] == 'H':
            horizontales.update({numfoto : (tam, tags)})
            moda.setdefault(tam,0)
            moda[tam] += 1
        else:
            verticales.append((numfoto, tam, tags))
    valmoda = 0
    if len(moda) > 0:
        valmoda = maxDictValue(moda)

    dif = 0
    tamano = len(verticales)
    lonver = len(verticales)
    print(lonver)
    while tamano > 2:
        for vert1 in range(0, lonver - 2):
            if(isinstance(verticales[vert1], int)):
                continue
            ve1 = verticales[vert1]
            ve1 = set(ve1[2])
            for vert2 in range((vert1 + 1 ), (lonver - 1)):
                if (isinstance(verticales[vert2], int)):
                    continue
                ve2=verticales[vert2]
                ve2=set(ve2[2])
                union = ve1.union(ve2)
                lunion = len(union)
                if(abs(lunion - valmoda)== dif):
                    horizontales.update({(verticales[vert1][0],verticales[vert2][0]): (lunion, union)})
                    verticales[vert2] = 0 #Se consume
                    verticales[vert1] = 0
                    tamano -= 2
                    break
        dif += 1
    count = 0
    lista = list(sort_dic_value(horizontales))
    res = " \n"
    i=0
    while(i < len(lista)-2):
        foto1 = lista[1]
        j = i+1
        while(j < len(lista)-1):
            foto2=lista[2]
            minimo = min(foto1[1][0],foto2[1][0])
            if(len(set(foto1[1][1]).intersection(set(foto2[1][1])))== minimo/2):


        i+=1
    fichero_salida.write(res)
    fichero.close()
    fichero_salida.close()