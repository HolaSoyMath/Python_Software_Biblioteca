from unittest import case
from menu import *
from livros import *
from basearquivos import *

CATEGORIAS_LIVRO =['Terror', 'Comédia', 'Suspense', 'Romântico']
MENU_INICIAL = ['Registro Empréstimo','Registro Devolução', 'Novo Usuário', 'Editar Usuário', 'Lista Usuários', 'Novo livro', 'Editar Livro', 'Consultar Livro']
quantidade = 0

while True:
    # Abrir menu inicial com os sub-menus a serem acessados
    cabecalho('Menu Inicial')
    escolha = sub_menu(MENU_INICIAL, 'Sair')
    apagar_console()
    
    # Caso o usuário digite 0 o programa é encerrado
    if escolha == 0:
        break
    # Caso o usuário digite 6 o programa ira criar um novo livro na base de dados
    elif escolha == 6: # Novo Livro
        while True: 
            cabecalho('Registro novo livro', 'Qual a categoria do novo livro ?') # Construir o cabeçalho
            while True: 
                
                # Escolha de categoria do livro
                escolha_cat = sub_menu(CATEGORIAS_LIVRO)
                if escolha_cat ==0:
                    break
                elif escolha_cat < 0 or escolha_cat > len(CATEGORIAS_LIVRO):
                    print('Opção inválida, tente novamente!')
                    cabecalho('Registro novo livro', 'Qual a categoria do novo livro ?')
                else:
                    break
            if escolha_cat ==0:
                apagar_console()
                break
            
            # Escolher as informações referentes ao livro
            nome_livro = str(input('Qual o nome do livro ? ')).capitalize()
            codigo_livro = gerador_codigo(CATEGORIAS_LIVRO[escolha_cat])
            quantidade = int(input('Quantidade de livros disponíveis: '))
            print(f'O código gerado para o livro é: {codigo_livro}')
            
            # Verificação, criação e alteração do arquivo da Base de dados
            arquivoExiste('Banco Livros.txt')
            cadastrar_livro('Banco Livros.txt', nome_livro, codigo_livro, quantidade)
            
            # Registro de um novo livro
            while True:
                resp = str(input('Deseja cadastrar um novo livro ? [S/N] ')).strip().upper()[0]
                if resp in 'SN':
                    break
                else:
                    print('Opção inválida, tente novamente!')
            apagar_console()
            if resp == 'N':
                break
            
    # Caso o usuário digite 8 o programa ira listartodos os livros presentes na base de dados
    elif escolha == 8:
        while True:
            # Ler todos os livros presentes na Base de Dados
            lerArquivo('Banco Livros.txt', 'Livros Cadastrados')
            linha()
            # Opção para voltar ao menu principal
            resp = int(input('Para voltar ao menu principal digite 0: '))
            apagar_console()
            if resp == 0:
                break
            else:
                print('Opção inválida, tente novamente!')

        
print('Programa encerrado!')
print('Obrigado e volte sempre!')
