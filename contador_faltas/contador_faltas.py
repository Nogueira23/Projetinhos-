#Entrada inicial
faltas = 0
print("Responda sempra 'y' para sim ou 'n' para não nas preguntas")
datas = []
#Desenvolvimento
with open("relatorio.csv", "r") as relatorio:
    for line in relatorio:
        linha = line.split(";")
        if linha[0] == "total":
            continue
        else:
            if linha[0] == '0':
                total = int(input("Quantas aulas terá a discilina? "))
            else:
                total = int(linha[0])
            faltas = int(linha[1])
            porcentagem = float(linha[2])
            restante = int(linha[3])
    while True:
        pergunta1 = input("Há faltas para registrar? ")
        if pergunta1 == "n":
            aux = 25 - porcentagem
            if aux < 0:
                aux = 0
            restante = int((aux/100)*total)
            datas.append(total)
            datas.append(faltas)
            datas.append(porcentagem)
            datas.append(restante)
            break
        else:
            pergunta2 = int(input("Quantas aulas você faltou? "))
            faltas += pergunta2
            porcentagem = float(((faltas/total))*100)
#Atualização de relatório
with open("relatorio.csv", "w") as relatorio:
    head = f'total;faltas;faltas_porcentagem;faltas_restantes'
    head += "\n"
    relatorio.write(head)
    line = f'{datas[0]};{datas[1]};{datas[2]}%;{datas[3]}'
    line += "\n"
    relatorio.write(line)

            
