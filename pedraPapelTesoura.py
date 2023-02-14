import random

print("=-" * 50 + "=")
print("Jogo de pedra papel tesoura! Pedra (a) ganha de tesoura (t) | t ganha de Papel (e) | e ganha de a!")
print("=-" * 50 + "=\n")

def jogo():
    player = input("Escolha pedra (a) papel (e) tesoura (t): ")
    comp = random.choice(['a', 'e', 't'])

    # print(f"\nO computador escolheu: {comp}.")

    if player == comp:
        print(f"Empate! O computador também escolheu '{comp}'")
    # a ganha de t | t ganha de e | e ganha de a
    elif (player == 'a' and comp == 't') or (player == 't' and comp == 'e') or (player == 'e' and comp == 'a'):
        print(f"Você venceu! O computador escolheu '{comp}'")
    else:
        print(f"Você perdeu! O computador escolheu '{comp}'")


jogo()
