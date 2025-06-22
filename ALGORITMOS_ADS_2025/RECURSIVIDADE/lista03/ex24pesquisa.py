from utils import obter_inteiro_maior_que_0, obterNumRealPositivo, obterNumInteiroPositivo

def saida(soma_salario, qtd_habitantes, total_filhos, qtd_pessoas_salario_ate_1000):
    return f'''
    Média de salário da população: R${soma_salario / qtd_habitantes:.2f}
    Media de número de filhos: {total_filhos / qtd_habitantes}
    Percentual de pessoas com salário de até R$1.000,00: {qtd_pessoas_salario_ate_1000 / qtd_habitantes * 100:.1f}%
'''


def obter_dados(qtd_habitantes, contador = 1, soma_salario = 0, total_filhos = 0, qtd_pessoas_salario_ate_1000 = 0):

    if contador <= qtd_habitantes:
        print(f'-=-{contador}° habitante-=-')
        salario = obterNumRealPositivo('Salário: R$')
        qtd_filhos = obterNumInteiroPositivo('Quantidade de filhos: ')

        if salario <= 1000:
            qtd_pessoas_salario_ate_1000 += 1
        
        soma_salario += salario
        total_filhos += qtd_filhos

        return obter_dados(qtd_habitantes, contador + 1, soma_salario, total_filhos, qtd_pessoas_salario_ate_1000)
    
    return saida(soma_salario, qtd_habitantes, total_filhos, qtd_pessoas_salario_ate_1000)


def main():
    qtd_habitantes = obter_inteiro_maior_que_0('Quantidade de habitantes: ')
    print(obter_dados(qtd_habitantes, 1, 0, 0, 0))

main()    
