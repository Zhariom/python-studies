import random

lista_palavras = ['ventilador', 'perspicaz', 'felicidade', 'perspectiva', 'enfermidade', 'consecutivo', 'diversidade',
                  'reciprocidade', 'condescente', 'amor', 'alienado', 'empatia', ]
palavra_sorteada = random.choice(lista_palavras)
palavra_secreta = palavra_sorteada
letras_digitadas = []
tentativas = 5

while True:
    if tentativas <= 0:
        print('Você perdeu. Recomece o jogo.')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1 or len(letra) < 0:
        print('Hahahaha, não tente trapacear. Volta lá e digite apenas uma letra.')
        continue

    letras_digitadas.append(letra)
    if letra in palavra_secreta:
        print('Uhuuul! Você acertou uma letra, continue assim para ganhar.')
    else:
        tentativas -= 1
        if tentativas > 1:
            print(f'Você errou, mas não desanime você ainda tem {tentativas} chances.')
        elif tentativas >= 1:
            print(f'Você errou, mas não desanime você ainda tem {tentativas} chance.')
        else:
            print('Você perdeu, tente novamente!')
            break

    palavra_temporaria = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_digitadas:
            palavra_temporaria += letra_secreta
        else:
            palavra_temporaria += '_'

    if palavra_temporaria == palavra_secreta:
        print(f'PARABÉNS VOCÊ ACERTOU A PALAVRA SECRETA! A palavra secreta era {palavra_secreta}')
        break
    else:
        print(f'A palavra secreta está assim até o momento: {palavra_temporaria}')

    print()
