from time import sleep

def menu():
    return f'1 - SIM\n2 - NÃO'


def obterInteiro(label):
    num = str(input(label))
    try:
        num = int(num)
        return num
    except ValueError:
        print('Inteiro inválido!')
        return obterInteiro(label)



def obterResposta(pergunta, label):
    print(pergunta)
    print(menu())
    sleep(1)

    resposta = obterInteiro(label)

    if resposta != 1 and resposta != 2:
        print('Resposta inválida!')
        sleep(1)
        return obterResposta(pergunta, label)
    else:
        return resposta
    

def eh_positiva(pergunta, labelEntrada):  
    resposta = obterResposta(pergunta, labelEntrada)
    return resposta == 1



def contarRespostasPositivas():
    qtdRespostasSim = 0

    label = 'Insira sua resposta: '

    if eh_positiva('Telefonou para a vítima?', label):
        qtdRespostasSim += 1
    if eh_positiva('Esteve no local do crime?', label):
        qtdRespostasSim += 1
    if eh_positiva('Mora perto da vítima?', label):
        qtdRespostasSim += 1
    if eh_positiva('Devia para a vítima?', label):
        qtdRespostasSim += 1
    if eh_positiva('Já trabalhou com a vítima?', label):
        qtdRespostasSim += 1

    return qtdRespostasSim


def classificarPessoa():
    qtdDeRespostaPositivas = contarRespostasPositivas()

    if qtdDeRespostaPositivas <= 1:
        return 'Inocente'
    elif qtdDeRespostaPositivas == 2:
        return 'Suspeita'
    elif qtdDeRespostaPositivas <= 4:
        return 'Cúmplice'
    else:
        return 'Assasino'
    

def main():
    situacao = classificarPessoa()

    print(f'Você é "{situacao}"')

main()    

            


    