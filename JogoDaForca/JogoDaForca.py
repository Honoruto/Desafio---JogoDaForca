import random

palavraUm = ["c", "a", "c", "h", "o", "r", "r", "o"]
esconder = ["_", "_", "_", "_", "_", "_", "_", "_"]

palavraDois = ["g", "i", "r", "a", "f", "a"]
esconderDois = ["_", "_", "_", "_", "_", "_"]

palavraTres = ["m", "a", "c", "a", "c", "o"]
esconderTres = ["_", "_", "_", "_", "_", "_"]

aleatorio = 0
respostaErrada = 0
resposta = 0

tentativas = 16
tentativasSeis = 12

escolha = int(input("Esse é o jogo da forca! Escolha o tema do jogo (digite o numero do tema):\n 1 - Animais(disponivel).\n 2 - objetos(Em Breve!). \n 3 - frutas(Em Breve!)."))
if escolha == 1:
    aleatorio = random.randint(1, 3)
    if aleatorio == 1:
        for indiceDois in range(tentativas):
            print(f"Tentativas restantes:{tentativas}")
            print(esconder)
            letra = input("digite uma letra\n")
            for indice in range(0, 8):
                if palavraUm[indice] == letra:
                    esconder[indice] = palavraUm[indice] = letra
                    resposta = 1

                elif palavraUm[indice] != letra:
                    respostaErrada = 1

            if respostaErrada == 1 and resposta == 0:
                print("letra digitada não existe!")
                respostaErrada = 0

            elif resposta == 1 and respostaErrada == 0:
                resposta = 0

            elif resposta == 1 and respostaErrada == 1:
                resposta = 0
                respostaErrada = 0
            tentativas -= 1
            if palavraUm == esconder:
                print("Parabens! Você acertou a palavra secreta.")
                print(f"A pavra secreta era: {esconder}")
                break
            elif palavraUm != esconder and tentativas <= 0:
                print("As tentativas acabaram jogue de novo!")

    elif aleatorio == 2:
        for indiceDois in range(tentativasSeis):
            print(f"Tentativas restantes:{tentativasSeis}")
            print(esconderDois)
            letra = input("digite uma letra\n")
            for indice in range(0, 6):
                if palavraDois[indice] == letra:
                    esconderDois[indice] = palavraDois[indice] = letra
                    resposta = 1

                elif palavraDois[indice] != letra:
                    respostaErrada = 1

            if respostaErrada == 1 and resposta == 0:
                print("letra digitada não existe!")
                respostaErrada = 0

            elif resposta == 1 and respostaErrada == 0:
                resposta = 0
            elif resposta == 1 and respostaErrada == 1:
                resposta = 0
                respostaErrada = 0
            tentativasSeis -= 1
            if palavraDois == esconderDois:
                print("Parabens! Você acertou a palavra secreta.")
                print(f"A pavra secreta era: {esconderDois}")
                break
            elif palavraDois != esconderDois and tentativasSeis <= 0:
                print("As tentativas acabaram jogue de novo!")

    elif aleatorio == 3:
        for indiceDois in range(tentativasSeis):
            print(f"Tentativas restantes:{tentativasSeis}")
            print(esconderTres)
            letra = input("digite uma letra\n")
            for indice in range(0, 6):
                if palavraTres[indice] == letra:
                    esconderTres[indice] = palavraTres[indice] = letra
                    resposta = 1

                elif palavraTres[indice] != letra:
                    respostaErrada = 1

            if respostaErrada == 1 and resposta == 0:
                print("letra digitada não existe!")
                respostaErrada = 0

            elif resposta == 1 and respostaErrada == 0:
                resposta = 0
            elif resposta == 1 and respostaErrada == 1:
                resposta = 0
                respostaErrada = 0
            tentativasSeis -= 1
            if palavraTres == esconderTres:
                print("Parabens! Você acertou a palavra secreta.")
                print(f"A pavra secreta era: {esconderTres}")
                break
            elif palavraTres != esconderTres and tentativasSeis <= 0:
                print("As tentativas acabaram jogue de novo!")