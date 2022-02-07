import random

def jogar():
    print("********************************")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    #print(numero_secreto)



    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel =  int (input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite Seu Número Entre 1 e 100: ")
        chute = int(chute)
        if (chute<1 or chute>100):
            print("Voce Deve Digitar Um Numero Entre 1 e 100")
            continue
        print("Você Digitou", chute)


        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto


        if (acertou):
            print("Você Acertou e fez {} pontos!!".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi pra cima")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

                # print("{}".format(pontos_perdidos))
                #print("{}".format(pontos))

            elif (menor):
                print("O seu chute foi pra baixo")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

                # print("{}".format(pontos_perdidos))
                #print("{}".format(pontos))

        rodada = rodada + 1



    print("Fim Do Jogo.")

if(__name__ == "__main__"):
    jogar()
