from funcoes import *
import json
import os
import shutil

CAMINHO_ARQUIVO = 'dados/biblioteca.json'


# Carregar dados do JSON
def carregar_dados():
    if not os.path.exists('dados'):
        os.makedirs('dados')

    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    else:
        return []


# Salvar dados no JSON
def salvar_dados(biblioteca):
    if not os.path.exists('dados'):
        os.makedirs('dados')

    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(biblioteca, arquivo, indent=4, ensure_ascii=False)


def listar_livros(biblioteca):
    if not biblioteca:
        print(f"\n{COR_ERRO}Nenhum livro cadastrado.")
        return False

    print(f"\n{COR_TITULO}{'=' * 50}")
    print(f"{'Lista de Livros:':^50}")
    print(f"{'=' * 50}")

    for i, livro in enumerate(biblioteca, start=1):
        nome = livro.get('nome', 'N/A')
        autor = livro.get('autor', 'N/A')
        editora = livro.get('editora', 'N/A')
        ano = livro.get('ano', 'N/A')
        print(f"{i} - {nome} - {autor} - {editora} - {ano}")

    print(f"{COR_TITULO}{'=' * 50}")
    return True


def cadastrar_livro(biblioteca):
    limpar_tela()
    print(f"\n{COR_TITULO}OPERAÇÃO 1 – CADASTRAR LIVRO\n")

    nome = input_texto("Digite o nome do livro: ")
    autor = input_texto("Digite o autor do livro: ")
    editora = input_texto("Digite a editora do livro: ")
    ano = input_texto("Digite o ano do livro: ")

    livro = {
        'nome': nome,
        'autor': autor,
        'editora': editora,
        'ano': ano
    }

    biblioteca.append(livro)
    salvar_dados(biblioteca)
    msg_sucesso("Livro cadastrado com sucesso!")
    input(f"\n{COR_INPUT}Pressione ENTER para continuar...")


def atualizar_livro(biblioteca):
    limpar_tela()
    print(f"\n{COR_TITULO}OPERAÇÃO 2 – ATUALIZAR LIVRO\n")

    if not listar_livros(biblioteca):
        input(f"\n{COR_INPUT}Pressione ENTER para continuar...")
        return

    try:
        indice = int(input_texto("\nEscolha o número do livro para atualizar: ")) - 1
        if indice < 0 or indice >= len(biblioteca):
            msg_erro("Número inválido!")
            input(f"\n{COR_INPUT}Pressione ENTER para continuar...")
            return

        nome = input_texto("Digite o nome do livro: ")
        autor = input_texto("Digite o autor do livro: ")
        editora = input_texto("Digite a editora do livro: ")
        ano = input_texto("Digite o ano do livro: ")

        biblioteca[indice] = {
            'nome': nome,
            'autor': autor,
            'editora': editora,
            'ano': ano
        }

        salvar_dados(biblioteca)
        msg_sucesso("Livro atualizado com sucesso!")

    except ValueError:
        msg_erro("Digite um número válido!")

    input(f"\n{COR_INPUT}Pressione ENTER para continuar...")


def excluir_livro(biblioteca):
    limpar_tela()
    print(f"\n{COR_TITULO}OPERAÇÃO 3 – EXCLUIR LIVRO\n")

    if not listar_livros(biblioteca):
        input(f"\n{COR_INPUT}Pressione ENTER para continuar...")
        return

    try:
        indice = int(input_texto("\nEscolha o número do livro para excluir: ")) - 1
        if indice < 0 or indice >= len(biblioteca):
            msg_erro("Número inválido!")
            input(f"\n{COR_INPUT}Pressione ENTER para continuar...")
            return

        livro = biblioteca.pop(indice)
        salvar_dados(biblioteca)
        msg_sucesso(f"Livro '{livro['nome']}' excluído com sucesso!")

    except ValueError:
        msg_erro("Digite um número válido!")

    input(f"\n{COR_INPUT}Pressione ENTER para continuar...")


def fazer_backup():
    origem = os.path.join('dados', 'biblioteca.json')
    destino = r'C:\Users\estud\Desktop\AULAS\PYTHON\AULA_10\dado_salvos\biblioteca.json'

    try:
        shutil.copy(origem, destino)
        print(f"\n{COR_SUCESSO}Backup realizado com sucesso! Arquivo salvo em: {destino}")
    except Exception as erro:
        print(f"\n{COR_ERRO}Erro ao realizar backup: {erro}")
    input(f"\n{COR_INPUT}Pressione ENTER para continuar...")


def menu_main():
    limpar_tela()
    print(f"{COR_TITULO}                 BIBLIOTECA VIRTUAL                 \n")
    print(f"{COR_MENU}1- Cadastrar livro:")
    print(f"{COR_MENU}2- Atualizar livro:")
    print(f"{COR_MENU}3- Excluir livro:")
    print(f"{COR_MENU}4- Fazer backup")
    print(f"{COR_MENU}0- Sair:\n")


def main():
    biblioteca = carregar_dados()

    while True:
        menu_main()
        opcao = input_opcao()

        if opcao == '1':
            cadastrar_livro(biblioteca)
        elif opcao == '2':
            atualizar_livro(biblioteca)
        elif opcao == '3':
            excluir_livro(biblioteca)
        elif opcao == "4":
            fazer_backup()
        elif opcao == '0':
            msg_sair("Saindo do programa... Até mais!")
            break
        else:
            msg_erro("Opção inválida! Tente novamente.")
            input(f"\n{COR_INPUT}Pressione ENTER para continuar...")


if __name__ == '__main__':
    main()
