#PARTE - VICTÓRIA
pontos1=0
pontos2=0
pontos3=0
pontos4=0
    

#tela de saída e dicas
def tela_de_saida():
    print("----------------------------------------------------------------------")
    print("\n TELA DE SAÍDA\n")
    print("----------------------------------------------------------------------")
    print("\nParabéns por ter terminado nosso programa. Esperamos que tenha gostado :)")
    print(" ")
    print(" ")
    print("***********************************************************************")
    exit()
            
def tela_de_dicas():
    print("----------------------------------------------------------------------")
    print("\nTELA DE DICAS\n")
    print("----------------------------------------------------------------------")
    print("1. Dica 1: Reduza o consumo de plástico, principalmente em embalagens de produtos frequentes na sua rotina, como: alimentos, bebidas e cosméticos")
    print("2. Dica 2: Economize energia elétrica apagando as luzes em comodos não utilizados no momento e desligando eletrodomésticos de uso simplório")
    print("3. Dica 3: Separe seu lixo para reciclagem")
    print("4. Dica 4: Faça o uso de mais transportes públicos e evite pegar Táxi/Uber em curtas distâncias")
    input("\nPressione Enter para voltar...") 

    
#COMEÇAR DAQUI
def tela_de_nivel():
    while True:
        print("----------------------------------------------------------------------")
        print("\nPARABÉNS, VOCÊ CONLUIU O DESAFIO SUSTENTAÍ!\n")
        print("\nAgora você podera saber o quão sustentável você é!\n")
     
        variavel_do_nivel=(pontos1+pontos2+pontos3+pontos4)
        
        if (variavel_do_nivel>=30) and (variavel_do_nivel<=40):
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É: ALTO!")
            print("----------------------------------------------------------------------")
        elif (variavel_do_nivel>=20) and (variavel_do_nivel<=29):
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É MODERADO!")
            print("----------------------------------------------------------------------")
        else:
            print("----------------------------------------------------------------------")
            print("O SEU NÍVEL DE SUSTENTABILIDADE É BAIXO!")
            print("----------------------------------------------------------------------")
            print("")
            print("Mas fique tranquilo(a), vamos te ajudar a melhorar...")
            
        print("\nEscolha uma opção:")
        print("(1) Obter dicas")
        print("(2) Levantamento de dados")
        print("(3) Sair")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            tela_de_dicas()
        elif opcao == "2":
            tela_de_levantamento_de_dados()
        elif opcao == "3":
            tela_de_saida()
            break
        else:
            print("\nOpção inválida! Tente novamente.")

#diária
def tela_de_levantamento_de_dados():
    total_pontos = pontos1 + pontos2 + pontos3 + pontos4 
    if total_pontos > 0:
        porcentagem1 = (pontos1 / total_pontos) * 100
        porcentagem2 = (pontos2 / total_pontos) * 100
        porcentagem3 = (pontos3 / total_pontos) * 100
        porcentagem4 = (pontos4 / total_pontos) * 100
    else:
        porcentagem1 = porcentagem2 = porcentagem3 = porcentagem4 = 0
            
    print("----------------------------------------------------------------------")
    print(" ")
    print("LEVANTAMENTO DE DADOS")
    print(" ")
    print("----------------------------------------------------------------------")
    print("Vamos ver detalhes da sua performance diária...")
    print("\nAgora você poderá saber o quão sustentável você é e onde pode melhorar, caso necessário!")
    print("Nível de sustentabilidade (diário) de acordo com cada desafio: ")
    print(" ")
    print(f"\nDesafio 1: {pontos1} pontos")
    print(f"\nDesafio 2: {pontos2} pontos")
    print(f"\nDesafio 3: {pontos3} pontos")
    print(f"\nDesafio 4: {pontos4} pontos")
    print(" ")
    print("\nDistribuição percentual dos pontos:")
    print(" ")
    print(f"\nDesafio 1: {porcentagem1:.2f}%")
    print(f"\nDesafio 2: {porcentagem2:.2f}%")
    print(f"\nDesafio 3: {porcentagem3:.2f}%")
    print(f"\nDesafio 4: {porcentagem4:.2f}%")
    print(" ")
        
    while True:
        print("\nEscolha uma opção:")
        print("(1) Voltar ao menu principal")
        print("(2) Obter dicas")
        print("(3) Sair")
        opcao9 = int(input("Digite a opção desejada: "))
        if opcao9 == 1:
            print("\nVoltando ao menu principal...")
            tela_de_menu_principal()
        elif opcao9==2:
            print("Tela de dicas") 
            tela_de_dicas()
        elif opcao9== 3:
            print("\nVocê encerrou o programa. Até mais!")
            tela_de_saida()
        else:
            print("\nOpção inválida! Tente novamente.")
tela_de_nivel()

def tela_de_menu_principal():
    print("----------------------------------------------------------------------")
    print(" ")
    print(" ")
    print(" ")
    print("----------------------------------------------------------------------")