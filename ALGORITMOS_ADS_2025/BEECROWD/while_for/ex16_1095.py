def exibir_sequencia():
    i, j = 1, 60

    while True:
        print(f'I={i} J={j}')
        if j == 0:
            break
        i += 3
        j -= 5
        

def main():
    exibir_sequencia()

main()    
