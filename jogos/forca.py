import  random

def jogar():

    mensagem_abertura()

    palavra_secreta = carregar_palvras_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    erros = 0
    enforcou = False
    acertou = False


    while(not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas,palavra_secreta)
        else:
            erros+=1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if (acertou):
            imprime_mensagem_vencedor()
        elif(enforcou):
            imprime_mensagem_perdedor()


def mensagem_abertura():
    print("********************************")
    print("**BEM VINDO AO JOGO DA FORCA!**")
    print("********************************")
def carregar_palvras_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute =input("CHUTE UMA LETRA: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Você Ganhou!!")
    print("FIM DO JOGO!!")


def imprime_mensagem_perdedor():
    print("Você Perdeu!!")
    print("FIM DO JOGO!!")



if(__name__ == "__main__"):
    jogar()