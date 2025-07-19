# def eh_alfabetica(caractere):
#     codigo = ord(caractere)
#     return (codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122)


def eh_numero(caractere):
    codigo = ord(caractere)
    return codigo >= 48 and codigo <= 57
    

def obter_nova_string(string):
    nova_string = ''

    for caractere in string:
        if caractere == 'O' or caractere == 'o':
            nova_string += '0'
        elif caractere == 'l':
            nova_string += '1'
        elif eh_numero(caractere):
            nova_string += caractere    

    return nova_string          
                

def validar_nova_string(nova_string):
    try:
        num = int(nova_string)
        if num > 2147483647:
            return 'error'
        elif num == 0:
            return num
        elif len(nova_string) > 0 and nova_string[0] == '0':
            return 'error'
        else:
            return num
        
    except ValueError:
        return 'error'


def main():
    try:
        while True:
            string = input()
            if not string:
                break

            nova_string = obter_nova_string(string)
            print(validar_nova_string(nova_string))

    except EOFError:
        pass        

main()





def obter_nova_string(string):
    nova_string = ''

    for caractere in string:
        if caractere == 'o' or caractere == 'O':
            nova_string += '0'
        elif caractere == 'l':  # Somente 'l' minúsculo vira 1
            nova_string += '1'
        elif caractere.isdigit():
            nova_string += caractere
        # Qualquer outra letra ou caractere é ignorado

    return nova_string

def validar_nova_string(nova_string):
    if len(nova_string) == 0:
        return 'error'

    if nova_string != '0' and nova_string[0] == '0':
        return 'error'

    try:
        numero = int(nova_string)
        if numero > 2147483647:
            return 'error'
        return numero
    except:
        return 'error'

def main():
    try:
        while True:
            entrada = input()
            if not entrada:
                break
            
            nova_string = obter_nova_string(entrada)
            print(validar_nova_string(nova_string))
    except EOFError:
        pass
