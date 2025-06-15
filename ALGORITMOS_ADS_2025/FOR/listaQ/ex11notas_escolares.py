from itertools import count

from utils import obter_real_no_intervalo, obter_inteiro_positivo

def calcular_media(nota1, nota2, nota3):
    return (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10


def saida(qtd_alunos, qtd_aprovados, qtd_reprovados):
    return f'''
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Total de alunos: {qtd_alunos}
    Total aprovados: {qtd_aprovados}
    Total reprovados: {qtd_reprovados}
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''


def obter_resultado(media_de_aprovacao):
    total_aprovados = 0
    total_reprovados = 0

    for aluno in count():
        matricula = obter_inteiro_positivo(f'Matrícula do {aluno + 1}° aluno: (flag = 0) ')

        if matricula == 0:
            return saida(aluno, total_aprovados, total_reprovados)
        
        nota1 = obter_real_no_intervalo('1° nota: ', 0, 10)
        nota2 = obter_real_no_intervalo('2° nota: ', 0, 10)
        nota3 = obter_real_no_intervalo('3° nota: ', 0, 10)

        media_do_aluno = calcular_media(nota1, nota2, nota3)
        
        if media_do_aluno >= media_de_aprovacao:
            total_aprovados += 1
        else:
            total_reprovados += 1


def main():
    media_de_aprovacao = 7
    print(obter_resultado(media_de_aprovacao))

main()