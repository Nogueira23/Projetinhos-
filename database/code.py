class Persons:
    def __init__(self):
        self.persons = {}

    def new_person(self):
        name = input("Digite o nome: ")
        while True:
            sex = input("Digite o sexo: ")
            if sex == "M" or sex == "F":
                break
            else:
                print("Responda com M (para masculino) ou F (para feminino)!")
        age = int(input("Digite a idade: "))
        self.persons[name] = []
        self.persons[name].append(sex)
        self.persons[name].append(age)
    
    def newest_person(self):
        menor = 400
        for person in self.persons.values():
            if person[1] < menor:
                menor = person[1]
            else:
                continue
        return f'A pessoa mais nova tem {menor} anos.'
    
    def oldest_person(self):
        maior = 0
        for person in self.persons.values():
            if person[1] > maior:
                maior = person[1]
            else:
                continue
        return f'A pessoa mais nova tem {maior} anos.'
    
        
    def man_persons(self):
        aux = 0
        for person in self.persons.values():
            if person[0] == "M":
                aux += 1
            else:
                continue
        return f'{aux} homens foram registrados'    
            
    def women_persons(self):
        aux1 = 0
        for person in self.persons.values():
            if person[0] == "F":
                aux1 += 1
            else:
                continue
        return f'{aux1} mulheres foram registradas'
        


persons = Persons()
persons.new_person()
pergunta = input("Ainda há pessoas para registrar? ")
while pergunta != "n":
    persons.new_person()
    pergunta = input("Ainda há pessoas para registrar? ")

print(persons.newest_person())
print(persons.oldest_person())
print(persons.man_persons())
print(persons.women_persons())

