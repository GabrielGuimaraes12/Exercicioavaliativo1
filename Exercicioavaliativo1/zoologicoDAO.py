from typing import List
from pymongo import MongoClient
from bson.objectid import ObjectId
from classes import Habitat

class ZoologicoDAO:
    def __init__(self, database):
        self.db = database

    def create_Animal(self, nome: str, especie: str, idade: int, habitat: List[Habitat]) -> str:
        try:
            result = self.db.collection.insert_one({"id": id, "nome": nome, "especie": especie, "idade": idade, "habitat": habitat})
            animal_id = str(result.inserted_id)
            print(f"Animal {nome} criado com o id: {animal_id}")
            return animal_id
        except Exception as error:
            print(f"Um erro aconteceu nao criacao do animal: {error}")
            return None

    def read_animal_by_id(self, animal_id: str) -> dict:
        try:
            animal = self.db.collection.find_one({"_id": ObjectId(animal_id)})
            if animal:
                print(f"Animal encontrado: {animal}")
                return animal
            else:
                print(f"Nenhum animal encontrado com o id {animal_id}")
                return None
        except Exception as error:
            print(f"Um erro aconteceu nao hora de ler o animal: {error}")
            return None
    def updateAnimal(self, animal_id: str, nome: str) -> None:
        try:
            result = self.db.collection.update_one({"_id": ObjectId(animal_id)}, {"$set": {"Animal": nome}})
            if result.modified_count:
                print(f"Animal {animal_id} updated with name {nome}")
            else:
                print(f"No animal found with id {animal_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating animal: {error}")
            return None
    def delete_animal(self, animal_id: str) -> int:
        try:
            result = self.db.collection.delete_one({"_id": ObjectId(animal_id)})
            if result.deleted_count:
                print(f"animal {animal_id} deleted")
            else:
                print(f"No animal found with id {animal_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting animal: {error}")
            return None
