# início 25/05 - 13:00
# fim 25/05 - 13:39

from q1_number_utils import obterNumInteiroPositivo

def main():
    numDados = obterNumInteiroPositivo('Quantidade de dados: ')
    quantidade = obterQuantidade(numDados)

    qtdBack = int(quantidade[0])
    qtdDados = int(quantidade[1])
    qtdFront = int(quantidade[2])
    qtdMobile = int(quantidade[3])

    qtdTotal = qtdBack + qtdDados + qtdFront + qtdMobile

    print(exibirEstatistica(qtdBack, qtdDados, qtdFront, qtdMobile, qtdTotal))


def exibirEstatistica(qtdBack, qtdDados, qtdFront, qtdMobile, qtdTotal):
    return f'''
Total: {qtdTotal} alunos
Total de Backend: {qtdBack}
Total de Dados: {qtdDados}
Total de Frontend: {qtdFront}
Total de Mobile: {qtdMobile}
Percentual de Backend: {obterPercentual(qtdBack, qtdTotal):.2f}%
Percentual de Dados: {obterPercentual(qtdDados, qtdTotal):.2f}%
Percentual de Frontend: {obterPercentual(qtdFront, qtdTotal):.2f}%
Percentual de Mobile: {obterPercentual(qtdMobile, qtdTotal):.2f}%

'''
def obterPercentual(parte, todo):
    return parte / todo * 100


def menu():
    return '''
-=-=-=-=-=-=-=    
B - BACKEND
F - FRONTEND
M - MOBILE
D - DADOS
-=-=-=-=-=-=-=
'''

def pedirOpcao(label: str):
    print(menu())
    opcao = input(label).upper()

    qtd = opcao.split()[0]

    try:
        qtd = int(qtd)
    except ValueError:
        print('Entrada inválida')  
        return pedirOpcao(label)  
    
    tipo = opcao.split()[1]   

    if tipo != 'B' and tipo != 'F' and tipo != 'M' and tipo != 'D':
        print('Entrada inválida!')
        return pedirOpcao(label)
    
    return qtd, tipo



def obterQuantidade(numDados):
    contador = 1
    qtdBack = 0
    qtdFront = 0
    qtdDados = 0
    qtdMobile = 0

    while contador <= numDados:
        opcao = pedirOpcao('Insira a quantidade e o código: ex: 10 B\n--> ')
        qtd = opcao[0]
        tipo = opcao[1]

        if tipo == 'B':
            qtdBack += qtd
        elif tipo == 'F':
            qtdFront += qtd
        elif tipo == 'D':
            qtdDados += qtd
        else:
            qtdMobile += qtd            

        contador += 1

    return qtdBack, qtdDados, qtdFront, qtdMobile




main()