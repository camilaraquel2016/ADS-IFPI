def eh_minuscula(letra):
    codigo = ord(letra)
    return codigo >= 97 and codigo <= 122

def obter_mensagem_decodificada(msg_codificada):
    msg_decodificada = ''

    for letra in msg_codificada:
        if eh_minuscula(letra):
            msg_decodificada = letra + msg_decodificada

    return msg_decodificada


def repetir(qtd_casos):
    for caso in range(qtd_casos):
        codigo = input()
        mensagem_decodificada = obter_mensagem_decodificada(codigo)
        print(mensagem_decodificada)


def main():
    qtd_casos  = int(input())
    repetir(qtd_casos)

main()   
