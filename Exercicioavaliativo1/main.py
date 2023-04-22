from typing import List
from database import Database
from zoologicoCLI import AnimalCLI
from zoologicoDAO import ZoologicoDAO


animal_model = ZoologicoDAO(database = Database(database="Zoologico", collection="Animais")) #Inicializando o banco de dados chamado Zoologico e com a collections chamada Animais


#mexer dps
iniciar = AnimalCLI(animal_model)
iniciar.run()

