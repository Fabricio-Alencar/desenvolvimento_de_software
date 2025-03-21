from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    @abstractmethod
    def realizar_transacao(self, conta, transacao):
        pass

    @abstractmethod
    def adicionar_conta(self, conta):
        pass

class Conta(ABC):
    def __init__(self, numero: int, agencia: str, cliente: Cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    @abstractmethod
    def ver_saldo(self):
        pass

    @abstractmethod
    def nova_conta(self, cliente: Cliente, numero: int):
        pass

    @abstractmethod
    def sacar(self, valor: float):
        pass

    @abstractmethod
    def depositar(self, valor: float):
        pass

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta: Conta):
        pass

class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf: str, nome: str, data_nascimento: str):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        if isinstance(conta, Conta):
            return transacao.registrar(conta)
        print("Conta inválida")

    def adicionar_conta(self, conta):
        if isinstance(conta, Conta):
            self.contas.append(conta)
            print("Conta adicionada com sucesso!")
        else:
            print("Selecione uma conta válida!")

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta: Conta):
        conta.saldo += self.valor
        print("Depósito realizado com sucesso!")

class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta: Conta):
        conta.saldo -= self.valor
        print("Saque realizado com sucesso!")

class Historico:
    def __init__(self):
        self.historico = ["Histórico:",]

    def adicionar_transacao(self, transacao: Transacao):
        if isinstance(transacao, Saque):
            self.historico.append(f"Saque: R$ {transacao.valor}")
            print("Saque adcionado ao histórico")
        elif isinstance(transacao, Deposito):
            self.historico.append(f"Depósito: R$ {transacao.valor}")
            print("Transação adicionada ao histórico")


class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente):
        self.nova_conta(cliente, numero)
        super().__init__(numero, agencia, cliente)
        self.limite = 2000
        self.limite_saques = 2000

    def ver_saldo(self):
        print(f"Seu saldo é de R$ {self.saldo}")

    def nova_conta(self, cliente: Cliente, numero: int):
        print("Nova conta criada com sucesso!")
        return self

    def sacar(self, valor: float):
        if self.limite_saques < valor:
            print(f"Você ultrapassou seu limite de saque, selecione um valor menor [limite de saque: R$: {self.limite_saques}]")
            return
        if self.saldo < valor:
            print(f"Saldo insuficiente \nSaldo atual: {self.saldo}")
            return
        saque = Saque(valor)
        saque.registrar(self)
        self.historico.adicionar_transacao(saque)

    def depositar(self, valor: float):
        deposito = Deposito(valor)
        deposito.registrar(self)
        self.historico.adicionar_transacao(deposito)


if __name__ == "__main__":
    # Criando instâncias de clientes
    cliente1 = PessoaFisica("Rua A, 123", "259717289", "Maria", "24/09/2004")
    cliente2 = PessoaFisica("Rua B, 123", "272728292", "Pedro", "09/12/1999")

    # Criando contas correntes para os clientes
    conta1 = ContaCorrente("17272636", "Bradesco", cliente1)
    conta2 = ContaCorrente("28277227", "Banco do Brasil", cliente2)

    # Adicionando as contas aos clientes
    cliente1.adicionar_conta(conta1)
    cliente2.adicionar_conta(conta2)

    # Realizando transações na conta de Maria (cliente1)
    conta1.sacar(1000)   # Tenta sacar R$ 1000 (saldo insuficiente)
    conta1.depositar(2000)  # Deposita R$ 2000
    conta1.sacar(1000)  # Realiza saque de R$ 1000

    # Exibindo o saldo final da conta de Maria
    conta1.ver_saldo()  # Exibe saldo após saque e depósito

    # Realizando transações de Pedro (cliente2) na conta de Maria
    saque1 = Saque(1000)
    cliente2.realizar_transacao(conta1, saque1)  # Cliente2 tenta realizar transação na conta de Maria

    # Realizando mais transações com a conta de Maria
    conta1.sacar(500)  # Realiza saque de R$ 500
    conta1.depositar(1500)  # Realiza depósito de R$ 1500

    # Exibindo o saldo final de Maria
    conta1.ver_saldo()  # Exibe saldo após o saque e o depósito adicionais

    # Exibindo o histórico final
    print(conta1.historico.historico)  # Histórico final
