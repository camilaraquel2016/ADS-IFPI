# # a e b
# # a = 0
# # b = 1
# # soma = a + b

# # obs: soma a partir do terceiro giro

# # a = b
# # b = soma;

def exibir_fibonacci(qtd_termos):
    a = 0
    b = 1
    soma = 0
    
    for i in range(qtd_termos):
        if i >= 2:
            soma = a + b
            print(soma)
            a = b
            b = soma
        else:
            print(i)


def main():
    qtd_termos = int(input('Quantidade de termos: '))
    exibir_fibonacci(qtd_termos)

main()    


