#Ejercicio de Consumo de API REST CON POKE-API en PYTHON
from os import system
import requests
import os

import matplotlib.pyplot as plot
import matplotlib.image as img

from PIL import Image
import urllib.request
import numpy

from beautifultable import BeautifulTable

class Poke_API():
    def __init__(self):
        pass

    def menuInicio(self):
        global respuesta
        while True:
            system("cls")
            print ("Bienvenido a la Poké-API")
            poke = input("Ingresa el Nombre/ID del Pokémon que desas Buscar: ")
            try:
                respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke}") #Ya que la BD de Pokémon's es extensa el ultimo valor se lopregubtamos al usuario para que sea el el que decida que dato de Pokémon ver
                if respuesta.status_code == 200:
                    print("Pokemon encontrado!")
                    self.menuSeleccion()
                elif poke == 0:
                    system("cls")
                    print("Adios...")
                    os._exit(1)
                else:
                    system("cls")
                    print("No se han encontrado datos...")
                    system("pause")            
            except Exception as e:
                system("cls")
                print(f"Error: {e}")
                system("pause")

    def menuSeleccion(self):
        system("cls")
        print("=== MENU DE SELECCION ===")
        print(" 1 ---> PokeDex          ")
        print(" 2 ---> PokeImagen       ")
        print(" 3 ---> Volver Atras     ")
        opc = int(input("Seleccione una Opcion: "))
        try:
            if opc == 1:
                self.pokeDex()
            elif opc == 2:
                self.pokeImagen()
            elif opc == 3:
                self.menuInicio()
            else:
                print("Opccion Incorrecta!")
        except Exception as e:
            print(f"Error: {e}")

    def pokeDex(self):
        try:
            system("cls")
            # Convertimos la respuesta JSON en un diccionario
            datos = respuesta.json()

            # Creamos la tabla para mostrar datos
            tabla = BeautifulTable()
            tabla.columns.header = ["ID", "NOMBRE", "ALTURA", "PESO", "HABILIDAD","TIPO"]

            id_pokemon = datos.get("id", "")
            nombre = datos.get("name", "")
            altura = datos.get("height", "")
            peso = datos.get("weight", "")
            habilidades = ", ".join([item["ability"]["name"] for item in datos.get("abilities", [])])
            tipos = ", ".join([item["type"]["name"] for item in datos.get("types", [])])

            # Añadimos una fila a la tabla
            tabla.rows.append([id_pokemon, nombre, altura, peso, habilidades, tipos])

            # Damos estilo a la tabla
            tabla.set_style(BeautifulTable.STYLE_BOX)

            # Mostramos la tabla
            system("cls")
            print(tabla)
            system("pause")

        except Exception as e:
            system("cls")
            print(f"Error: {e}")
            system("pause")

    def pokeImagen(self):
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
