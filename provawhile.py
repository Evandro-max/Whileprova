numero_secreto = 7
maximo = 3

for tentativa in range(1, maximo + 1):
    palpite = int(input(f"Tentativa {tentativa}/{maximo}: Qual é o número? "))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
else:
    print(f"Você não conseguiu adivinhar o número em 3 tentativas. O número era {numero_secreto}.")
