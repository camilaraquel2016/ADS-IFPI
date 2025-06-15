def obterConceito(media):
    if media >= 9:
        return 'A'
    elif media >= 7.5:
        return 'B'
    elif media >= 6:
        return 'C'
    elif media >= 4:
        return 'D'
    else:
        return 'E'
    

def situacaoAluno(conceito):
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        return 'Aprovado'
    else:
        return 'Reprovado'


def calcularMedia(nota1, nota2):
    return (nota1 + nota2) / 2


def obterNota(num):
    nota = float(input(f'Insira a {num}° nota do aluno: ')) 

    while nota < 0 or nota > 10:
        print('Nota inváida') 
        nota = float(input(f'Insira a {num}° nota do aluno: ')) 
    return nota


def main():
    nota1 = obterNota(1)
    nota2 = obterNota(2)

    media = calcularMedia(nota1, nota2)

    conceito = obterConceito(media)

    situacao = situacaoAluno(conceito)

    print(f'Nota 1: {nota1:.1f}\nNota 2: {nota2:.1f}\nMédia: {media:.1f}\nConceito: {conceito}\nSituação do aluno: {situacao}')


main()    




