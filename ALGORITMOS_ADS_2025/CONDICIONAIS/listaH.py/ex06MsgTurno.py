def menu():
    print('M - matutino\nV - vespertino\nN - noturno')

def saudacoes(nome, turno):
    if turno == 'M':
        return f'Bom dia, {nome}'    
    elif turno == 'T':
        return f'Boa tarde, {nome}'
    elif turno == 'N':
        return f'Boa noite, {nome}'
    else:
        return 'turno inválido'
    

def main():
    nome = str(input('Qual seu nome? '))    
    menu()
    turno = str(input('Qual turno desejado? (M/V/N) ')).upper()
    msgSaudacoes = saudacoes(nome, turno)
    print(msgSaudacoes)

main()    