

def jogar():
    print("********************************")
    print("**BEM VINDO AO JOGO DA FORCA!**")
    print("********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        print("JOGANDO!")
        chute = input("CHUTE UMA LETRA: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontreia a letra {} na posição {}".format(letra,index))
            index = index + 1


    print("FIM DO JOGO!!")

if(__name__ == "__main__"):
    jogar()