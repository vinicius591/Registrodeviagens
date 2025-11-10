from funcoes import *
listaViagens = []

while True:
    print('''
      ESCOLHA:
    1- Registrar viagens 
    2- Exibir todas as viagens  
    3- Buscar viagens pelo motorista
    4- Exibir viagem mais cara
    5- Mostrar média geral de consumo 
    0- sair
      ''')
    opcao = input("Digite a opção que deseja: ")
    
    match opcao: 
        case "1":
            registrar_viagem(listaViagens)
        case "2":
            exibir_viagens(listaViagens)
        case "3":
            buscar_motorista(listaViagens)
        case "4":
            viagem_mais_cara(listaViagens)
        case "5":
            media_consumo(listaViagens)    
        
    