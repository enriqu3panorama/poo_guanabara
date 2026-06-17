# Declaração da Classe
class Gafanhoto:
    def __init__(self):
        # Atributos de instância
        self.nome = ""
        self.idade = 0
    
    # Métodos de instância
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"

# Declaração de objeto
g1 = Gafanhoto()
g1.nome = "Joao"
g1.idade = 19
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Lucas"
g2.idade = 26
g2.aniversario()
print(g2.mensagem())