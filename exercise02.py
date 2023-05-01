num = int(input("\nDigite um número para verificar se pertence à sequência de Fibonacci: "))

fibonacci = [0, 1]
while fibonacci[-1] < num:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if num in fibonacci:
    print(f"O número {num} faz parte da sequência de Fibonacci!")
else:
    print(f"O número {num} não faz parte da sequência de Fibonacci.")

print("Sequência de Fibonacci:")
print(fibonacci[:-1])
