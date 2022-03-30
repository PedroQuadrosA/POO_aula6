#Fazer potencia sem usar multiplicacao ou usar a funcao potencia do python

def potencia (base, expo): 
    i = 0
    j = 0
    aux = 0
    
    aux = base
    for i in range(0,int(expo-1)): #
        r = 0
        for j in range(0,int(aux)):
            r = r + base
        aux = r

    return aux

base = input("Base: ")
expoente = input("Expoente: ")
potencia(int(base),int(expoente))
print(f"O resultado da potencia eh: {potencia(int(base),int(expoente))}")
