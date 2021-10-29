
from forca import boneco, lista_palavras
from random import randint


def exibe_boneco(vidas_restantes: int):  # Samantha Costa
    'Recebe vidas_restantes(int)) e retorna o estado atual do boneco da forca(str)'
    vidas_restantes = 6 - vidas_restantes
    return (boneco[vidas_restantes])


def escolha_resposta():  # Felipe Backes Kettl
    index = randint(0, len(lista_palavras)-1)
    resposta = lista_palavras[index]
    return resposta


def atualiza_palavra(palavra: str, letra: str, indices: list):  # Victor Gouvêa
    '''Função que atualiza a palavra que está sendo advinhada
     Substitui os traços pela letra escolhida, baseado no índice dessa letra na resposta
     Retorna a palavra atualizada já em string'''
    palavra = list(palavra)

    for index in indices:
        palavra[index] = letra

    palavra = "".join(palavra)

    return palavra


def acerto(letra, resposta):  # Felipe Backes Kettl
    '''Função para verificar o acerto, ou não, da letra
     Recebe a letra que o jogador escolheu e a palavra-resposta que o jogo selecionou
     Retorna o bool se acertou ou não e uma lista com os index dos acertos'''
    acertou = False
    index = []
    for x in range(len(resposta)):
        if letra == resposta[x]:
            index.append(x)
            acertou = True
    return acertou, index


def main():  # Todos
    print('-'*40)
    print('JOGO DA FORCA'.center(40))
    print('-'*40)
    vidas_restantes = 6
    resposta = escolha_resposta().upper()
    palavra = "_" * len(resposta)
    letras_chutadas = []

    while True:
        print(f'Palavra ({len(palavra)} letras): {palavra}')
        print(exibe_boneco(vidas_restantes))

        letra = input("Escolha uma letra: ").upper()
        if len(letra) > 1:
            print("Você digitou mais de uma letra, tente novamente")
            continue
        elif letra in letras_chutadas:
            print("Você já acertou com essa letra, tente novamente")
            continue

        acertou, index = acerto(letra, resposta)

        if acertou:
            print("Você acertou a letra!")
            palavra = atualiza_palavra(palavra, letra, index)
            letras_chutadas.append(letra)

        else:
            print("Você errou!")
            vidas_restantes -= 1

        if vidas_restantes == 0:
            print("Você perdeu! Fim do jogo, a palavra era {}".format(resposta))
            print(exibe_boneco(vidas_restantes))
            break

        elif "_" not in palavra:
            print("Você ganhou, parabéns!")
            print("Você ainda tinha {} tentativas".format(vidas_restantes))
            break


while True:
    main()
    while True:
        escolha = input('Quer jogar novamente? [S/N] ')[0].upper().strip()
        if escolha in 'SN':
            break
        else:
            print('Tente novamente, digitando S ou N. ', end=" ")
    if escolha == 'S':
        continue
    else:
        break
