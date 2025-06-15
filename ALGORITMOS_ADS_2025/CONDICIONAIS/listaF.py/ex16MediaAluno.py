from utils import entradaFloat, validarNumLimiteFloat

def calcularMedia(n1, n2):
    return (n1 + n2) / 2


def pedirNota(label: str):
    nota = entradaFloat(label)
    nota = validarNumLimiteFloat(nota, 0, 10, label)
    return nota


def situacaoAluno(n1, n2):
    media = calcularMedia(n1, n2)

    if media >= 7:
        return f'Média: {media:.1f}\nSituação do aluno: "Aprovado"'
    else:
        print(f'Média: {media:.1f}')
        print('Sua média foi abaixo de 7.0. Você deve fazer uma nova prova!')
        notaNovaProva = pedirNota('Insira sua nota obtida nessa nova prova: ')
        novaMedia = calcularMedia(media, notaNovaProva) # a nova média será calculada a partir da média anterior e da nova nota do aluno a partir dessa últma prova
       
        if novaMedia >= 7:
            return f'Média: {novaMedia:.1f}\nSituação do aluno: "Aprovado"'
        else:
            return f'Média: {novaMedia:.1f}\nSituação do aluno: "Reprovado"'   


def main():
    print('-=-NOTAS ESCOLARES-=-')

    nota1 = pedirNota('Insira a primeira nota do aluno: ')
    nota2 = pedirNota('Insira a segunda nota do aluno: ')

    print(situacaoAluno(nota1, nota2))

main()    