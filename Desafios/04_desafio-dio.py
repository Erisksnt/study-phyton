#Desafio Dio 4 - Utiliando Classes
#Em andamento
from datetime import datetime, date, time
from abc import ABC, abstractmethod

class Transacao(ABC):
     @abstractmethod
     def registrar(self, conta):
          pass
     
class Deposito(Transacao):
     def __init__(self, valor):
          self._valor = valor

     def registrar(self, conta):
          conta.depositar(self._valor)
          
class Saque(Transacao):
     def __init__(self, valor):
          self._valor = valor

     def registrar(self, conta):
          conta.sacar(self._valor)
     
class Historico:
     def __init__(self, transacao=None):
          if transacao is not None:
            self.transacoes.append(transacao)
          
     def extrato(self):
          return self.transacoes

     def adicionar_transacao(self,transacao=None):
          if transacao is not None:
            self.transacoes.append(transacao)                     

class Conta:
     def __init__(self, numero, agencia, cliente, sacar, depositar,saldo=0):
          self.saldo = saldo
          self.numero = numero
          self.agencia = agencia
          self.cliente = cliente
          self.sacar = sacar
          self.depositar = depositar

class ContaCorrente(Conta):
     def __init__(self, saldo, numero, agencia, cliente, limite, limite_saque):
          super().__init__(saldo, numero, agencia, cliente)
          self.limite = limite
          self.limite_saque = limite_saque

class Cliente:
     def __init__(self, nome, cpf, data_nasc, endereco):
          self.nome = nome
          self.cpf = cpf
          self.data_nasc = data_nasc
          self.endereco = endereco
          self.lista_conta = []
          return
     
     def adicionar_conta(self,conta):
          self.lista_conta.append(conta)
          return

     def realizar_trasacao(self, conta, transacao):
          transacao.registrar(conta)
          return

class PessoaFisica(Cliente):
     def __init__(self, nome, cpf, data_nasc, endereco):
          super().__init__(nome, cpf, data_nasc, endereco)   

menu = """
╔====================== Bem vindo ao Erisk Bank ====================╗
║============== Onde seu dinheiro trabalha por você ================║
║                         [1] Depositar                             ║ 
║                         [2] Saque                                 ║
║                         [3] Extrato                               ║
║                         [4] Criar Usuario                         ║
║                         [5] Criar Nova conta                      ║
║                         [6] Sair                                  ║
╚===================================================================╝
"""


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

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
     self.saldo = saldo
     self.numero = numero
     self.agencia = agencia
     self.historico = historico

#Cadastro de usuario
usuarios = []
def criar_usuario(usuarios):
    cpf = input("Informe o CPF(Somente numeros):")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Já existe usuario vinculado a esse CPF")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nasc = input("Informe sua data de nascimento: ")
    endereco = input("Informe seu endereço: ")

    usuarios.append({
        "nome": nome,
        "data_nasc": data_nasc,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuario Cadastrado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
     return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

#Criar conta Corrente
contas_corrente = []

def criar_conta(usuarios, contas_corrente):
     cpf = input("Informe o CPF(Somente numeros):")
     usuario = filtrar_usuarios(cpf, usuarios)

     if not usuario:
        print("Usuário não encontrado! Cadastre primeiro o usuário.")
        return
     
     agencia = "0001"
     numero_conta = len(contas_corrente) + 1

     conta = {
          "agencia": agencia,
          "numero_conta": numero_conta,
          "usuario": usuario,
          
     }
     contas_corrente.append(conta)
     print(f"Conta criada com sucesso!\nAgencia: {agencia}\nConta: {numero_conta}")

def filtrar_usuarios(cpf, usuarios):
     return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)


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
         print("=========================Extrato============================\n")
         print(extrato)
         print(f"Seu saldo é de: R$ {saldo:.2f}")
         print(f"Extrato referente ao dia {data_atual.strftime(mascara_dia)}\n")
         print("============================================================")
         
    #Chamar a função criar_usuario
    elif opcao == "4":
         criar_usuario(usuarios)
    
    #Chamar a função criar_conta
    elif opcao == "5":
          criar_conta(usuarios, contas_corrente)

    #Sair do laço
    elif opcao == "6":
        print("Obrigado volte sempre!")
        break
    else:
         print("Digite uma opção valida")
