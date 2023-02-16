"""
nome = input("Nome completo: ")

nomePartes = nome.split()

print(nome.upper(), "\n", nome.lower())
print("Seu primeiro nome tem {} letras".format(len(nomePartes[0])))

# ------------------------------------------------------------------------------------------------

n = int(input('Digite um número entre 0 e 9999: '))
if 0 <= n <= 9999:
    n2 = str(int(10000 + n))
    print('O número {} possui, {} milhares.'.format(n, n2[1]))
    print('O número {} possui, {} centenas. '.format(n, n2[2]))
    print('O número {} possui, {} dezenas. '.format(n, n2[3]))
    print('O número {} possui, {} unidades.'.format(n, n2[4]))
else:
    print("Numero fora dos parametros pedidos.")


# tentando fazer com laço de repetição depois
num = input("Digite um numero: ")

i = 0

print(num[1])
while i <= len(num):
    print(num[i])
    i += 1

# ------------------------------------------------------------------------------------------------

cidade = input("Digite o nome de uma cidade: ").strip().capitalize()

contem = "Santo" in cidade

print(cidade)

if contem == True:
    print("O nome da cidade começa com Santo")
else:
    print("O nome da cidade não começa com Santo.")

# ------------------------------------------------------------------------------------------------

nome = input("Qual seu nome completo: ").title()

nomeSplit = nome.split()
print("Seu nome contém a palavra 'Silva': ", "Silva" in nomeSplit)

#  ------------------------------------------------------------------------------------------------

frase = input("Digite uma frase: ").lower()

print("Na frase '{}' tem {} letras 'a'.".format(frase, frase.count("a")))

print("A primeira letra a aparece na posição: {} e a última na posição: {}".format(frase.find("a") + 1, frase.rfind("a") + 1))
print("Contando espaços.")
"""
#  ------------------------------------------------------------------------------------------------
nomeC = input("Seu nome completo: ")

listaN = nomeC.split()

print(listaN)

# o -1 é pq na lista mostra que tem 3 valores (p um nome de 3 nomes), mas nas posições o ultimo valor é 2 ( 0 1 2)
print(f"Seu primeiro e último nome são: {listaN[0]} {listaN[len(listaN) - 1]}")
