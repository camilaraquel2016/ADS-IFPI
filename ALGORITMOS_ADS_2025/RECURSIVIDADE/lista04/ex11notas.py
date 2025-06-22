from utils import obter_num_real_na_faixa, obterNumInteiroPositivo


def saida(qtd_alunos, qtd_aprovados, qtd_reprovados):
    return f'''
    Total de alunos: {qtd_alunos}
    Total de aprovados: {qtd_aprovados}
    Total de reprovados: {qtd_reprovados}'''


def calcular_media_final(peso_nota1, peso_nota2, peso_nota3, nota1, nota2, nota3):
    return (nota1 * peso_nota1 + nota2 * peso_nota2 + nota3 * peso_nota3) / (peso_nota1 + peso_nota2 + peso_nota3)


def obter_media_final(peso_nota1, peso_nota2, peso_nota3):
    nota1 = obter_num_real_na_faixa('Primeira nota: ', 0, 10)
    nota2 = obter_num_real_na_faixa('Segunda nota: ', 0, 10)
    nota3 = obter_num_real_na_faixa('Terceira nota: ', 0, 10)
    return calcular_media_final(peso_nota1, peso_nota2, peso_nota3, nota1, nota2, nota3)


def obter_situacao(media_final):
    return 'APROVADO' if media_final >= 7 else 'REPROVADO'


def obter_resultado(peso_nota1, peso_nota2, peso_nota3, qtd_alunos = 0, qtd_aprovados = 0, qtd_reprovados = 0, contador = 1):
    matricula = obterNumInteiroPositivo(f'Matrícula do {contador}° aluno: (flag = 0) ')

    if matricula != 0:
        print(f'-=-{contador}° aluno-=-')
        media_final = obter_media_final(peso_nota1, peso_nota2, peso_nota3)
        situacao = obter_situacao(media_final)

        if situacao == 'APROVADO':
            qtd_aprovados += 1
        elif situacao == 'REPROVADO':
            qtd_reprovados += 1

        qtd_alunos += 1

        return obter_resultado(peso_nota1, peso_nota2, peso_nota3, qtd_alunos, qtd_aprovados, qtd_reprovados, contador + 1)    
    
    return saida(qtd_alunos, qtd_aprovados, qtd_reprovados)


def main():
    peso_nota1 = 2
    peso_nota2 = 3
    peso_nota3 = 5
    print(obter_resultado(peso_nota1, peso_nota2, peso_nota3, 0, 0, 0, 1))

main()