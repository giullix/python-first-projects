"""
n1 = float(input("Nota :"))
n2 = float(input("Nota: "))

media = (n1 + n2) / 2

print(f"Sua media é: {media}")

# ou também pode usar
# print("Sua média foi boa!" if media >= 6 else "Você está abaixo da média!")

if media >= 6:
    print("Sua média foi boa!")
else:
    print("Você está abaixo da média!")
# -------------------------------------------------------------------------------------------------

from random import randint
from time import sleep
num = random.randint(0, 5)
print("-=-" * 20)
valor = int(input("Tente adivinhar que número eu escolhi entre 0 e 5: "))
print("-=-" * 20)

print("Processano...")
sleep(3)

if valor == num:
    print("Você acertou!")
else:
    print(f"Você errou, o número escolhido é: {num}")

# -------------------------------------------------------------------------------------------------

vel = int(input("Digite a velocidade em que você estava: "))

if vel > 80:
    print("Você ultrpassou o limite de 80km. A multa é de: {} reais".format((vel - 80) * 7))
    print("A cada km ultrapassado é cobrado 7 reais de multa.")
else:
    print("Você estava dentro da velocidade pemitida.")

# -------------------------------------------------------------------------------------------------

n = int(input("Digite um número, irei dizer se é par ou ímpar: "))

if n % 2 == 1:
    print(f"{n} é ímpar")
elif n == 0:
    print("Zero não é par nem ímpar.")
else:
    print(f"{n} é par.")

# -------------------------------------------------------------------------------------------------

d = int(input("Qual é a distância da viagem? "))

# tbm pode fazer assim:
# passagem = d * 0.5 if d <= 200 else passagem * 0.45

if d <= 200:
    passagem = d * 0.45
    print(f"O valor da sua passagem é: {passagem}")
else:
    passagem = d * 0.5
    print(f"O valor da sua passagem é: {passagem}")

# -------------------------------------------------------------------------------------------------

from datetime import date
ano = int(input("Digite um ano(coloque 0 para o ano atual): "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é bissexto.".format(ano))
else:
    print(f"O ano {ano} não é bissexto.")

# -------------------------------------------------------------------------------------------------
n1 = float(input("Digite um número: "))

n2 = float(input("Digite mais um número: "))

n3 = float(input("Digite só mais um número: "))

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f"O menor valor é {menor}. O maior é {maior}")

# OU

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f"O menor valor é {menor}. O maior é {maior}")

# -------------------------------------------------------------------------------------------------

print("-=" * 20)
print("Veja se você terá aumento de salário!")
print("-=" * 20)

s = float(input("Qual é o valor do seu salário: R$:"))

if s <= 1250.0:
    print(f"Seu salário subirá de R${s} para R${s * 0.15 + s}, um aumento de 15%")
else:
    print("Seu salário subirá de R${} para R${}, um aumento de 10%".format(s, s * 0.1 + s))

# -------------------------------------------------------------------------------------------------
"""
print("*" * 30)
print("Irei descobrir se as retas formam um triângulo ou não.")
print("PS: sempre use a mesma unidade de medida.")
print("*" * 30)

a = float(input("Comprimento da reta a: "))
b = float(input("Comprimento da reta b: "))
c = float(input("Comprimento da reta c: "))

if a + b > c and b + c > a and a + c > b:
    print(f"As retas {a}, {b} e {c} formam um triângulo: ")
else:
    print("As retas não formam um triângulo.")
