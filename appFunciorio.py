# |=======| CLASSE DE FUNCIONÁRIOS |=======|
class Funcionario():
    # ======= CONSTRUTOR =======
    def __init__(self, ID : int, nome : str, idade : int, cargo : str, salario : float):
        self.id      = ID      # ID do funcionário
        self.nome    = nome    # Nome do funcionário
        self.idade   = idade   # Idade do funcionário
        self.cargo   = cargo   # Cargo do funcionário
        self.salario = salario # Salário do funcionário

    
# ==========================
if __name__ == '__main__':
        print('[ERRO] Esta classe só pode ser chamada de outra classe!')