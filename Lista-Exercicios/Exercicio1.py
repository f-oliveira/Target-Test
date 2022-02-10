#Exercicio 1

def somar(INDICE,SOMA,K):
    while(K < INDICE):
        K += 1
        SOMA += K
    return SOMA


INDICE = 13
SOMA = 0
K = 0

print(f'Exercicio 1: {somar(INDICE,SOMA,K)}')