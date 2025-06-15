# 73 - 37 = 36 

def inverter(texto):
    novo_texto = ''

    for caractere in texto:
        novo_texto = caractere + novo_texto

    return novo_texto    


def descobrir_idade():
    contador = 0
    idade_mae = 36

    while True:
        idade_filho = idade_mae - 36

        if str(idade_mae) == inverter(str(idade_filho)):
            contador += 1
           
            if contador == 5:
                return idade_filho
        
        idade_mae += 1


def main():
    idade_atual_filho = descobrir_idade()
    print(f'Idade atual do filho: {idade_atual_filho}')

main()
        

