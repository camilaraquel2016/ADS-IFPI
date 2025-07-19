def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        nova_colecao.append(funcao_transformadora(item))

    return nova_colecao    


def obter_saida(media):
    if media > 60:
        return 'AQUI E BODYBUILDER!!'
    elif media >= 40:
        return 'Ta saindo da jaula o monstro!'
    elif media >= 14:
        return 'Bora, hora do show! BIIR!'
    elif media >= 13:
        return 'E 13'
    elif media >= 1:
        return 'Nao vai da nao'


def obter_resultado():
    qtd_casos = 0
    soma_das_media = 0

    while True:
        w1, w2, r = mapear(input().split(), int)

        if w1 == 0 and w2 == 0 and r == 0:
            if qtd_casos > 0:
                media_de_todos_casos = soma_das_media / qtd_casos
                if media_de_todos_casos > 40:
                    print()
                    print('Aqui nois constroi fibra rapaz! Nao e agua com musculo!')
                
            break

        obter_media_1rm = lambda w1, w2, r: ((w1 + w2) / 2) * (1 + (r / 30)) 
        media = obter_media_1rm(w1, w2, r)
        saida = obter_saida(media)
        print(saida)

        qtd_casos += 1
        soma_das_media += media


def main():
    obter_resultado()

main()    
    