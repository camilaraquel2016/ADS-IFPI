def exibirSexo(resposta: str):
    return 'Feminino' if resposta == 'F' else 'Masculino' if resposta == 'M' else 'inválido'


def menu():
    print('F - Feminino\nM - Masculino')
    
def main():
    menu()
    resposta = str(input('Digite seu sexo: (F/M) '))
    sexo = exibirSexo(resposta)
    print(f'Seu sexo é {sexo}')

main()    


