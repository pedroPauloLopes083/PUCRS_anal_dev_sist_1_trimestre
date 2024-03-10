#Programa que determina o preço de venda conforme o preço de custo do produto
custoproduto=float(input('Insira o preço de custo do produto: '))
if custoproduto<=0: print('Erro. Valor inválido')
if custoproduto<10: precovenda=custoproduto * 1.7 #lucro 70%
elif custoproduto>=10 and custoproduto<30: precovenda=custoproduto * 1.5 #lucro 50%
elif custoproduto>=30 and custoproduto<50: precovenda=custoproduto * 1.4 #lucro 40%
else: precovenda=custoproduto * 1.3 #lucro 30%

print('O preço de venda do produto informado é de: ', precovenda)

#Programa lê um valor inteiro e escreve o dia da semana correspondente
diasemana=int(input('Insira um valor inteiro de 1 a 7: '))
if diasemana<1 or diasemana>7: print('Erro. Insira um número de 1 a 7')
elif diasemana==1: print('O Dia da semana escolhido foi Domingo')
elif diasemana==2: print ('O dia da semana escolhido foi segunda-feira')
elif diasemana==3: print ('O dia da semana escolhido foi terça-feira')
elif diasemana==4: print ('O dia da semana escolhido foi quarta-feira')
elif diasemana==5: print ('O dia da semana escolhido foi quinta-feira')
elif diasemana==6: print ('O dia da semana escolhido foi sexta-feira')
else: print ('O dia da semana escolhido foi Sábado')