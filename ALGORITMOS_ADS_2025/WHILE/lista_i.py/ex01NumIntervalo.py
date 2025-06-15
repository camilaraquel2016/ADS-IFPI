from utils import obterNumInt, validarLimiteMin

def listarNumeros(ultimoNum: int):
    num = 1 # estado anterior 
    
    while num <= ultimoNum: # condicão de continuidade
        print(num, end = ' ') # trabalho
        if num < ultimoNum:
            print('-', end = ' ')
       
        num +=1 # convergÊncia dos dados
        
      
def main():
    label = 'Deseja listar de 1 até quanto? '
    num = obterNumInt(label)
    num = validarLimiteMin(num, 1, label)

    listarNumeros(num)


main()    


