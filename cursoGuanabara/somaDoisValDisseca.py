#SOMA DE DOIS NUMEROS#
"""
#qnd pedimos um input que nao é string, precisamos declarar
#qual o tipo de variavel que vai ser iserida no caso int, se ñ o comptdr acha q e string
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

soma = n1 + n2

print("A soma de {} e  {} eh {}".format(n1, n2, soma))
"""
n1 = input("Digite um valor: ")
#dissecando a variavel, colocando ".is()" traz diversas funções que trazem informacoes sobre ela
print(n1.isdecimal())
