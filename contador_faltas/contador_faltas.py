#Entrada inicial
total = int(input("Quantas aulas terá a discilina? "))
faltas = []
print("Responda sempre 'y' para sim ou 'n' para não nas preguntas")
faltas_aux = 0

#Desenvolvimento
while True:
    pergunta1 = input("Há faltas para registrar? ")
    if pergunta1 == "n":
        faltas_totais = sum(faltas)
        porcentagem = (faltas_totais/total)*100
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
        faltas_aux += pergunta2
        faltas.append(faltas_aux)

