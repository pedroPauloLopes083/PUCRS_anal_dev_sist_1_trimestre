#Programa que lê a altura e o gênero de alguém  e indica o peso ideal
altura = float(input('Insira a sua altura em metros (ex 1.70): '))
genero = int(input('Insira o seu gênero. Utilize 1 para feminino e 2 para masculino: '))

# Verifica se o gênero é válido
if genero > 2 or genero < 1:
    print('Erro')
else:
    if genero == 1:
        peso = 62.1 * altura - 44.7
    else:
        peso = 72.7 * altura - 58

    print("O seu peso ideal é:", peso)

#Programa que lê uma nota e escreva o conceito correspondente
nota=float(input('Insira a sua nota: '))
if nota>10 or nota<0 : print('Erro. Nota inválida')
elif nota>=9: print('Conceito A')
elif nota>=7: print('Conceito B')
elif nota>=5: print('Conceito C')
elif nota>=3: print('Conceito D')
else: print('Conceito E')
