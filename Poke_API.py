#Ejercicio de Consumo de API REST CON POKE-API en PYTHON
from os import system
import requests

import matplotlib.pyplot as plot
import matplotlib.image as img

from PIL import Image
import urllib.request
import numpy


class Poke_API():
    def __init__(self):
        pass

    def menuInicio(self):
        system("cls")
        print ("Bienvenido a la Poké-API")
        poke = input("Ingresa el Nombre/ID del Pokémon que desas Buscar: ")

        respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke}") #Ya que la BD de Pokémon's es extensa el ultimo valor se lopregubtamos al usuario para que sea el el que decida que dato de Pokémon ver

        if respuesta.status_code == 200:

            #Convertimos la respuesta JSON en un diccionario
            datos = respuesta.json()

            sprite_url = datos['sprites']['front_default']

            if sprite_url:
                #Usamos urllib y PIL para descargar y leer la imagen
                with urllib.request.urlopen(sprite_url) as reponse:
                    imagen = Image.open(reponse)

                    #Le damos los colores Correctos a la Imagen
                    imagen = imagen.convert("RGBA")

                    #Convertimos la imagen en un arry de numpy
                    imagen_array = numpy.array(imagen)

                #Mostramos la Imagen con Matplotlib
                plot.title(datos['name'])
                imgplot = plot.imshow(imagen_array)
                plot.axis('off') #Oculta los ejes
                plot.show()
            else:
                print("El Pokémon no tiene Imagen asociada.")
        else:
            print("No se han encontrado datos.")
