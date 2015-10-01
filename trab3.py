lst = ["zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oita", "nove"]

def numeros(n):
    for x in str(n):
        x = int(x)
        print(lst[x])
    return 0

def numeros2(n):
    for x in range(len(lst)):
        if vet[x] == n:
            return x
    return 0

numeros(123)
