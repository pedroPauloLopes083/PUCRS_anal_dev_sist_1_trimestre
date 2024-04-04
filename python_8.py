import random
lista = [] # lista vazia

for i in range (1,26):
    lista.append(random.randint(1,5))
print("Notas: ", lista)

conceito = []
quantidade= []
conceito.append('Excelente')
quantidade.append(lista.count(5))
conceito.append('Bom')
quantidade.append(lista.count(4))
conceito.append('Regular')
quantidade.append(lista.count(3))
conceito.append('Ruim')
quantidade.append(lista.count(2))
conceito.append('Péssimo')
quantidade.append(lista.count(1))

maiorQuantidade = quantidade[0]
maiorConceito = conceito[0]

for i in range (0,5):
    print(conceito[i], ' - ', quantidade[i])
    if quantidade[i] > maiorQuantidade:
        maiorQuantidade = quantidade[i]
        maiorConceito = conceito[i]

mediaVotacao = sum(lista)/25

print('Conceito mais votado: ', maiorConceito)
print(f'Recebeu {maiorQuantidade} votos!')
print('Média dos votos: ', mediaVotacao)