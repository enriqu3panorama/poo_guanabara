import time
class Livro:
    '''
    Cria um livro que tem páginas e passa as página
    '''
    def __init__(self, titulo='Livro', paginas='5'):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_leitor = 1
    
    def avancar_paginas(self, n_paginas):
        for _ in range(n_paginas):
            if self.pagina_leitor >= self.paginas:
                break
            self.pagina_leitor += 1
            print(f'Você passou uma página e agora está na página {self.pagina_leitor}.')
            time.sleep(0.3)
        if self.pagina_leitor >= self.paginas:
            print('Você chegou ao final do livro.')
        else:
            print(f'Você avançou {n_paginas} e agora está na página {self.pagina_leitor}')
    def __str__(self):
        return f'Você acabou de abrir o livro {self.titulo}, que tem {self.paginas} paginas no total. Você agora está na página {self.pagina_leitor}.'


l1 = Livro('Crime e Castigo', 10)
print(l1)
l1.avancar_paginas(5)
l1.avancar_paginas(100)
l1.avancar_paginas(1)
l1.avancar_paginas(2)


