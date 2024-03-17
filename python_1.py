import math

#Fórmula para calcular o volume de uma esfera
#v=4/3*PI*raio³

raio=float(input("Informe o raio para calcular o volume: "))
volume=4/3 * math.pi * math.pow(raio,3)

print("O volume é: ", volume)

#Programa que lê dois valores inteiros e escreve a soma
val1=int(input("insira um valor inteiro: "))
val2=int(input("insira um segundo valor inteiro: "))
soma= val1 + val2
print("A soma dos dois valores inseridos é: ", soma)

#Programa que lê dois valores inteiros e escreve a diferença
val1=int(input("insira um valor inteiro: "))
val2=int(input("insira um segundo valor inteiro: "))
diferença= val1 - val2
print("A diferença entre os dois valores inseridos é de: ", diferença)

#Programa que lê dois valores inteiros e escreve a média
val1=int(input("insira um valor inteiro: "))
val2=int(input("insira um segundo valor inteiro: "))
media= (val1 + val2)/2
print("A média dos dois valores inseridos é: ", media)

#Programa que lê dois valores inteiros e escreve a distância (valor absoluto da diferença)
val1=int(input("insira um valor inteiro: "))
val2=int(input("insira um segundo valor inteiro: "))
distancia= abs(val1 - val2)
print("O valor absoluto da dieferença dos dois valores inseridos é: ", distancia)

#Programa que lê dois valores inteiros e escreve o maior dos dois valores
val1=int(input("insira um valor inteiro: "))
val2=int(input("insira um segundo valor inteiro: "))
maior= (val1 + val2 + abs(val1 - val2))/2
print("O maior dos dois valores inseridos é: ", maior)

#Programa que lê dois valores inteiros e escreve o menor dos dois valores
val1=int(input("insira um valor inteiro: "))
val2=int(input("insira um segundo valor inteiro: "))
menor= (val1 + val2 -abs(val1 - val2))/2
print("O menor dos dois valores inseridos é: ", menor)
