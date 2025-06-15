from utils import obterNumInt, validarLimiteMin
#esse programa retorna apenas divisores naturais, e não aceita valores de entrada negativa!

def encontrarOsDivisores(num: int):
    divisor = 1 #estado anterior
    divisores = []

    while divisor <= num: #condição de continuidade 
        #trabalho
        if num % divisor == 0:
            divisores.append(divisor) 
        #convergência de dados    
        divisor += 1
    return divisores


def main():
    label = 'Insira um número para encontramos todos seus divisores: (flag = 0) '
    #estado anterior
    num = obterNumInt(label)
    num = validarLimiteMin(num, 0, label) 

    while num != 0: #condição de continuidade
        # trabalho
        divisores = encontrarOsDivisores(num)
        print(f'Os divisores de {num} são: {divisores}')
        #convergência de dados
        num = obterNumInt(label)
        num = validarLimiteMin(num, 0, label)

    print('Encerrando programa...')    


main()





