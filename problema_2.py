def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

def main():
    while True:
        entrada = input("Informe um número para verificar se pertence à sequência de Fibonacci: ")
        
        # Verificar se a entrada não está vazia e se é um número válido
        if entrada.isdigit():
            numero = int(entrada)
            break
        else:
            print("Por favor, insira um número válido.")
    
    if fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
