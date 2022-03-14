#Entrada inicial
total = int(input("Quantas aulas terá a discilina? "))
faltas = 0
print("Responda sempra 'y' para sim ou 'n' para não nas preguntas")

#Desenvolvimento
with open("relatorio.csv", "r+") as relatorio:
    for line in relatorio:
        pass
    while True:
        pergunta1 = input("Há faltas para registrar? ")
        if pergunta1 == "n":
            porcentagem = (faltas/total)*100
            if porcentagem < 25:
                aux = 25 - porcentagem
                print(f"Você faltou {porcentagem}% das aulas")
                if aux < 0:
                    print(f"Você está reprovado por falta, sorry!")
                else:
                    restante = int((aux/100)*total)
                    print(f"Você ainda pode faltar {restante} aulas!")
                break
        else:
            pergunta2 = int(input("Quantas aulas você faltou? "))
            faltas += pergunta2

