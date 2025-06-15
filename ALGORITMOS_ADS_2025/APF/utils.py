def obter_num_inteiro(label: str):
    while True:
        try:
            num = int(input(label))
            return num
        except ValueError:
            print('Entrada inválida!')


def obter_num_real(label: str):
    while True:
        try:
            num = float(input(label))
            return num
        except ValueError:
            print('Entrada inválida!')


            
            
