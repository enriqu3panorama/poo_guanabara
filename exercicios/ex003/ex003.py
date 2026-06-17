class ContaBancaria:
    '''
    Cria uma conta bancaria e permite fazer saques e depositos
    '''
    def __init__(self, id, nome, saldo=0):
        # Atributos de instância
        self.id = id
        self.nome = nome
        self.saldo = saldo
    
    def __str__(self):
        return f'A conta de id {self.id}, em nome de {self.nome}, tem R${self.saldo:.2f} de saldo'
    
    def depositar(self, valor):
        self.saldo += valor
        return print(f'Depósito de {valor} concluido! Seu saldo total agora é R${self.saldo:.2f}')


    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Erro: Saldo insuficiente')
        else:
            self.saldo -= valor
            print(f'Saque de {valor} concluido! Seu saldo total agora é R${self.saldo:.2f}')


c1 = ContaBancaria(1, 'Joao', 0)
c1.depositar(1000)
c1.sacar(3000)
print(c1)
    