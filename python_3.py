#Programa que lê 3 valores e escreve o maior deles
valor1=float(input('Insira um valor númerico: '))
valor2=float(input('Insira um valor númerico: '))
valor3=float(input('Insira um valor númerico: '))

if valor1>=valor2 and valor1>valor3: maior =valor1
elif valor2>valor1 and valor2>=valor3: maior = valor2
elif valor3>=valor1 and valor3>valor2: maior = valor3

print('O maior valor inserido é: ', maior)

#Programa que lê 5 valores e escreve o maior deles (outra forma)
valor1=float(input('Insira um valor númerico: '))
valor2=float(input('Insira um valor númerico: '))
valor3=float(input('Insira um valor númerico: '))
valor4=float(input('Insira um valor númerico: '))
valor5=float(input('Insira um valor númerico: '))

maior= valor1

if valor2>maior: maior=valor2
if valor3>maior: maior=valor3
if valor4>maior: maior=valor4
if valor5>maior: maior=valor5

print('O maior valor dos cinco valores inseridos é: ', maior)