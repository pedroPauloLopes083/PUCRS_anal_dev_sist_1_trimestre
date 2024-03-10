#Programa de conversão de Farenheit para Celsius
farenheit=float(input("Escreva o valor em graus Farenheit: "))
celsius= 5/9*(farenheit - 32)
print(f"O valor inserido em graus Celsius é igual a {celsius}º C" )

#Programa que lê o tempo em horas e o decompõe em minutos e segundos
horas=int(input("Insira a quantidade de horas: "))
minutos=horas*60
segundos=minutos*60
print(f"A quantidade de horas informadas é igual em minutos a {minutos} e em segundos a {segundos}")

#Programa que lê o tempo em segundos e o decompõe em minutos e horas
segundo=int(input("Insira a quantidade de segundos: "))
minutos=segundos/60
horas=minutos/60
print(f"A quantidade de segundos informados é em minutos igual {minutos} e em horas igual a {horas}")

#Programa que lê um valor inteiro de 4 dígitos e o escreve na ordem inversa
valor=int(input("Insira um valor inteiro de 4 dígitos"))
if valor < 1000 or valor > 9999:
    print("Por favor, digite um valor inteiro de 4 dígitos.")
else: 
    m=valor//1000
    c=(valor%1000)//100
    d=(valor%100)//10
    u=valor % 10
    numeroinvertido= u * 1000 + d * 100 + c * 10 + m
    print(f"O número inserido invertido é igual a {numeroinvertido}")
