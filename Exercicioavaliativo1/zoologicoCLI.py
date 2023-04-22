from classes import Animal, Cuidador, Habitat

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                breakmo
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class AnimalCLI(SimpleCLI):
    def __init__(self, zoologicoDAO):
        super().__init__()
        self.zoologicoDAO = zoologicoDAO
        self.add_command("create", self.create)
        self.add_command("read", self.read)
        self.add_command("update", self.updateAnimal)
        self.add_command("delete", self.delete)

    def create(self):
        print("Seja muito bem vindo cuidador!!")
        nome = input("Qual o seu nome ?")
        documento = input(f"Qual o seu documento {nome} ?")
        cuidador = Cuidador(nome, documento)

        habitats = []
        quant = int(input("quantos habitates voce quer criar ?"))
        for i in range(0,quant):
            nome = input("Qual o nome do habitat ?")
            tipo = input("Qual tipo de habitat:")
            habitat = Habitat(nome, tipo, cuidador)
            habitats.append(vars(habitat))

        nomeAnimal = input(f"Qual o nome do animal ?")
        especieAnimal = input(f"Qual a especie do animal ?")
        idadeAnimal = int(input(f"Qual a idade do animal ?"))

        self.zoologicoDAO.create_Animal( nomeAnimal, especieAnimal, idadeAnimal, habitats)

    def read(self):
        print(f"Coloque um id :")
        id = str(input())
        self.zoologicoDAO.read_animal_by_id( id)

    def updateAnimal(animal: Animal, nome: str):
        self.zoologicoDAO.updateAnimal(animal, nome)
    
    def delete(self):
        print(f"Coloque um id :")
        id = str(input())
        self.zoologicoDAO.read_animal_by_id( id)