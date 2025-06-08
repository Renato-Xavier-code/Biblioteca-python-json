from colorama import Fore, Style, init
import os

# Inicializa o colorama
init(autoreset=True)

# ==========================
# ======== CORES ===========
# ==========================
COR_TITULO = Fore.MAGENTA + Style.BRIGHT
COR_MENU = Fore.YELLOW + Style.BRIGHT
COR_INPUT = Fore.WHITE + Style.BRIGHT
COR_ERRO = Fore.RED + Style.BRIGHT
COR_SUCESSO = Fore.CYAN + Style.BRIGHT
COR_SAIR = Fore.LIGHTGREEN_EX + Style.BRIGHT
COR_INPUT_MENU = Fore.BLUE + Style.BRIGHT   # Pergunta do menu
COR_RESP = Fore.WHITE + Style.BRIGHT        # Resposta do menu


# ==============================
# ========= FUNÇÕES ============
# ==============================

# Limpar tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# Menu principal
def menu_main():
    limpar_tela()
    print(f"\n{COR_TITULO}                 BIBLIOTECA VIRTUAL                 \n")
    print(f"{COR_MENU}1- Cadastrar livro:")
    print(f"2- Atualizar livro:")
    print(f"3- Excluir livro:")
    print(f"4- Backup dos Dados:")  # 🔥 NOVO
    print(f"0- Sair:\n")


# Input para opção do menu
def input_opcao():
    return input(f"{COR_INPUT_MENU}QUAL OPERAÇÃO DESEJA: {COR_RESP}")


# Input padrão
def input_texto(texto):
    return input(f"{COR_INPUT}{texto}")


# Mensagem de erro
def msg_erro(texto):
    print(f"\n{COR_ERRO}{texto}")


# Mensagem de sucesso
def msg_sucesso(texto):
    print(f"\n{COR_SUCESSO}{texto}")


# Mensagem de saída
def msg_sair(texto):
    print(f"\n{COR_SAIR}{texto}\n")
