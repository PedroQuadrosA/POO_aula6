def criar_matriz(linhas,colunas,valor):
    matriz = []
    for i in range (linhas):
        linha = []
        for j in range (colunas):
            linha.append(valor)
            

        matriz.append(linha)
        
    return matriz


matriz = criar_matriz(2,2,0)
print(matriz)
