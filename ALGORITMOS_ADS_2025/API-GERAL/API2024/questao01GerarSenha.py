#9:52

from random import randint

def calcularDiferenca(num1, num2):
    return num1 - num2 


def gerarNum0A9(antecessor):
    num = randint(0, 9)
    diferenca = calcularDiferenca(antecessor, num)
    if diferenca == 1 or diferenca == -1:
        num = gerarNum0A9(antecessor)
    return num 


def tamanhoSenha(senha):
    return len(senha)


def gerarSenha(qtdDig):
    senha = ''
    antecessor = -1
    
    while tamanhoSenha(senha) < qtdDig:
        num = gerarNum0A9(antecessor)
        if num != antecessor:
            senha += str(num)
            antecessor = num

    return senha    



def senhaFinal(qtdDig):
    resposta = 0

    while resposta != 1:
        senha = gerarSenha(qtdDig)
        print(f'Nova senha: {senha}')
        label = 'Você está satisfeito com essa senha? Digite 1 para SIM ou outro número para NÃO: '
        resposta = int(input(label))
    return senha    



    

    
    


def main():
    print('-=-GERADOR DE SENHA-=-')
    qtdDig = int(input('Quantidade de dígitos: '))
    senha = senhaFinal(qtdDig)
    print(f'Sua nova senha: {senha}')

main()
    


        














