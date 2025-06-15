from utils import entradaFloat

def calcularMedia(nota1, nota2):
    return (nota1 + nota2) / 2


def analisarSituacao(media):
    return 'Aprovado com distinção' if media == 10 else 'Aprovado' if media >= 7 else 'Reprovado'


def main():
    nota1 = entradaFloat('Nota 1: ')
    nota2 = entradaFloat('Nota 2: ')
    media = calcularMedia(nota1, nota2)

    situacaoAluno = analisarSituacao(media)
    print(f'Média do aluno: {media:.1f}\nSituação do aluno: {situacaoAluno}')

main()

