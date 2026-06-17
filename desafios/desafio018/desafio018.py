class Churrasco:
    '''
    Analisa um churrasco, quantas pessoas vão, quantos KG de carne devem ser comprados, preço por pessoa
    '''
    def __init__(self, titulo='Churrasco', pessoas=1):
        self.titulo = titulo
        self.pessoas = pessoas
        self.qtd_carne = 0.4*pessoas
        self.custo_total = 82.40*self.qtd_carne
        self.custo_por_pessoa = self.custo_total / self.pessoas    
    
    
    def analisar(self):
        print(f'''              Analisando {self.titulo} com {self.pessoas} convidados...
              
              Cada participante comerá 0.4Kg e cada Kg custa R$82.40

              Recomendo comprar {self.qtd_carne:.2f}Kg de carne

              O custo total será de R${self.custo_total:.2f}

              Cada pessoa pagará R${self.custo_por_pessoa:.2f}''')

c1 = Churrasco('Churras dos crias', 3)
c1.analisar()