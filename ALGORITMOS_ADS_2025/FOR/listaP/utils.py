def obterNumInteiro(label: str):
    while True:
        try:
            num = int(input(label))
            return num
        except ValueError:
            print('Entrada inválida!\nO valor inserido deve ser um número inteiro')

