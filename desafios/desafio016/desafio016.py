class Funcionario:
    '''
    Cria um funcionário que tem nome, setor e cargo em uma empresa
    '''
    def __init__(self, nome, cargo, setor):
        self.nome = nome
        self.cargo = cargo
        self.setor = setor
    
    def apresentar(self):
        return f'Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa Curso Em Vídeo.'

f1 = Funcionario('Rafael', 'Programador', 'TI')
print(f1.apresentar())

f2 = Funcionario('Maria', 'Diretora', 'Admnistração')
print(f2.apresentar())