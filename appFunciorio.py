class Funcionario():
    def __init__(self, ID : int, nome : str, idade : int, cargo : str, salario : float):
        self.id      = ID
        self.nome    = nome
        self.idade   = idade
        self.cargo   = cargo
        self.salario = salario

    
# ==========================
if __name__ == '__main__':
        print('[ERRO] Esta classe só pode ser chamada de outra classe!')