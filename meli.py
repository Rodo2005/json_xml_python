
'''
JSON [Pyhon]
Uso de la API pública de mercadolibre
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json
import requests
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes


prov = input('Ingrese la provincia para el reporte de alquileres, el nombre'
 'de la provincia siempre debe empezar con "MAYUSCULA": ')
min = int(input('Ingrese el valor minimo de alquiler: '))
max = int(input('Ingrese el valor maximo de alquiler: '))


url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20' + prov + '%20&limit=50'

def fetch_data():
    response = requests.get(url)
    contenido = response.json()
    resultados = contenido['results']
    filtro_1 = [{'precio': x['price'], 'condicion': x['condition']}
     for x in resultados if x.get('currency_id') == 'ARS']
    with open('alquileres.json', 'w') as alq:
        json.dump(filtro_1, alq, indent=0)
    return
    
def transform(min, max):
    
    with open('alquileres.json', 'r') as alq:
        alquileres = json.load(alq)
        filtro_1 = [x["precio"] for x in alquileres]
        entre_0 = [x for x in filtro_1 if x >= min and x <= max]
        menor_0 = [x for x in filtro_1 if x < min]
        mayor_0 = [x for x in filtro_1 if x > max]
        entre = len(entre_0)
        menor = len(menor_0)
        mayor = len(mayor_0)
        parametros = [{'entre': entre, 'menor': menor, 'mayor': mayor}]
        with open('parametros.json', 'w') as par:
            json.dump(parametros, par, indent=0)
        print('Menores que $', min, 'hay', menor, 'departamentos', 'entre $',
         min, 'y $', max, 'hay', entre, 'departamentos y mayor que $', max,
          'hay', mayor, 'departamentos.')
        print('')
        # print('')
        # entre_0 = [{'precio': x['precio'], 'condicion': x['condicion']}
        # for x in alquileres if min <= x.get('precio') <= max]
        # menor_0 = [{'precio': x['precio'], 'condicion': x['condicion']}
        # for x in alquileres if x.get('precio') < min]
        # mayor_0 = [{'precio': x['precio'], 'condicion': x['condicion']}
        # for x in alquileres if x.get('precio') > max]
        # entre = len(entre_0)
        # menor = len(menor_0)
        # mayor = len(mayor_0)
        # print('Menores que $', min, 'hay', menor, 'departamentos', 'entre $',
        #  min, 'y $', max, 'hay', entre, 'departamentos y mayor que $', max,
        #   'hay', mayor, 'departamentos.')
    return

    
def report():

    with open('parametros.json', 'r') as par:
        parametros = json.load(par)
    valores = [(x['entre'], x['menor'], x['mayor']) for x in parametros]
    maximo = str(max)
    minimo = str(min)
    claves = ('entre $' + minimo + 'y $' + maximo, 'menor a $' + minimo, 'mayor a $' + maximo)
    fig = plt.figure()
    fig.suptitle('Reporte de alquileres en ' + prov, fontsize=16)
    ax = fig.add_subplot()
    ax.set_facecolor('whitesmoke')
    explode = (0.1, 0.15, 0.2)
    ax.pie(valores, labels=claves, autopct='%1.1f%%', shadow=True, explode=explode)
    plt.show()

if __name__ == '__main__':
    fetch_data()
    transform(min, max)
    report()
