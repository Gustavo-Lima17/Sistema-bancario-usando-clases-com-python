class Conta:
    def __init__(self, cliente, cpf, saldo, agencia = 1000):
        self.cliente = cliente
        self.cpf = cpf
        self.saldo = float(saldo)
        self.agencia = agencia
        self.transacoes = []
    
    def linha(self):
        return '*'*50
        
    def exibir_valores(self):
        return f"Nome: {self.cliente} \nCPF: {self.cpf} \nSaldo: {self.saldo} \nAgencia: {self.agencia}"
    
    def sacar(self,valor):
        if 0 < valor <= self.saldo:
            if valor <= 1000:
                self.saldo -= valor
                self.transacoes.append(f"Saque: -R$ {valor:.2f}")
                return f"Saque de R$ {valor:.2f} realizado. Saldo atual R$ {self.saldo};"
            return "Impossivel sacar mais de R$ 1000"
        return f"Valor de saque de R$ {valor} insunficiente ou invalido"

    def deposito(self,valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Deposito: +R$ {valor:.2f}")
            return f"Valor de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo};"
        return f"Valor de R$ {valor} invalido para deposito."
    def extrato(self):
        print("Extrato da conta: ")
        
        for t in self.transacoes:
            print(t)
        return f"Seu saldo Atual: R$ {self.saldo}"
    
class Menu:
    conta = Conta("testando 1", 12345678901, 1000, agencia= 1001)

    while True:
        print('SUPER BANCO VERSION 3.0')
        try: 
            opc = int(input('O que você deseja? \n1 - Verificar seus dados \n2 - Realizar saque \n3 - Realizar deposito \n4 - Extrato  \n5 - Sair \nR:  '))
        except ValueError:
            print("Digite um numero valido")
            continue
        
        if opc == 1:
            print('Verificando saldo...')
            print(conta.exibir_valores())
            print(conta.linha())
        elif opc == 2:
            valor = float(input("Insira o valor do saque: "))
            print(conta.sacar(valor))
            print(conta.linha())
        elif opc == 3:
            valor = float(input("Insira o valor do deposito: "))
            print(conta.deposito(valor))
            print(conta.linha())
        elif opc == 4:
            print("exibindo extrato detalhado.....")
            print(conta.extrato())
            print(conta.linha())
        elif opc == 5:
            print("Saindo....")
            break
        else:
            print("Opção invalida")


    