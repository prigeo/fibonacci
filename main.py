# Crie um programa onde o usuário informa o número de sequências de Fibonacci a ser calculada.

def calcular_fibo(n):
    if n <= 1:
        return n
    else:
        return calcular_fibo(n-1)+calcular_fibo(n-2)

# Programa principal
n = int(input('Informe o número de sequências fibonacci: '))
print(calcular_fibo(n))

# exibe a sequencia
for x in range(n):
    print(calcular_fibo(x))