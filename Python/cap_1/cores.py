# =========================================
# GUIA DE CORES NO TERMINAL (COLORAMA)
from colorama import Fore, Back, Style, init

# Inicializa (OBRIGATÓRIO no Windows)
init()

# ESTILOS (Style)

# Style.BRIGHT  -> Negrito
# Style.DIM     -> Fraco
# Style.NORMAL  -> Normal
# Style.RESET_ALL -> Reseta tudo (IMPORTANTE)

# CORES DO TEXTO (Fore)
# Fore.BLACK
# Fore.RED
# Fore.GREEN
# Fore.YELLOW
# Fore.BLUE
# Fore.MAGENTA
# Fore.CYAN
# Fore.WHITE

# CORES DO FUNDO (Back)
# Back.BLACK
# Back.RED
# Back.GREEN
# Back.YELLOW
# Back.BLUE
# Back.MAGENTA
# Back.CYAN
# Back.WHITE

# =========================================
# EXEMPLOS PRÁTICOS
# =========================================

print(Fore.GREEN + "Texto verde")
print(Fore.RED + "Erro em vermelho")
print(Fore.YELLOW + "Aviso em amarelo")

print(Back.BLUE + Fore.WHITE + "Fundo azul com texto branco")

print(Style.BRIGHT + Fore.MAGENTA + "Texto roxo em negrito")

# IMPORTANTE: sempre resetar no final
print(Style.RESET_ALL)

# =========================================
# EXEMPLO DE MENU COLORIDO
# =========================================

print(Fore.GREEN + "1 - Cadastrar")
print(Fore.BLUE + "2 - Listar")
print(Fore.YELLOW + "3 - Buscar")
print(Fore.RED + "0 - Sair")

a=3
b=5
print("Valores de {} e {}".format(Fore.RED + str(a) + Fore.RESET, Fore.GREEN + str(b)))
