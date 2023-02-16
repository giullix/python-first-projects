frase = "Curso em vídeo python"

# mostra quem está na terceira posição da frase
print(frase[3])

# mostra o começo da frase até a posição 4
print(frase[:4])

# mostra a frase a partir do elemento na posição 2 até a posição 16, pulando 2 em 2
print(frase[2:16:2])

print("""Atirei o pau no gato, tô
Mas o gato, tô
Não morreu, reu, reu
Dona Chica, cá cá
Admirou-se, se se
Do berrô, do berrô, que o gato deu, Miau!""")

# conta quantos Os tem na frase
print(frase.count("o"))

# substitui a primeira palavra pela segunda
print(frase.replace("python", "Android"))

# verifica se a palavra está na frase
print("Curso" in frase)

print(frase.title())

dividido = frase.split()

# mostra o terceiro elemento da lista dividido e o elemento na pos. 0 desse elemento
print(dividido[3][0])
