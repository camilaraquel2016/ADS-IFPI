def eh_raiz(num):
    possivel_raiz = 1
    resultado_raiz = 1
    

    while resultado_raiz <= num:
        if resultado_raiz == num:
            return True
        
        possivel_raiz += 1
        resultado_raiz = possivel_raiz ** 2
            
    return    


def main():
    num = int(input('Número: '))
    print(eh_raiz(num))

main()    