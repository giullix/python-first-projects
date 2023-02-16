# Colocando cores no terminal #
print("\033[1;33;44mOla mundo\033[m")
print("\033[1;31mOla mundo\033[m")
print("\033[1;36;41mOla mundo\033[m")
print("\033[7mOla mundo\033[m")
print("\033[1;43mOla mundo\033[m")

a = 2
b = 4

print(f"Os valores são \033[34m{a} \033[me \033[m{b}")

nome = "Cuerva"

print("Ola, {}{}{}".format("\033[7m", nome, "\033[m"))

# usando dicionario

cores = {"branco": "\033[7;m",
         "vermelho": "\033[1;31m",
         "verde": "\033[1;32m",
         "amarelo": "\033[1;33m",
         "azul": "\033[1;34m",
         "roxo": "\033[1;35m",
         "ciano": "\033[1;36m"}

print(f"""{cores["branco"]}USANDO {cores["vermelho"]}AS {cores["verde"]}SETE 
{cores["amarelo"]}CORES {cores["azul"]}QUE {cores["roxo"]}CONFIGUREI 
{cores["ciano"]}AQUI!!!""")
