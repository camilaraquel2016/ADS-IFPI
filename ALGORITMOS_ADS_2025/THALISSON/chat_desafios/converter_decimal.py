def converter_para_bin(num_decimal):
    num_binario = 0
    multiplicador = 1
        
    for i in range(num_decimal, 0, -1):
        
        resto = num_decimal % 2
        num_decimal //= 2

        num_binario += resto * multiplicador

        multiplicador *= 10

    return num_binario 
   

def main():
    num_decimal = int(input('Número decimal: '))
    num_bin = converter_para_bin(num_decimal)
    print(num_bin)


main()
