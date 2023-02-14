import random


def adivinhar_numero():
  print("=-" * 60 + "=")
  print("Olá, usuário! \nIrei escolher um número dentro da sequência que você quiser e você tem que adivinhar ele!")
  print("=-" * 60 + "=")

  menor = int(input("Início do intervalo: "))

  maior = int(input("Fim do intervalo: "))

  escolhido = random.randint(menor, maior)

  palpite = 0

  print(escolhido)

  while palpite != escolhido:
    palpite = int(input(f"Escolha um número entre {menor} e {maior}: "))
    if palpite < escolhido:
      print("Tente mais uma vez, esse número está baixo...")
    elif palpite > escolhido:
      print("Tente mais uma vez, esse número está alto...")

  print(f"Você acertou! Eu escolhi o número {escolhido}!")

adivinhar_numero()


def comp_adivinha_num():

    # eu vou escolher um num e o pc tem q descobrir
    print("*-" * 50 + "*")
    print("Olá, usuário! Pense em um número e eu irei adivinhá-lo")
    print("*-" * 50 + "*")

    # 1 definir o intervalo por input("") (podia ser fixo)
    # usuario definira um intervalo e tentara adivinhar a partir dele
    print("\nPrimeiro, defina o intervalo em que esse número se encontra. Por exemplo: o numero está entre 1 e 10.")
    menor = int(input("Início do intervalo: "))
    maior = int(input("Fim do intervalo: "))

    # 2 preciso dar feedback se está baixo, alto ou correto, aqui so criando a variavel
    feedb = ""

    # o loop vai começar até conseguir acertar o numero, é um while pq enquanto ñ acertar, vai ficar perguntando
    while feedb != "c":
        if menor != maior:
            palpite = random.randint(menor, maior)
        else:
            palpite = menor  # tbm podia ser maior
        feedb = input(f"\nO numero {palpite} é menor ou maior? Ou é o número escolhido? \
      \nDigite c se estiver correto\nM maiusculo se for maior \nm minusculo se estiver menor\nResposta: ")

        if feedb == "M":
            maior = palpite - 1
        elif feedb == "m":
            menor = palpite + 1
    print(f"O número que vc escolheu foi: {palpite}, o computador acertou!")


comp_adivinha_num()
