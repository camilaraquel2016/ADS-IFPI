from time import sleep

def exibirRequisitos():
    return '''-=-=-Requisistos para criar uma senha-=-=-

    - Pelo menos 8 caracteres
    - Pelo menos uma letra maiúscula 
    - Pelo menos uma letra minúscula
    - Pelo menos um número
    - Pelo menos um caractere especial(!, @, #, $, %, &, *)

 '''


def removerEspacos(texto: str):
    return texto.replace(' ', '')


def contarCaractere(texto):
    return len(texto)


def criterioMin8Caracteres(texto):
    texto = removerEspacos(texto)
    quantCaractere = contarCaractere(texto)
    return quantCaractere >= 8


def criterioMin1Numero(texto: str):
    quantNum = sum(1 for caractere in texto if caractere in '0123456789')
    return quantNum >= 1 


def criterioMin1Especial(texto: str):
    quantCaractereEspecial = sum(1 for caractere in texto if caractere in '!@#$%&*') 
    return quantCaractereEspecial >= 1


def criterioMin1Maiuscula(texto: str):
    quantCaractereMaiusculo = sum(1 for caractere in texto if caractere.isupper())
    return quantCaractereMaiusculo >= 1


def criterioMin1Minusculo(texto: str):
    quantCaractereMinusculo = sum(1 for letra in texto if letra.islower())
    return quantCaractereMinusculo >= 1


def eh_senha_valida(texto: str):
    return criterioMin8Caracteres(texto) and criterioMin1Maiuscula(texto) and criterioMin1Minusculo(texto) and criterioMin1Especial(texto) and criterioMin1Numero(texto)


def validarSenha(texto: str):
    if eh_senha_valida(texto):
        return True
    else:
        print('Senha inválida, não atende os requisistos necessários!')
        sleep(2)
        print(exibirRequisitos())
        texto = str(input('Digite a nova senha: '))
        return validarSenha(texto)


def main():
    print(exibirRequisitos())

    senha = str(input('Digite a senha que deseja criar: '))

    validarSenha(senha)

    print('Senha criada com sucesso!')


main()

