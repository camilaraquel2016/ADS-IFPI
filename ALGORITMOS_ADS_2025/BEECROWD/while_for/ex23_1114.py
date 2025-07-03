def validar_senha(senha_permitida):
    while True:
        tentativa_de_senha = int(input())
        if tentativa_de_senha == senha_permitida:
            print('Acesso Permitido')
            break
        
        print('Senha Invalida')


def main():
    senha_permitida = 2002
    validar_senha(senha_permitida)

main()