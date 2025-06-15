from utils import obterNumInt, obterNumReal

def obterNota(num):
    nota = obterNumReal(f'{num}° nota do aluno: ')

    while nota < 0 or nota > 10:
        print('Nota inválida!')
        nota = obterNumReal(f'{num}° nota do aluno: ')
    return nota    


def calcularMediaPonderada(nota1, peso1, nota2, peso2, nota3, peso3):
    return ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)


def obterSituacao(media):
    return 'aprovado' if media >= 7 else 'reprovado'


def analisarTurma(peso1, peso2, peso3):
    qtdAlunos = 0
    qtdAprovados = 0
    qtdReprovados = 0
    matricula = obterNumInt('Insira a matrícula: (flag = 0) ')

    while matricula != 0:
        qtdAlunos += 1
        nota1 = obterNota(1)
        nota2 = obterNota(2)
        nota3 = obterNota(3)
        media = calcularMediaPonderada(nota1, peso1, nota2, peso2, nota3, peso3)
        situacaoAluno = obterSituacao(media)
        if situacaoAluno == 'aprovado':
            qtdAprovados += 1
        else:
            qtdReprovados += 1    
    
        matricula = obterNumInt('Insira a matrícula: (flag = 0) ')
        
    if qtdAlunos == 0:
        return 'Não há alunos cadastrados!'
    else:
        return f'Total de aprovados: {qtdAprovados}\nTotal de reprovados: {qtdReprovados}\nTotal alunos: {qtdAlunos}'
 

def main():
    peso1, peso2, peso3 = 2, 3, 5
    print('-=-ANALISANDO NOTAS-=-')
    print(analisarTurma(peso1, peso2, peso3))    

main()

