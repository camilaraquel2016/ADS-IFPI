def calcular_media_ponderada(peso_1, peso_2, peso_3, peso_4, nota_1, nota_2, nota_3, nota_4):
    return (nota_1 * peso_1 + nota_2 * peso_2 + nota_3 * peso_3 + nota_4 * peso_4) / (peso_1 + peso_2 + peso_3 + peso_4)


def obter_situacao_do_aluno(media):
    return 'Aluno aprovado.' if media >= 7 else 'Aluno em exame.' if media >= 5 else 'Aluno reprovado.'


def obter_situacao_final(media):
    return 'Aluno aprovado.' if media >= 5 else 'Aluno reprovado.'


def calcular_media_simples(nota1, nota2):
    return (nota1 + nota2) / 2


def main():
    peso_1 = 2
    peso_2 = 3
    peso_3 = 4
    peso_4 = 1

    notas = input().split()

    nota_1 = float(notas[0])
    nota_2 = float(notas[1])
    nota_3 = float(notas[2])
    nota_4 = float(notas[3])

    media = calcular_media_ponderada(peso_1, peso_2, peso_3, peso_4, nota_1, nota_2, nota_3, nota_4)

    print(f'Media: {media:.1f}')

    situacao_aluno = obter_situacao_do_aluno(media)

    print(situacao_aluno)

    if situacao_aluno == 'Aluno em exame.':
        nota_do_exame = float(input())
        print(f'Nota do exame: {nota_do_exame:.1f}')
        media = calcular_media_simples(media, nota_do_exame)
        situacao_final = obter_situacao_final(media)
        print(situacao_final)
        print(f'Media final: {media:.1f}')

main()        




