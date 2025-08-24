
import datetime

menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

limite = 1000
saldo = limite
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
datas_saque = []

def data():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def deposito():
    print("=== Depósito ===")
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        global saldo, extrato
        saldo += valor
        extrato += f"{data()}    Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor para depósito precisa ser maior que 0(zero).")

def saque():
    print("=== Saque ===")
    valor = float(input("Informe o valor do saque: "))
    if valor > 0 and valor <= 500:
        global saldo, extrato, numero_saques
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
        # verifica se a quantidade de saques é 2
        if len(datas_saque) == 3:
            # Pega a primeira data de saque registrada
            #data_apenas = datas_saque[0].split()[0]
            primeira_data = datetime.datetime.strptime(datas_saque[0], "%d/%m/%Y %H:%M:%S")
            primeira_data_apenas = primeira_data.strftime("%d/%m/%Y")

            #data_atual_apenas = data_atual.strftime("%d/%m/%Y")
            # Só permite 3 saques se for em um dia diferente, se a data atual,
            # for diferente da primeira data quer dizer que estou em outro dia, 
            # e posso sacar, por isso zeramos a lista com das datas de saque e o numero de saques
            #data_atual = "24/08/2025 20:59:06"
            #if data_atual.date() != primeira_data.date():
            #print("Essa é a data atual: ",data_atual, " seu tipo é: ", type(data_atual))
            #print("Essa é a primeira data: ",data_apenas, " seu tipo é: ", type(data_apenas))
            if data_atual != primeira_data_apenas:
                datas_saque.clear()
                numero_saques = 0
        if numero_saques < LIMITE_SAQUES:
            if valor <= saldo:
                saldo -= valor
                #extrato += f"{data_atual}    Saque: R$ {valor:.2f}\n"
                #datas_saque.append(data_atual)
                extrato += f"{data()}    Saque: R$ {valor:.2f}\n"
                datas_saque.append(data())
                numero_saques += 1
                print("Saque realizado com sucesso!")
            else:
                print("Operação falhou! Saldo insuficiente.")
        else:
            print("Operação falhou! Limite de saques atingido.")
    else:
        print("Operação falhou! O valor para saque precisa ser maior que 0(zero) e menor que 500.")

def gerar_extrato():
    texto_extrato = "Extrato"
    print(texto_extrato.center(50, "="))
    if not extrato:
        print(f"\nNão foram realizadas movimentações.\n\n{data()}    Saldo com Limite: R$ {saldo:.2f}")
    else:
        print(extrato)
        print(f"{data()}    Saldo com Limite: R$ {saldo:.2f}")
    print("\n==================================================")


while True:
    
    opcao = input(menu)

    if opcao == "d":
        deposito()

    elif opcao == "s":
        saque()

    elif opcao == "e":
        gerar_extrato()

    elif opcao == "q":
        break
    else:
        print("Opção inválida. Tente novamente.")