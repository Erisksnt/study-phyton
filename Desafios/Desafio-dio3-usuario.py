#Desafio Dio 3 - Cadastrando Usuario
from datetime import datetime, date, time
menu = """
╔==================== Bem vindo ao Erisk Bank ====================╗
║============== Onde seu dinheiro trabalha por você ==============║
║                         [1] Depositar                           ║ 
║                         [2] Saque                               ║
║                         [3] Extrato                             ║
║                         [4] Sair                                ║
╚=================================================================╝
"""
#em andamento

saldo = 0
limite = 500
saque_total = 0
limite_saque = 10
num_saques = 0
extrato = ""
data_hora_atual = datetime.today()
data_atual = datetime.today()
mascara_hora = "%H:%M - %d/%m/%Y"
mascara_dia = "%d/%m/%Y - %H:%M"
usuario = str(input("Informe o usuario de login:"))
senha = str(input("Digite sua senha:"))

while True:
    opcao = input(menu)
    #Deposito
    if opcao == "1" :
        valor = float(input("Qual valor do deposito?: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f} Realizado às {data_hora_atual.strftime(mascara_hora)}\n"
            print("Deposito efetuado com sucesso!", data_hora_atual.strftime(mascara_hora))
            print(f"Seu saldo é de: R$ {saldo:.2f}")
        else:
            print("Valor invalido")
    #Saque
    elif opcao == "2":
        valor = float(input("Qual valor do saque?: "))

        if (saque_total + valor) > limite:
                valor = print(input("O limite diario para saque é de R$500,00"))
                               
        else:
            if num_saques >= limite_saque:
                    print("Voce excedeu a quatidade de saques permitida.")
            else:
                if valor <= 0 or valor > saldo:
                        valor = print(input(f"Saldo insuficiente \nSaldo atual é de: R$ {saldo:.2f}"))
                        
                else:
                    saldo -= valor
                    saque_total += valor
                    num_saques += 1
                    extrato += f"Saque: R$ {valor:.2f} Realizado às {data_hora_atual.strftime(mascara_hora)}\n"
                    print("Saque efetuado com sucesso!", data_hora_atual.strftime(mascara_hora))
                    print(f"Seu saldo é de: R$ {saldo:.2f}")
    #Extrato
    elif opcao == "3":
         print(extrato)
         print(f"Seu saldo é de: R$ {saldo:.2f}")
         print(f"Extrato referente ao dia {data_atual.strftime(mascara_dia)}")
         
    #Sair do laço
    elif opcao == "4":
         print("Obrigado volte sempre!")
         break
    
    else:
         print("Digite uma opção valida")
