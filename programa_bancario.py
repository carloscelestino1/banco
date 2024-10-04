class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.__saldo = saldo  # Atributo privado para encapsulamento

    # Getter para saldo
    @property
    def saldo(self):
        return self.__saldo

    # Setter para saldo
    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("O saldo não pode ser negativo.")

    # Getter para titular
    @property
    def titular(self):
        return self.__titular

    # Setter para titular
    @titular.setter
    def titular(self, nome):
        if nome:
            self.__titular = nome
        else:
            print("O nome do titular não pode ser vazio.")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        elif valor <= 0:
            print("O valor de saque deve ser positivo.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def encerrar_conta(self):
        print(f"Conta {self.numero_conta} encerrada.")

contas = {}

def criar_conta():
    numero_conta = input("Informe o número da nova conta: ")
    if numero_conta in contas:
        print("Conta já existe. Tente novamente.")
    else:
        titular = input("Informe o nome do titular da conta: ")
        nova_conta = ContaBancaria(numero_conta, titular)
        contas[numero_conta] = nova_conta
        print(f"Conta {numero_conta} criada com sucesso.")

def selecionar_conta():
    numero_conta = input("Informe o número da sua conta: ")
    conta = contas.get(numero_conta)
    if conta:
        return conta
    else:
        print("Conta não encontrada.")
        return None

def verificar_saldo():
    conta = selecionar_conta()
    if conta:
        print(f"Saldo atual: R${conta.saldo:.2f}")

def depositar_dinheiro():
    conta = selecionar_conta()
    if conta:
        try:
            valor = float(input("Informe o valor para depósito: "))
            conta.depositar(valor)
        except ValueError:
            print("Valor inválido. Tente novamente.")

def sacar_dinheiro():
    conta = selecionar_conta()
    if conta:
        try:
            valor = float(input("Informe o valor para saque: "))
            conta.sacar(valor)
        except ValueError:
            print("Valor inválido. Tente novamente.")

def encerrar_atendimento():
    print("Encerrando o atendimento. Obrigado!")
    exit()

def menu():
    while True:
        print("\n=== Banco POO ===")
        print("1. Criar conta")
        print("2. Verificar saldo")
        print("3. Depositar dinheiro")
        print("4. Sacar dinheiro")
        print("5. Encerrar atendimento")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_conta()
        elif opcao == '2':
            verificar_saldo()
        elif opcao == '3':
            depositar_dinheiro()
        elif opcao == '4':
            sacar_dinheiro()
        elif opcao == '5':
            encerrar_atendimento()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
