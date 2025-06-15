#16:01
#16:23

def obterTamanho(texto: str):
    return len(texto)


def ehPar(num):
    return num % 2 == 0


def exibirDivisores(num):
    divisor = 1
    while divisor <= num:
        if num % divisor == 0:
            print(divisor)
        divisor += 1


def exibirMultiplos(num):
    contador = 1

    while contador <= num:
        contador += 1
        multiplo = num * contador
        print(multiplo) 
       

def main():
    nome = str(input('Nome do usuário: '))
    tamanhoNome = obterTamanho(nome)

    if ehPar(tamanhoNome):
        print(f'-=-=-PRÓXIMOS {tamanhoNome} MÚLTIPLOS DE {tamanhoNome}-=-')
        exibirMultiplos(tamanhoNome)
    else:
        print(f'-=--=DIVISORES DE {tamanhoNome}-=-=-')    
        exibirDivisores(tamanhoNome)


main()        


