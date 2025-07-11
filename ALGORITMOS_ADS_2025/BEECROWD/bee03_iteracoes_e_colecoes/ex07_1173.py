def repetir(qtd_vezes, v):

    for vez in range(qtd_vezes):
        print(f'N[{vez}] = {v}')
        v *= 2



def main():
    v = int(input())
    repetir(10, v)

main()    

