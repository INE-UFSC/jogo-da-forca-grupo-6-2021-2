def acerto(letra, resposta):
    
    acertou = False
    index = []
    for x in range(len(resposta)):
        if letra == resposta[x]:
            index.append(x)
            acertou = True
    return acertou, index

