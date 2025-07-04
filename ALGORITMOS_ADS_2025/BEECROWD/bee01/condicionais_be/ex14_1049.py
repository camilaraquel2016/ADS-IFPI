def obter_animal(classificacao1, classificacao2, classificacao3):
    if classificacao1 == 'vertebrado':
        if classificacao2 == 'ave':
            if classificacao3 == 'carnivoro':
                return 'aguia'
            else:
                return 'pomba'
        else:
            if classificacao3 == 'onivoro':
                return 'homem'
            else:
                return 'vaca'
    else:
        if classificacao2 == 'inseto':
            if classificacao3 == 'hematofago':
                return 'pulga'
            else:
                return 'lagarta'
        else:
            if classificacao3 == 'hematofago':
                return 'sanguessuga'
            else:
                return 'minhoca'                


def main():
    classificacao1 = input()
    classificacao2 = input()
    classificacao3 = input()

    animal = obter_animal(classificacao1, classificacao2, classificacao3)
    print(animal)

main()    



