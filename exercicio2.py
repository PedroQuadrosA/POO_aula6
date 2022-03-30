def fatorial(numero):
    fat = 1
    i = 1

    while  i <= numero:
        fat = fat * i
        i = i + 1
    return fat

n = int(input("Digite o valor da fatorial: ")) 
print(f"O valor de %d! eh = {fatorial(n)}" %n)
