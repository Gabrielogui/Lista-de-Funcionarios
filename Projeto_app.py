from appFunciorio import *
import os # Biblioteca para manipular sistema operacional(SO)

class Aplicacao:
    def __init__(self):
        # DADOS DA APLICAÇÃO
        self.dados = []
        while True:
            os.system('cls')
            # MENU
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
        
    def incluir_func(self):
        print('======= INCLUIR =======')
        IDfun  = int(input('ID do funcionario     : '))
        nmfun  = input('Nome do funcionario   : ')
        iddfun = input('Idade do funcionario  : ')
        cafun  = input('Cargo do funcionario  : ')
        safun  = float(input('Salario do funcionario: '))
        funcionario = Funcionario(IDfun, nmfun, iddfun, cafun, safun)
        self.dados.append(funcionario)
        print('Incluido com sucesso...')
        os.system('pause') # Função para apaertar qualquer botão para continuar

    def excluir_func(self):
        print('======= EXCLUIR =======')
        IDfun  = int(input('ID do funcionario: '))
        for f in self.dados:
            if IDfun == f.id:
                self.dados.remove(f) # FUNÇÃO QUE REMOVE O ELEMENTO DA LISTA
        print('Removido com sucesso...')
        os.system('pause') # Função para apaertar qualquer botão para continuar
    
    def ConsUm_func(self):
        print('===== CONSULTAR UM ======')
        IDfun  = int(input('ID do funcionario: '))
        for f in self.dados:
            if IDfun == f.id:
                print(f'ID = {f.id} ; Nome = {f.nome} ; Cargo = {f.cargo} ; Idade = {f.idade} ; salario = {f.salario}')
        os.system('pause') # Função para apaertar qualquer botão para continuar

    def ConsTodos_func(self):
        print('===== CONSULTAR TODOS =====')
        for f in self.dados:
            print(f'ID = {f.id} ; Nome = {f.nome} ; Cargo = {f.cargo} ; Idade = {f.idade} ; salario = {f.salario}')
        os.system('pause') # Função para apaertar qualquer botão para continuar

    def alterar_func(self):
        print('======= ALTERAR =======')
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
        print('Alterado com sucesso...')
        os.system('pause') # Função para apaertar qualquer botão para continuar
        '''self.ConsTodos_func()'''

# ================================
if __name__ == '__main__':
    app = Aplicacao()