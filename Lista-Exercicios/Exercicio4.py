#S0 = 0 eh ribeirao preto
#Para encontrar o sA e o sB devem ser iguais sA = sB
#Formula MRU S(t) = S0 + V * T


#Caminhao faz 2 pausas de 5 minutos
st = 0 + 22.23 + 18.94
print(f'tempo caminhao {st}')

sA = 0
vA = 30.56 #Conversao km/h para m/s

sB = 100000 #Conversao km para m
vB = -22.23 #Conversao km/h para m/s

t = 1000/(30.56 + 22.23)

print(f'Tempo de encontro {t:.2f} minutos')

sE = 30.56 * t

print(f'Ponto de encontro {sE:.2f} m')