from forca import boneco, lista_palavras
from random import randint

def exibe_boneco(vidas_restantes: bool):# Samantha
    'Recebe vidas_restantes(bool) e retorna o estado atual do boneco da forca(str)'
    return (boneco[vidas_restantes])

def escolha_resposta():#Felipe Backes Kettl
    index = randint(0, len(lista_palavras)-1)
    resposta = lista_palavras[index]
    return resposta


def atualiza_palavra(palavra: str, letra: str, indices: list):#Victor Gouvêa
    letra = letra.upper()
    palavra = list(palavra.upper())

    for index in indices:
        palavra[index] = letra

    palavra = "".join(palavra)

    return palavra

def acerto(letra, resposta): #Felipe Backes Kettl
    #Função para verificar o acerto, ou não, da letra
    #Recebe a letra que o jogador escolheu e a palavra-resposta que o jogo selecionou
    #Retorna o bool se acertou ou não e uma lista com os index dos acertos
    acertou = False
    index = []
    for x in range(len(resposta)):
        if letra == resposta[x]:
            index.append(x)
            acertou = True
    return acertou, index

