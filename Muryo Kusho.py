def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return 'Conta invalida'

print("Selecione a operação:")
print("1. Adição")
print('2. Subtração')
print("4. Multiplicação")
print("3. Divisão")

# Obter entrada do usuário
escolha = input("Digite o número da operação desejada (1/2/3/4): ")

# Obter números de entrada
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Executar a operação selecionada
if escolha == '1':
    print(num1, "+", num2, "=", adicao(num1, num2))
elif escolha == '2':
    print(num1, '-')
elif escolha == '3':
    print(num1, "*", num2, "=", multiplicacao(num1, num2))
elif escolha == '4':
    print(num1, "/", num2, "=", divisao(num1, num2))
else:
   print('Não foi possivel realizar essa conta')