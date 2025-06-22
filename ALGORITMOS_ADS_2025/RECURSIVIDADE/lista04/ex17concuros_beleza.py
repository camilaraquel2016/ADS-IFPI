from utils import obterNumRealPositivo


def saida(menor_peso, maior_peso, menor_altura, maior_altura, nome_magra, nome_gorda, nome_baixa, nome_alta):
    if maior_peso == 0:
        return f'NENHUMA CANDIDATA CADASTRADA'
    
    return f'''
    -=-MAIS ALTA-=
    Nome: {nome_alta}
    Altura: {maior_altura:.1f}

    -=-MAIS BAIXA-=
    Nome: {nome_baixa}
    Altura: {menor_altura:.1f}

    -=-MAIS GORDA-=-
    Nome: {nome_gorda}
    Peso: {maior_peso:.1f}

    -=-MAIS MAGRA-=-
    Nome: {nome_magra}
    Peso: {menor_peso:.1f}'''


def obter_dados(menor_peso = float('inf'), maior_peso = 0, menor_altura = float('inf'), maior_altura = 0, nome_magra = '', nome_gorda = '', nome_baixa = '', nome_alta = ''):
    print('-=' * 16)
    nome = str(input(f'Nome da candidata: (flag = FIM) ')).upper()

    if nome == 'FIM':
        return saida(menor_peso, maior_peso, menor_altura, maior_altura, nome_magra, nome_gorda, nome_baixa, nome_alta)
    
    peso = obterNumRealPositivo('Peso: (Kg) ')
    altura = obterNumRealPositivo('Altura: (M) ')

    if peso > maior_peso:
        maior_peso = peso
        nome_gorda = nome

    if peso < menor_peso:
        menor_peso = peso
        nome_magra = nome

    if altura > maior_altura:
        maior_altura = altura
        nome_alta = nome

    if altura < menor_altura:
        menor_altura = altura
        nome_baixa = nome

    return obter_dados(menor_peso, maior_peso, menor_altura, maior_altura, nome_magra, nome_gorda, nome_baixa, nome_alta)


def main():
    print('-=-=-=-CONCURSO DE BELEZA-=-=-=-')
    print(obter_dados(float('inf'), 0, float('inf'), 0, '', '', '', ''))

main()    