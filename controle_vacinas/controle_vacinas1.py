
# Leitura do número de meses
N = int(input("Quantidade de meses: ")) #quantidade de meses
D2 = 0 #imunizadas com a segunda dose em dias (prioridade 2)
D1 = 0 #imunizadas com a primeira dose (prioridade 3)
D2A = 0 #imunizadas completamente com atraso
D1A = 0 # esperando a segunda dose com atraso (prioridade 1)
vacinas = 0
# Processamento de cada mês
meses = list(range(1,N+1))
for i in meses:
    lote = int(input(f"Lote de vacinas do mês {i}: "))
    vacinas = vacinas + lote
    if D1 <= vacinas:
        D2 = D1
        vacinas = vacinas - D2
        D1
        D2
    elif D1 > vacinas:
        D2 = D1 - vacinas
        D1A = D1 - D2
        D1
        D2
        D1A
    if D1A <= vacinas:
        D2A = vacinas - D1A
        D1
        D2
        D1A
        D2A
    elif D1A > vacinas:
        D1A = D1A - vacinas
        D2A = D1A - vacinas
        D1
        D2
        D1A
        D2A

        
# Impressão da saída

print("Pessoas completamente imunizadas:", D2)
print("Pessoas imunizadas apenas com uma dose:", D1)
print("Pessoas que tomaram a segunda dose com atraso:", D2A)
print("Pessoas esperando a segunda dose com atraso:", D1A)
