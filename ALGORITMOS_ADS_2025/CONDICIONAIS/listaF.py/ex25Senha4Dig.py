from utils import entradaInt

def senha_correta(senhaTentativa, senhaCorreta):
    return senhaTentativa == senhaCorreta


def pedirSenha():
    senha = entradaInt('Insira a senha de 4 dígitos: ')
    if senha >= 1000 and senha <= 9999:
        return senha
    else:
        print('Senha inválida! A senha deve possuir 4 dígitos')
        return pedirSenha()


def main():
    senha = pedirSenha()

    if senha_correta(senha, 1234):
        print('Senha correta!')
    else:
        print('Senha incorreta!')    
    

main()    