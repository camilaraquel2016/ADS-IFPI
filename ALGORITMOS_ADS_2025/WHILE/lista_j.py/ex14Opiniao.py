from time import sleep
from utils import obterNumInt

def saidaVotoInvalido():
    sleep(1)
    print(' ')
    print('Voto inválido!')
    sleep(1)

def saidaFinal(votosSerra, votosDilma, votosCiro, votosIndeciso, votosOutros, votosNuloBranco, totalRespostas):
    return f'''
        Serra: {calcularPorcentagem(votosSerra, totalRespostas):.1f}%
        Dilma: {calcularPorcentagem(votosDilma, totalRespostas):.1f}%
        Ciro Gomes: {calcularPorcentagem(votosCiro, totalRespostas):.1f}%
        Indecisos: {calcularPorcentagem(votosIndeciso, totalRespostas):.1f}%
        Outros: {calcularPorcentagem(votosOutros, totalRespostas):.1f}%
        Nulos ou brancos: {calcularPorcentagem(votosNuloBranco, totalRespostas):.1f}%'''


def menu():
    return '-=-=-=-=-=-=-=-\nSerra - 45\nDilma - 13\nCiro Gomes - 23\nIndeciso - 99\nOutros - 98\nNulo/Branco - 0\n-=-=-=-=-=-=-=-'


def calcularPorcentagem(valor, total):
    return valor / total * 100


def pedirVoto():
    while True:
        print(menu())
        print(' ')
        sleep(1)
        voto = obterNumInt('Seu voto: (flag = -1) ')
        if voto == 45 or voto == 13 or voto == 23 or voto == 99 or voto == 98 or voto == 0 or voto == -1:
            break 
        else:
           saidaVotoInvalido()

    return voto


def obterOpiniao():
    totalRespostas = 0
    votosSerra, votosDilma, votosCiro = 0, 0, 0
    votosIndeciso, votosOutros, votosNuloBranco = 0, 0, 0
    opiniao = pedirVoto()
    
    while opiniao != -1:
        totalRespostas += 1
        if opiniao == 45:
            votosSerra += 1
        elif opiniao == 13:
            votosDilma += 1
        elif opiniao == 23:
            votosCiro += 1
        elif opiniao == 99:
            votosIndeciso += 1
        elif opiniao == 98:
            votosOutros += 1
        elif opiniao == 0:
            votosNuloBranco += 1

        opiniao = pedirVoto()

    if totalRespostas == 0:
        return 'Nenhuma resposta cadastrada!'
    else:
        return saidaFinal(votosSerra, votosDilma, votosCiro, votosIndeciso, votosOutros, votosNuloBranco, totalRespostas)





            
        



