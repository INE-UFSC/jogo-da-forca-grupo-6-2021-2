
from forca import boneco, lista_palavras
from random import randint


def exibe_boneco(vidas_restantes: int):  # Samantha Costa
    'Recebe vidas_restantes(int)) e retorna o estado atual do boneco da forca(str)'
    vidas_restantes = 6 - vidas_restantes
    return (boneco[vidas_restantes])


def escolha_resposta():  # Felipe Backes Kettl
    '''Escolhe uma palavra aleatória de lista_palavras'''
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


def acerto(letra: str, resposta: str):  # Felipe Backes Kettl
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


def adiciona_palavra():  # Victor Gouvêa e Samantha Costa
    ''' Pede uma nova palavra, verifica se a palavra digitada é a que deseja adicionar na lista e caso sim, adiciona a lista_palavras. Printa se foi adicionada ou não. '''
    nova_palavra = str(
        input('Digite uma nova palavra para adicionar: ')).upper().strip()
    verificacao = input(
        f'Palavra digitada: {nova_palavra}. Adicionar? [S/N] ').upper()[0]
    while verificacao not in 'SN':
        verificacao = input(f'Erro. Tente novamente, digitando S ou N: ')
    if verificacao == 'S':
        lista_palavras.append(nova_palavra)
        print('Palavra adicionada com sucesso!')
    else:
        print('Palavra não adicionada. ')


def main():  # Todos
    print('-'*40)
    print('NOVO JOGO'.center(40))
    print('-'*40)
    vidas_restantes = 6
    resposta = escolha_resposta().upper()
    palavra = "_" * len(resposta)
    letras_chutadas = []

    while True:
        print(f'Palavra ({len(palavra)} letras): {palavra}')
        print(exibe_boneco(vidas_restantes))

        if letras_chutadas != []:
            print(f'Letras já escolhidas: {letras_chutadas}')
        letra = input("Escolha uma letra: ").upper()
        print()

        if len(letra) > 1:
            print("Você digitou mais de uma letra, tente novamente.")
            continue
        elif letra in letras_chutadas:
            print("Você já inseriu essa letra, tente novamente.")
            continue
        else:
            letras_chutadas.append(letra)

        acertou, index = acerto(letra, resposta)

        if acertou:
            print("Você acertou a letra!")
            palavra = atualiza_palavra(palavra, letra, index)

        else:
            print("Você errou!")
            vidas_restantes -= 1

        if vidas_restantes == 0:
            print(exibe_boneco(vidas_restantes))
            print("Você perdeu! Fim do jogo, a palavra era {}.".format(resposta))
            break

        elif "_" not in palavra:
            print(exibe_boneco(7))
            print("Você ganhou, parabéns!")
            print("A palavra era {} e você ainda tinha {} tentativa(s).".format(
                resposta, vidas_restantes))
            break


while True:
    print('-'*40)
    print('JOGO DA FORCA'.center(40))
    print('-'*40)
    print('''[ 1 ] Novo jogo
[ 2 ] Adicionar nova palavra ao jogo
[ 3 ] Sair do Programa''')
    while True:
        opcao = input('Digite o número de escolha: ').strip()[0]
        if opcao.isnumeric() != True or opcao not in '123':
            print('Por favor, digite um número correto. ')
            continue
        else:
            opcao = int(opcao)
            break
    if opcao == 1:
        main()
    elif opcao == 2:
        adiciona_palavra()
    else:
        print('FIM!')
        break
