# OPERADORES ARITMETICOS + - / * // % ** #

nome = str(input("Qual é seu nome? "))
print("Prazer em te conhecer {:*^20}!".format(nome))

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

print(f" Soma: {n1 + n2} \n Multiplicação: {n1 * n2} \n Divisão: {n1 / n2} \n Divisão inteira: {n1 // n2} \n Resto: {n1 % n2}\n", end="-")

# ------------------------------------------------------

# Desafio 5 aula 7
num = int(input("Digite um número:"))
print(f"O antecessor de {num} é {num-1}. O sucessor é {num+1}.\n")

# Desafio 6 aula 7
print(f"O dobro de {num} é: {num *2}. O tripo: {num * 3 }. Raiz quadrada: {num * (1/2)}\n")

# Desafio 7 aula 7
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

print("Sua média é: {}".format((n1 + n2) / 2))

# Desafio 8 aula 7
metro = float(input("Digite os metros: "))

print(" {} metros em CM = {} \n {} metros em MM = {}".format(metro, metro * 100, metro, metro * 1000))

# Desafio 9 aula 7 - TABUADA #
num = int(input("Vou mostrar a tabuada do numero desejado. Digite um numero inteiro: "))
qtdTabuada = int(input("Até qual numero voce deseja saber a tabuada? "))

i = 1

while  (i <= qtdTabuada):
    print(f"{num} x {i} = {num * i}")
    i += 1

# Desafio 10 aula 7

cotaDol = float(input("Qual é a cotação atual do dólar? "))
reais = float(input("Quantos reais você tem? "))

print(f"Você consegue comprar ${reais / cotaDol} dólares com esse valor.")

# Desafio 11 aula 7

alt = float(input("Qual é a altura da parede? "))
larg = float(input("Qual é a largura dela? "))

area = alt * larg

tinta = area / 2

print(f" Uma parede de área {area}m² precisa de {tinta} litros de tinta para ser pintada.")

# Desafio 12 aula 7 #

preco = float(input("Qual é o preço do produto? R$"))
desc = float(input("Quanto de desconto será aplicado? "))

print("O preço do produto com desconto é: R${:.2f}".format(preco - (desc * preco / 100)))

# Desafio 13 aula 7 #

sal = float(input("Quanto você recebe de salário?: R$"))
aum = float(input("Qual a porcentagem de aumento que você receberá? "))

print("Seu novo salário será de: R${:.2f}".format(sal + (aum * sal / 100) ))

# ALUGUEL DE CARRO #

dias = int(input("Por quantos dias o carro foi alugado? "))

km = float(input("Quantos km foram percorridos? "))

# 60 reais por dia e 15 centavos por km rodado

print("O valor a pagar pelo aluguel de {} dia(s) e {}km rodados é de: {}".format(dias, km, (dias * 60) + (0.15 * km)))
