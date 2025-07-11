def obter_mensagem(n):
    mensagem = ''

    for ho in range(n):
        if ho < n - 1:
            mensagem += 'Ho '
        else:
            mensagem += 'Ho!'    

    return mensagem     
        

def main():
    n = int(input())
    mensagem = obter_mensagem(n)
    print(mensagem)

main()    

