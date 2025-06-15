from utils import entradaFloat, validarNumLimiteFloat

def calcularMedia(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def situacaoAluno(nota1, nota2, nota3):
    media = calcularMedia(nota1, nota2, nota3)

    if nota1 == 0 or nota2 == 0 or nota3 == 0 or media < 5:
        return 'Reprovado' 
    elif media < 7:
        return 'Recuperação'
    else:
        return 'Aprovado'
    

def pedirNota(limiteMin, limiteMax, label):
    nota = entradaFloat(label)
    nota = validarNumLimiteFloat(nota, limiteMin, limiteMax, label)
    return nota
    

def main():
    nota1 = pedirNota(0, 10, f'Digite a {1}° nota do aluno: ')
    nota2 = pedirNota(0, 10, f'Digite a {2}° nota do aluno: ')
    nota3 = pedirNota(0, 10, f'Digite a {3}° nota do aluno: ') 

    media = calcularMedia(nota1, nota2, nota3)

    situacao = situacaoAluno(nota1, nota2, nota3)  

    print(f'Média do aluno: {media:.1f}\nSituação: "{situacao}"')  

main()    
    
