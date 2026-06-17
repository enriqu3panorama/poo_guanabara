# Declaração da Classe
class Gafanhoto:
    '''
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade

    Para criar uma nova pessoa, use:
    variavel = Gafanhoto(nome, idade)
    '''
    def __init__(self, nome='vazio', idade=0):
        # Atributos de instância
        self.nome = nome
        self.idade = idade
    
    # Métodos de instância
    def aniversario(self):
        self.idade += 1
    
    def __str__(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"

# Declaração de objeto
g1 = Gafanhoto('Maria', 19)
print(g1)

g2 = Gafanhoto('Joao Pedro', 20)
g2.aniversario()
print(g2)