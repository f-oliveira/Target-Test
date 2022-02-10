#Exercício 3

#A - 1,3,5,7,
def exA(a):
    r = 3 - 1
    x = 1 + (a-1)*r
    return print(f'O proximo termo: {x}')
    
#B 2,4,8,16,32,64
def exB(b):
    r = 4 / 2
    x = 2*(r**(b-1))
    print(f'O proximo termo: {x:.0f}')
        
#C 0,1,4,9,16,32,49
def exC(c):
    x = (c-1)**2
    return print(f'O proximo termo: {x}')

#D 4,16,36,64
def exD(d):
    r = 28 + 8
    x = d + r
    return print(f'O proximo termo: {x}')

#E 1,1,2,3,5,8
def exE(e):
    if e == 1:
        return 0
    elif e == 2:
        return 1
    else:
        return exE(e-1) + exE(e-2)
        
#F 2,10,12,16,17,18,19
print(f'O proximo termo: 200. Nao achei uma forma logica de calcular o valor, apenas supondo que todos comecem com a leta D')


exA(5)
print('\n')
exB(7)
print('\n')
exC(8)
print('\n')
exD(64)
print('\n')
print(f'O proximo termo: {exE(8)}')