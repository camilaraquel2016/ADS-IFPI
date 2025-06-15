def avaliarDesempenho(media):
    if media < 2:
        return 'Péssimo'
    elif media < 4:
        return 'Ruim'
    elif media < 7:
        return 'Regular'
    elif media < 8:
        return 'Bom'
    else:
        return 'Excelente'


def obterNumReal(label):
    num = str(input(label))

    try:
        num = float(num)
        return num
    except ValueError:
        print(f'O valor "{num}" não é um número real válido!')
        return obterNumReal(label)


def pedirNota():
    nota = obterNumReal('Insira a nota do aluno: ')

    if nota < 0 or nota > 10:
        print('Nota inválida!, nota deve está entre 0 e 10')
        nota = pedirNota()
    return nota 

def saidaFinal(genero,performace,quantidade,desempenho):
        print('-=' * 10)
        print(f'Performance das notas dos {genero}: {performace:.1f}%\nTotal de alunos: {quantidade}\nDesempenho dos homens: "{desempenho}"')
        print('-=' * 10)


def avaliarTurma(maiorNotaGeral,menorNotaGeral,qtdAlunos,qtdHomens,qtdMulheres,somatorioNotasGeral,somatorioNotasHomem,somatorioNotasMulheres):
    sexo = str(input('Sexo do aluno: (F/M) ')).upper()


    while sexo == 'F' or sexo == 'M':
        notaAluno = pedirNota()

        if notaAluno > maiorNotaGeral:
            maiorNotaGeral = notaAluno
        if notaAluno < menorNotaGeral:
            menorNotaGeral = notaAluno

        if sexo == 'F':
            qtdMulheres += 1
            somatorioNotasMulheres += notaAluno
        if sexo == 'M':
            qtdHomens += 1    
            somatorioNotasHomem += notaAluno

        qtdAlunos += 1
        somatorioNotasGeral += notaAluno
        sexo = str(input('Sexo do aluno: (F/M) ')).upper()
        
    if qtdAlunos >=1:
        mediaGeralDaTurma = somatorioNotasGeral / qtdAlunos
        desempenhoGeral = avaliarDesempenho(mediaGeralDaTurma)
        print('-=' * 10)
        print(f'Maior nota geral: {maiorNotaGeral:.1f}\nMenor nota geral: {menorNotaGeral:.1f}\nMédia geral da turma: {mediaGeralDaTurma:.1f}\nTotal de alunos: {qtdAlunos}\nDesempenho geral: "{desempenhoGeral}"')
        print('-=' * 10)

        if qtdMulheres >= 1:
            mediaNotasMulheres = somatorioNotasMulheres / qtdMulheres
            desempenhoMulheres = avaliarDesempenho(mediaNotasMulheres)
            performanceMulheres = mediaNotasMulheres * 10
            saidaFinal("mulheres",performanceMulheres,qtdMulheres,desempenhoMulheres)
        if qtdHomens >= 1:    
            mediaNotasHomens = somatorioNotasHomem / qtdHomens
            desempenhoHomens = avaliarDesempenho(mediaNotasHomens)
            performanceHomens = mediaNotasHomens * 10
            saidaFinal("homens", performanceHomens,qtdHomens,desempenhoHomens)
    else:
        print('Nenhum aluno cadastrado!')        

            



def main():
    maiorNotaGeral = 0
    menorNotaGeral = 11
    qtdAlunos = 0
    qtdHomens = 0 
    qtdMulheres = 0
    somatorioNotasGeral = 0
    somatorioNotasHomem = 0
    somatorioNotasMulheres = 0
    print('-=-AVALIADOR DE NOTAS-=-')        
    avaliarTurma(maiorNotaGeral,menorNotaGeral,qtdAlunos,qtdHomens,qtdMulheres,somatorioNotasGeral,somatorioNotasHomem,somatorioNotasMulheres)

main()

        
        





    