import math
import random
import emoji

"""
num = int(input("Digite um numero: "))

raiz = math.sqrt(num)

print(f"A raiz quadrada de {num} é {raiz}")

print(random.randint(1, 10))

print(emoji.emojize("Hello World :earth_americas:!", language='alias'))

# -----------------------------

# EXERCICIOS COM MÓDULOS #

# MOSTRA A PARTE INTEIRA DE UM NUMERO REAL #
n1 = float(input("Digite um numero real: "))

print("A parte inteira de {} é: {}".format(n1, math.trunc(n1)))

# -----------------------------

# CALCULA A HIPOTENUSA DE UM TRIANGULO RETANGULO #

#trinca 3 4 5 -  5 12 13

oposto = int(input("Qual o valor do cateto oposto? "))
adj = int(input("Qual o valor do cateto adjacente? "))

print("O valor da hipotenusa é: {}".format(math.isqrt(adj ** 2 + oposto ** 2)))

# SENO COSSENO TANGENTE #

angulo = float(input("Digite um ângulo: "))

aRad = math.radians(angulo)

print("O seno de {}: {:.2f}\n".format(angulo, math.sin(aRad)))

print("O cosseno de {}: {:.2f}\n".format(angulo, math.cos(aRad)))

print("A tangente de {}: {:.2f}".format(angulo, math.tan(aRad)))

# SORTEIO #

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

lista = [a1, a2, a3, a4]

e = random.choice(lista)

print("O auno escolhido foi: {}".format(e))

# ORDEM SORTEIO #
print("A ordem do sorteio é: {}".format(random.sample(lista, len(lista))))
"""
# ABRINDO ARQUIVO MP3 #
from playsound import playsound
playsound('water.mp3')
