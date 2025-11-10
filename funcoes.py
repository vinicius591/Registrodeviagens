import tabulate 

def registrar_viagem(listaViagens):
    motorista = input("Digite o nome do motorista: ")
    destino = input("O seu destino: ")
    distancia = float(input("Distancia percorrida em km: "))
    gasto = float(input("Valor gasto em combustivel em R$: "))
    consumo = gasto / distancia
    viagem = {
        "motorista": motorista,
        "destino": destino,
        "distancia": distancia,
        "gasto": gasto,
        "consmuo": consumo
    }
    listaViagens.append(viagem)
    print("viagem registrada\n")
    
def exibir_viagens(listaViagens):
    if not listaViagens:
        print("Nenhuma viagem registrada\n")    
        return
    
    tabela = []
    for v in listaViagens:
        tabela.append([
            v["motorista"],
            v["destino"],
            v["distancia"],
            v["gasto"],
            round(v["consumo"], 2)         
        ])
    print("\nLista de viagens: ")
    print(tabulate(tabela, headers = ["motorista", "destino", "km", "gasto R$", "R$/km"], tablefmt="fancy_grid"))
    
def buscar_motorista(listaViagens):
    nome = input("Digite o nome do motorsta: ")
    resultados = [v for v in listaViagens if v["motorista"] == nome.lower()]
    if not resultados:
        print("\nNenhuma viagem com {nome}\n")
        return
    
    tabela = []
    for v in resultados:
        tabela.append([
            v["motorista"],
            v["destino"],
            v["distancia"],
            v["gasto"],
            round(v["consumo"], 2)
        ])
    print(f"Viagens feitas por {nome}: ")
    print(tabulate(tabela, headers=["Motorista", "Destino", "Km", "Gasto R$", "R$/Km"], tablefmt="fancy_grid"))

def viagem_mais_cara(listaViagens):
    if not listaViagens:
        print("\nNenhuma viagem registrada: ")
        return
    
def pegar_gasto(v):
    return v["gasto"]

def viagem_mais_cara(listaViagens):
    if not listaViagens:
        print("\n⚠ Nenhuma viagem registrada ainda.\n")
        return

    mais_cara = max(listaViagens, key=pegar_gasto)

    print("\n Viagem com maior gasto:")
    print(f"Motorista: {mais_cara['motorista']}")
    print(f"Destino: {mais_cara['destino']}")
    print(f"Gasto: R$ {mais_cara['gasto']:.2f}\n")

    
def media_consumo (listaViagens):
    if not listaViagens:
        print("\nNenhuma viagem registrada")
        return
    
    media=sum (v["consumo"]for v in listaViagens) / len(listaViagens)
    print(f"\nMedia geral do consumo: {media:.2f} ")