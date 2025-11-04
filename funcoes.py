import tabulate 

def registrar_viagem(listaViagens):
    motorista = input("Digite o nome do motorista: ")
    destino = input("O seu destino: ")
    distancia = float(input("distancia percorrida em km: "))
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
    
def exibir_viagens(liataViagens):
    if not liataViagens:
        print("Nenhuma viagem registrada\n")    
        return
    
    tabela = []
    for v in liataViagens:
        tabela.append([
            v["motorista"],
            v["destino"],
            v["distancia"],
            v["gasto"],
            round(v["consumo"], 2)         
        ])
    print("\nLista de viagens")
    print("")