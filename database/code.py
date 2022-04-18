from operator import itemgetter


class Persons:
    def __init__(self):
        self.persons = {}
    
    def __str__(self):
        string = ''
        for person in self.persons.keys():
            string += f'{person}: (sexo: {self.persons[person][0]}, idade: {self.persons[person][1]})'
            string += "\n"
        return string 
class Application():
    def __init__(self):
        self.__persons = Persons()
    
    def help_commands(self):
        print("Digite 1 para adicionar uma pessoa")
        print("Digite 2 para saber a idade do mais novo")
        print("DIgite 3 para saber a idade do mais velho")
        print("Digite 4 para ter acesso ao banco de dados")
        print("Digite 5 para saber a quantidade de mulheres")
        print("Digite 6 para saber a quantidade de homens")
        print("Digite 0 para fechar o aplicativo")
    
    def help_sex(self):
        print("Digite M (para masculino) ou F (para feminino)")

    def add_person(self):
        name = input("Name: ")
        while True:
            sex = input("Sexo: ")
            if sex == "M" or sex == "F":
                break
            else:
                self.help_sex()
        age = int(input("Idade: "))
        self.__persons.persons[f'{name}'] = (sex, age)
    
    def newest_person(self):
        persons = sorted(self.__persons.persons.items(), key=itemgetter(1), reverse=True)
        newest_person = persons[0]
        if newest_person[1][0] == "M":
            print(f'{newest_person[0]} é o mais novo, com {newest_person[1][1]} anos de idade')
        else:
            print(f'{newest_person[0]} é a mais nova, com {newest_person[1][1]} anos de idade')
    
    def oldest_person(self):
        persons = sorted(self.__persons.persons.items(), key=itemgetter(1))
        oldest_person = persons[0]
        if oldest_person[1][0] == "M":
            print(f'{oldest_person[0]} é o mais velho, com {oldest_person[1][1]} anos de idade')
        else:
            print(f'{oldest_person[0]} é a mais velha, com {oldest_person[1][1]} anos de idade')
        
    def women(self):
        aux = 0
        for person in self.__persons.persons.values():
            if person[0] == "F":
                aux += 1
            else:
                continue
        print(f'Há {aux} mulheres registradas')
    
    def men(self):
        aux = 0
        for person in self.__persons.persons.values():
            if person[0] == "M":
                aux += 1
            else:
                continue
        print(f'Há {aux} homens registrados')
    
    def printest(self):
        print(self.__persons)

    def execute(self):
        while True:
            print('')
            command = input("Command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_person()
            elif command == "2":
                self.newest_person()
            elif command == "3":
                self.oldest_person()
            elif command == "4":
                self.printest()
            elif command == "5":
                self.women()
            elif command == "6":
                self.men()
            else:
                self.help_commands()


application = Application()
application.execute()