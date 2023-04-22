from typing import List

class Cuidador:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

class Habitat:
    def __init__(self, nome, tipoAmbiente, cuidador: Cuidador):
        self.nome = nome
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = cuidador

class Animal:
    def __init__(self, nome, especie, idade, habitat: List[Habitat]):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.habitat = habitat
