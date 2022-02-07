

def jogar():
    print("********************************")
    print("**BEM VINDO AO JOGO DA FORCA!**")
    print("********************************")

    palavra_secreta = "abacaxi".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    erros = 0
    enforcou = False
    acertou = False


    while(not enforcou and not acertou):
        print("JOGANDO!")
        chute = input("CHUTE UMA LETRA: ")
        chute = chute.strip().upper()
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index+=1
        else:
            erros+=1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if (acertou):
            print("Você Ganhou!!")
        else:
            print("Você Perdeu!")

    print("FIM DO JOGO!!")

if(__name__ == "__main__"):
    jogar()