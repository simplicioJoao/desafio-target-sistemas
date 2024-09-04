numero = int(input("Informe um número: "))
sequenciaFibonacci = [0, 1]
i = 1
numeroEncontrado = False

while sequenciaFibonacci[i] < numero:
    sequenciaFibonacci.append(sequenciaFibonacci[i] + sequenciaFibonacci[i - 1])
    i += 1
print(sequenciaFibonacci)

for valor in sequenciaFibonacci:
    if valor == numero:
        numeroEncontrado = True

if numeroEncontrado == True:
    print(f"O número {numero} pertence à sequência de Fibonacci")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci")