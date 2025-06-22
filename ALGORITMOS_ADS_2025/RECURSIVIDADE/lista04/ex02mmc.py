from utils import obter_inteiro_maior_que_0, eh_divisor

def obter_maior(num1, num2):
    return num1 if num1 > num2 else num2


def repetir(num1, num2, maior, candidato_mmc):
    if eh_divisor(num1, candidato_mmc) and eh_divisor(num2, candidato_mmc):
        return candidato_mmc
    
    candidato_mmc += maior
    return repetir(num1, num2, maior, candidato_mmc)
        

def obter_mmc(num1, num2):
    maior = obter_maior(num1, num2)
    candidato_mmc = maior

    return repetir(num1, num2, maior, candidato_mmc)


def main():
    num1 = obter_inteiro_maior_que_0('Primeiro número: ')
    num2 = obter_inteiro_maior_que_0('Segundo número: ')
    mmc = obter_mmc(num1, num2)
    print(f'MMC de ({num1}, {num2}) = {mmc}')

main()
