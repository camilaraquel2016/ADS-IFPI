from utils import obterNumInteiro

def somarIntervalo(limiteInicial, limiteFinal, soma):
    if limiteInicial >= limiteFinal:
        return soma
    else:
        limiteInicial += 1
        return somarIntervalo(limiteInicial, limiteFinal, soma + limiteInicial)
    

def main():
    limiteInicial = 1
    limiteFinal = obterNumInteiro('Limite final: ')    
    soma = limiteInicial

    somaDoIntervalo = somarIntervalo(limiteInicial, limiteFinal, soma)

    print(f'A soma do intervalo ({limiteInicial} a {limiteFinal}) é igual a {somaDoIntervalo}')

main()






