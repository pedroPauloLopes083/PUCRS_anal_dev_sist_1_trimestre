#Programa que lê 3 notas e calcula a média ponderada, 
#considerando os pesos 5 , 2.5 e 2.5; a maior nota tem peso 5

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Identifica a maior nota e atribui os pesos correspondentes
if nota1 >= nota2 and nota1 >= nota3:
    peso_nota1 = 5
    peso_nota2 = 2.5
    peso_nota3 = 2.5
elif nota2 >= nota1 and nota2 >= nota3:
    peso_nota1 = 2.5
    peso_nota2 = 5
    peso_nota3 = 2.5
else:
    peso_nota1 = 2.5
    peso_nota2 = 2.5
    peso_nota3 = 5

# Calcula a média ponderada
media_ponderada = (nota1 * peso_nota1 + nota2 * peso_nota2 + nota3 * peso_nota3) / (peso_nota1 + peso_nota2 + peso_nota3)

# Imprime o resultado
print("A média ponderada das notas é:", media_ponderada)
