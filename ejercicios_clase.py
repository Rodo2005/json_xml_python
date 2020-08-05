#!/usr/bin/env python
'''
JSON XML [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.axes


def ej1():
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado

    datos_personales = {
                        "nombre": "Rodolfo",
                        "Apellido": "Colombo",
                        "DNI:": 15177893,
                        "ropa": [
                            {
                            "prenda": "remera", "cantidad": 23
                            },
                            {
                            "prenda": "pantalones", "cantidad": 9
                            },
                            {
                            "prenda": "zapatillas", "cantidad": 8
                            },
                            {
                            "prenda": "medias", "cantidad": 12
                            }
                            ] 
                       }
    json_datos = json.dumps(datos_personales, indent=4)

    with open ("datos_personales.json", "w")  as archivo_writer:
        json.dump(json_datos, archivo_writer)
        print(json_datos)
    

    #pass


def ej2():
    # JSON Deserialize
    # Basado en el ejercicio anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en el ej1

    with open ('datos_personales', 'r') as jsonfile:
        current_data = json.load(jsonfile)
    string_data = json.dumps(current_data, indent=4)
    print(string_data)

    
    pass


def ej3():
    # Ejercicio de XML
    # Basado en la estructura de datos del ejercicio 1,
    # crear a mano un archivo ".xml" y generar una estructura
    # lo más parecida al ejercicio 1.
    # El objectivo es que armen un archivo XML al menos
    # una vez para que entiendan como funciona.

    datos_personales.xml
    

    pass


def ej4():
    # XML Parser
    # Tomar el archivo realizado en el punto anterior
    # e iterar todas las tags del archivo e imprimirlas
    # en pantalla tal como se realizó en el ejemplo de clase.
    # El objectivo es que comprueben que el archivo se realizó
    # correctamente, si la momento de llamar al ElementTree
    # Python lanza algún error, es porque hay problemas en el archivo.
    # Preseten atención al número de fila y al mensaje de error
    # para entender que puede estar mal en el archivo.

    tree = ET.parse('datos_personales.xml')
    root = tree.getroot()
    for child in root:
        print('tag:', child.tag, 'attr:', child.attrib, 'text:', child.text)
        for child2 in child:
            print('tag:', child2.tag, 'attr:', child2.attrib, 'text:', child2.text)
            for child3 in child2:
                print('tag:', child3.tag, 'attr:', child3.attrib, 'text:', child3.text)
    print('')
    pass


def ej5():
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general.
    # Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    # De cada usuario en el total de las 200 entradas contar cuantos títulos
    # completó cada usuario (de los 10 posibles) y armar
    # un gráfico de torta resumiendo la información.

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de torta.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.
    from collections import Counter
    response = requests.get(url)
    if response.status_code == 200:
        contenido = response.json()

    filter_data1 = [{'usuario': x['userId'], 'titulo': x['title'], 'certificado': x['completed']} for x in contenido if x.get('completed') is True]
    #filter_data2 = [(x['usuario']) for x in filter_data1]
    contador = Counter([(x['usuario']) for x in filter_data1])
    #  Imprimir los datos en consola
    for i in contador:
        print('El usuario', i, 'obtuvo', contador[i], 'titulos')

    #  Imprimir datos en grafico con dos ejes de coordenadas
    x = [i for i in contador]
    y = [contador[i] for i in contador]
    y_min = min(y)

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(x, y, c='cyan')
    ax.set_xlim(0, 10)
    ax.set_ylim(y_min, 12)
    ax.grid()
    ax.set_title('Titulos')
    plt.show()

    #  Imprimir los datos en grafico de torta
    fig = plt.figure()
    fig.suptitle('Usuarios / Titulos', fontsize=16)
    ax = fig.add_subplot()
    explode = (0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ax.pie(y, labels=x, autopct='%1.1f%%', shadow=True, startangle=343, explode=explode)
    ax.axis('equal')
    ax.set_title('Titulos')
    plt.show()

    print('')


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
