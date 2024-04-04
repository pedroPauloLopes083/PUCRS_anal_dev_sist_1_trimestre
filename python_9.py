import random
lista = [] # lista vazia

for i in range (1,21):
    lista.append(random.randint(0,100))
print("Idades: ", lista)

mediaIdade = sum(lista)/20
maiorIdade = max(lista)
menorIdade = min(lista)

print(f'A média de idade é de: {mediaIdade}')
print(f'A maior idade da lista é: {maiorIdade}')
print(f'A menor idade da lisa é: {menorIdade}')