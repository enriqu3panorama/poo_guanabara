class Produto:
    '''
    Cria um produto que tem nome e preço
    '''
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def etiqueta(self):
        return f'Produto: {self.nome}\nPreço: R${self.preco:.2f}'

p1 = Produto('Iphone 17', 7500)
print(p1.etiqueta())