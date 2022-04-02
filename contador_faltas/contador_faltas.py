#Entrada inicial
faltas = 0
datas = []
nome_arquivo = input("Digite o nome do relatório: ")

#leitura dos dados
try:
    with open(f'{nome_arquivo}.csv', "r") as relatorio:
        for line in relatorio:
            linha = line.split(";")
            if linha[0] == "total":
                continue
            else:
                if linha[0] == '0':
                    total = int(input("Quantas aulas terá a discilina? "))
                    percent_max = float(input("Digite a porcentagem máxima de faltas permitidas: "))
                else:
                    total = int(linha[0])
                    percent_max = float(linha[4])
                faltas = int(linha[1])
                porcentagem = float(linha[2])
                restante = int(linha[3])
        while True:
            while True:
                pergunta1 = input("Há faltas para registrar? ")
                if pergunta1 == 'n' or pergunta1 == 'y':
                    break
                else:
                    print("Por favor, digite, como resposta, 'y' para sim ou 'n' para não")
            if pergunta1 == "n":
                aux = percent_max - porcentagem
                if aux < 0:
                    aux = 0
                restante = int((aux/100)*total)
                datas.append(total)
                datas.append(faltas)
                datas.append(porcentagem)
                datas.append(restante)
                datas.append(percent_max)
                break
            else:
                pergunta2 = int(input("Quantas aulas você faltou? "))
                faltas += pergunta2
                porcentagem = float(((faltas/total))*100)

#Escrita da base do relátorio
except FileNotFoundError:
    with open(f'{nome_arquivo}.csv', 'w') as relatorio:
        head = f'total;faltas;faltas_porcentagem(%);faltas_restantes;porcentagem_max'
        head += '\n'
        relatorio.write(head)
        line = f'{int(0)};{int(0)};{int(0)};{int(0)};{float(0.0)}'
        relatorio.write(line)
    #Desenvolvimento
    with open(f'{nome_arquivo}.csv', "r") as relatorio:
        for line in relatorio:
            linha = line.split(";")
            if linha[0] == "total":
                continue
            else:
                if linha[0] == '0':
                    total = int(input("Quantas aulas terá a discilina? "))
                    percent_max = float(input("Digite a porcentagem máxima de faltas permitidas: "))
                else:
                    total = int(linha[0])
                    percent_max = float(linha[4])
                faltas = int(linha[1])
                porcentagem = float(linha[2])
                restante = int(linha[3])
        while True:
            while True:
                pergunta1 = input("Há faltas para registrar? ")
                if pergunta1 == 'n' or pergunta1 == 'y':
                    break
                else:
                    print("Por favor, digite, como resposta, 'y' para sim ou 'n' para não")
            if pergunta1 == "n":
                aux = percent_max - porcentagem
                if aux < 0:
                    aux = 0
                restante = int((aux/100)*total)
                datas.append(total)
                datas.append(faltas)
                datas.append(porcentagem)
                datas.append(restante)
                datas.append(percent_max)
                break
            else:
                pergunta2 = int(input("Quantas aulas você faltou? "))
                faltas += pergunta2
                porcentagem = float(((faltas/total))*100)

#Atualização de relatório
with open(f'{nome_arquivo}.csv', "w") as relatorio:
    head = f'total;faltas;faltas_porcentagem(%);faltas_restantes;porcentagem_max'
    head += "\n"
    relatorio.write(head)
    line = f'{datas[0]};{datas[1]};{datas[2]};{datas[3]};{datas[4]}'
    line += "\n"
    relatorio.write(line)

            
