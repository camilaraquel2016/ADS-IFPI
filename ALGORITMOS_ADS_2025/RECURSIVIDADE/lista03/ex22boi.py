from utils import obter_inteiro_maior_que_0, obterNumRealLimiteMin

def saida(identificacao_magro, identificacao_gordo, menor_peso, maior_peso):
    return f'''
    -=-Boi mais magro-=-
    N° de identificação: {identificacao_magro}
    Peso: {menor_peso} Kg

    -=-Boi mais gordo-=-
    N° de identificação: {identificacao_gordo}
    Peso: {maior_peso} Kg'''  


def controlar_boiada(n, maior_peso, menor_peso, identificacao_magro, identificacao_gordo, contador = 1):
 
    if contador <= n:
        print(f'-=-INFORMAÇÕES DO {contador}° BOI-=-')
        num_identificao = obter_inteiro_maior_que_0('Número de identificação: ')
        nome = str(input('Nome do boi: '))
        peso = obterNumRealLimiteMin(f'Peso do boi {nome}: (Kg) ', 1)

        if peso > maior_peso:
            maior_peso = peso
            identificacao_gordo = num_identificao

        if peso < menor_peso:
            menor_peso = peso
            identificacao_magro = num_identificao

        return controlar_boiada(n, maior_peso, menor_peso, identificacao_magro, identificacao_gordo, contador + 1)      

    return saida(identificacao_magro, identificacao_gordo, menor_peso, maior_peso)


def main():
    n = obter_inteiro_maior_que_0('Quantidade de fichas: ')
    maior_peso = 0
    menor_peso = float('inf')
    identificacao_mais_magro = 0
    identificacao_mais_gordo = 0
    print(controlar_boiada(n, maior_peso, menor_peso, identificacao_mais_magro, identificacao_mais_gordo, 1))

main()