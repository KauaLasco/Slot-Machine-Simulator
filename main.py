#Importação do módulo "random" para realizar a criação do caça-níquel.
#Precisamos desse módulo para gerar os valores do caça-níquel aleatóriamente.
import random

#Constantes globais.
MAXIMO_DE_LINHAS = 3
APOSTA_MAXIMA = 2000
APOSTA_MINIMA = 100


#Constantes do caça-níquel 3x3.
LINHAS = 3
COLUNAS = 3


#Quantidade dos simbolos selecionados que há em cada linha.
contagem_de_simbolos = {
    "$": 2,
    "@": 3,
    "#": 5,
    "%": 7
}


#Valores dos simbolos.
valor_dos_simbolos = {
    "$": 7,
    "@": 5,
    "#": 3,
    "%": 2
}


#Valida e verifica se há alguma linha com a sequência do mesmo simbolo para validar a vitórias do usuário em relação ao número de linhas que o mesmo selecionou para apostar.
def validador_de_vitorias(colunas, linhas, aposta, valores):
    vitorias = 0
    linhas_vitoriosas = []
    for linha in range(linhas):
        simbolo =  colunas[0][linha]
        for coluna in colunas:
            simbolo_a_validar = coluna[linha]
            if simbolo != simbolo_a_validar:
                break
        else:
            vitorias += valores[simbolo] * aposta
            linhas_vitoriosas.append(linha + 1)
    
    return vitorias, linhas_vitoriosas


#Gerador dos giros do caça-níquel, gerando aleatóriamente os simbolos em uma lista para serem adicionados na lista principal.
def giros_do_caca_niquel(linhas, colunas, simbolos):
    todos_simbolos = []
    for simbolo, contagem_de_simbolos in simbolos.items():
        for _ in range(contagem_de_simbolos):
            todos_simbolos.append(simbolo)

    colun = []
    for _ in range(colunas):
        coluna = []
        simbolos_atuais = todos_simbolos[:]
        for _ in range(linhas):
            valor = random.choice(simbolos_atuais)
            simbolos_atuais.remove(valor)
            coluna.append(valor)

        colun.append(coluna)
    
    return colun


#Exibe os simbolos em 3 linhas e 3 colunas.
def print_caca_niquel(colun):
    for linha in range(len(colun[0])):
        for i, coluna in enumerate(colun):
            if i != len(colun) - 1:
                print(coluna[linha], end=" | ")
            else:
                print(coluna[linha], end="")

        print()


#Variáveis globais.
saldo = 0


#Nesta função "Depósito" realizamos a coleta de informação do usuário referente a quantia que o mesmo deseja depositar.
#Verificamos se a informação inserida é um número, palavras, letras e maior que 0. 
#Caso atenda aos critérios irá ser realizado o armazenamento do valor inserido pelo usuário.
def deposito(saldo):
    while True:
        quantia = input("Quanto você deseja depositar? R$")
        if quantia.isdigit():
            quantia = int(quantia)
            if quantia > 0:
                saldo += quantia
                break
            else:
                print("Insira um valor válido que seja maior que 0!")
        else:
            print("Por favor insira um número!")
    return saldo


#Coleta de informações sobre as apostas do usuário em relação as linhas escolhidas para apostar.
def coleta_do_numero_de_linhas():
    while True:
        linhas = input(f"Insira o número de linhas para apostar! (1 - {str(MAXIMO_DE_LINHAS)})? ")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= MAXIMO_DE_LINHAS:
                break
            else:
                print("Insira um número válido de linhas!")
        else:
            print("Por favor insira um número!")
    return linhas


#Coleta do valor de aposta do usuário em cada linha.
def valor_da_aposta():
    while True:
        quantia = input("Quanto você deseja apostar em cada linha? R$")
        if quantia.isdigit():
            quantia = int(quantia)
            if quantia >= APOSTA_MINIMA and quantia <= APOSTA_MAXIMA:  
                break
            elif quantia < APOSTA_MINIMA:
                print(f"Insira um valor válido que seja maior que R${APOSTA_MINIMA}!")
            else:
                print(f"Insira um valor válido que seja menor que R${APOSTA_MAXIMA}")
        else:
            print("Por favor insira um número!")
    return quantia


#Dá opções ao usuário para prosseguir com a execução do código
def selecionar_opcao(saldo):
    while True:
        opcao = input("Você deseja depositar mais ou realizar outra aposta? " \
            "[1] depositar [2] refazer a aposta" \
            " ")
        if opcao.isdigit():
            opcao = int(opcao)
            if opcao == 1:
                    saldo = deposito(saldo)
                    return saldo
            elif opcao == 2:
                    return saldo
            else:
                print("Insira uma opção válida!")
        else:
            print("Insira um número!")


#Essa função serve para executar o programa multiplas vezes.
#Ela é a base para a execução de todo o software.
def giros(saldo):
    linhas = coleta_do_numero_de_linhas()
    while True:
        aposta = valor_da_aposta()
        valor_total_aposta = linhas * aposta 
        if valor_total_aposta > saldo:
            print(f"Você não tem saldo suficiente! Seu saldo atual é de R${saldo}!")
            print(f"Você precisa depositar mais R${linhas * aposta - saldo} para realizar a aposta!")
            saldo = selecionar_opcao(saldo)
            continue
        elif saldo < APOSTA_MINIMA:
            diferenca_saldo = APOSTA_MINIMA - saldo
            print(f"Seu saldo atual é de R${saldo}!")
            print(f"Deposite mais R${diferenca_saldo} para atingir o valor mínimo para realizar a aposta!")
            saldo = deposito(saldo  )
            continue        
        else:
            break

    print(f"Você está apostando R${aposta} em {linhas} linhas. O valor total da aposta é igual à R${valor_total_aposta}!")

    caca_niquel = giros_do_caca_niquel(LINHAS, COLUNAS, contagem_de_simbolos)
    print_caca_niquel(caca_niquel)

    vitorias, linhas_viroriosas = validador_de_vitorias(caca_niquel, linhas, aposta, valor_dos_simbolos)
    print(f"Você ganhou R${vitorias}!")
    print("Você ganhou nas seguintes linhas:", *linhas_viroriosas )
    saldo = saldo - valor_total_aposta + vitorias
    return saldo


#Função principal "main" para iniciar a execução do software
def main():
    saldo = deposito(0)
    while True:
        print(f"Seu saldo atual é R${saldo}")
        jogar = input("Pressione enter para jogar! (q para sair). ")
        if jogar == "q":
            break
        saldo = giros(saldo)

    print(f"Você terminou com R${saldo}.")

main()