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

