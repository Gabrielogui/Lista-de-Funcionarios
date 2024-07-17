from appFunciorio import * # Importando arquivo que contem classe do funcionário
import os # Biblioteca para manipular sistema operacional(SO)

# |=======| APLICAÇÃO |=======|
class Aplicacao:
    # ======= CONSTRUTOR DA APLICAÇÃO =======
    def __init__(self):
        # DADOS DA APLICAÇÃO
        self.dados = [] # Lista que ficará armazenado os funcionáios
        while True:
            os.system('cls')
            # ======= MENU =======
            print('''
            =================================
            CADASTRO DE FUNCUIONÁRIOS
            =================================
            Opções:
            1. Incluir funcionário
            2. Excluir funcionário
            3. Consultar um funcionário
            4. Consulta todos os funcionários
            5. Alterar funcionário
            6. Encerra aplicação
            =================================
            ''')
            op = int(input('Diga sua opção: '))
            if op == 1:
                self.incluir_func()
            elif op == 2:
                self.excluir_func()
            elif op == 3:
                self.ConsUm_func()
            elif op == 4:
                self.ConsTodos_func()
            elif op == 5:
                self.alterar_func()
            elif op == 6:
                print('Saindo do programa...')
                break
            else:
                print('Opção inválida...')
                os.system('pause') # Função para apaertar qualquer botão para continuar
    
    # |=======| MÉTODOS |=======|

    # ======= MÉTODO QUE GERA ID =======
    def gerandoID(self):
        return len(self.dados) + 1

    # ======= METODO QUE INCLUI FUNCIONÁRIO =======
    def incluir_func(self):
        print('======= INCLUIR =======')
        IDfun  = self.gerandoID()
        nmfun  = input('Nome do funcionario   : ')
        iddfun = input('Idade do funcionario  : ')
        cafun  = input('Cargo do funcionario  : ')
        safun  = float(input('Salario do funcionario: '))
        funcionario = Funcionario(IDfun, nmfun, iddfun, cafun, safun) # CRIANDO NOVO OBJETO FUNCIONÁRO
        self.dados.append(funcionario) # incluindo funcionário adicionado na lista
        print('Incluido com sucesso...')
        os.system('pause') # Função para apaertar qualquer botão para continuar

    # ======= MÉTODO QUE EXCLUI FUNCIONÁRIO =======
    def excluir_func(self):
        print('======= EXCLUIR =======')
        excluiu = False
        IDfun  = int(input('ID do funcionario: '))
        for f in self.dados:
            if IDfun == f.id:
                self.dados.remove(f) # FUNÇÃO QUE REMOVE O ELEMENTO DA LISTA
                excluiu = True
        
        if excluiu == False:
            print('Funcionário não encontrado!')
        else:
            print('Removido com sucesso...')
        os.system('pause') # Função para apaertar qualquer botão para continuar
    
    # ======= MÉTODO QUE CONSULTA UM FUNCIONÁIO =======
    def ConsUm_func(self):
        print('===== CONSULTAR UM ======')
        encontrou = False
        IDfun  = int(input('ID do funcionario: '))
        for f in self.dados:
            if IDfun == f.id:
                print(f'ID = {f.id} ; Nome = {f.nome} ; Cargo = {f.cargo} ; Idade = {f.idade} ; salario = {f.salario}')
                encontrou = True
        
        if encontrou == False:
            print('Fncionário não encontrado')
        os.system('pause') # Função para apaertar qualquer botão para continuar

    # ======= MÉTODO QUE CONSULTA TODOS OS FUNCIONÁRIOS =======
    def ConsTodos_func(self):
        print('===== CONSULTAR TODOS =====')
        encontrou = False
        for f in self.dados:
            print(f'ID = {f.id} ; Nome = {f.nome} ; Cargo = {f.cargo} ; Idade = {f.idade} ; salario = {f.salario}')
            encontrou = True

        if encontrou == False:
            print('Nenhum Funcionário cadastrado')
        os.system('pause') # Função para apaertar qualquer botão para continuar

    # ======= MÉTODO QUE ALTERA TODOS OS FUNCIONÁRIOS =======
    def alterar_func(self):
        print('======= ALTERAR =======')
        alterado = False
        IDfun  = int(input('ID do funcionario: '))
        for f in self.dados:
            if IDfun == f.id:
                nmfun  = input('Novo(ou não) nome do funcionario   : ')
                iddfun = input('Nova(ou não) Idade do funcionario  : ')
                cafun  = input('Novo(ou não) Cargo do funcionario  : ')
                safun  = float(input('Novo(ou não) salario do funcionario: '))
                f.nome    = nmfun
                f.idade   = iddfun
                f.cargo   = cafun
                f.salario = safun
                alterado = True
        
        if alterado == False:
            print('Funcionário não encontrado')
        else:
            print('Alterado com sucesso...')
        os.system('pause') # Função para apaertar qualquer botão para continuar
        '''self.ConsTodos_func()'''

# ================================
if __name__ == '__main__':
    app = Aplicacao()