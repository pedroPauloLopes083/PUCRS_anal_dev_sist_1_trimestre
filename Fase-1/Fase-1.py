# Dicionário para os meses
meses = {
  1: "Janeiro",
  2: "Fevereiro",
  3: "Março",
  4: "Abril",
  5: "Maio",
  6: "Junho",
  7: "Julho",
  8: "Agosto",
  9: "Setembro",
  10: "Outubro",
  11: "Novembro",
  12: "Dezembro"
}

# Dicionário para armazenar as temperaturas máximas mensais
temperaturas = {}

# Função para validar se a temperatura está entre -60°C e 50°C.
def valida_temperatura(temperatura):
  if -60 <= temperatura <= 50:
    return True
  else:
    return False

# Loop para coletar as temperaturas máximas mensais
for mes in range(1, 13):
  while True:
    temperatura = float(input(f"Informe a temperatura máxima do mês {mes} em 2021: "))
    if valida_temperatura(temperatura):
      temperaturas[mes] = temperatura
      break
    else:
      print(" ----Erro! A temperatura deve estar entre -60°C e 50°C.---- ")

# Cálculo da temperatura máxima média anual
soma_temperaturas = 0
for temperatura in temperaturas.values():
  soma_temperaturas += temperatura
temp_maxima_media = soma_temperaturas / len(temperaturas)

# Contagem de meses escaldantes
meses_escaldantes = 0
for temperatura in temperaturas.values():
  if temperatura > 33:
    meses_escaldantes += 1

# Encontrar o mês mais escaldante
mes_mais_escaldante = None
temperatura_mais_escaldante = None
for mes, temperatura in temperaturas.items():
  if temperatura_mais_escaldante is None or temperatura > temperatura_mais_escaldante:
    mes_mais_escaldante = mes
    temperatura_mais_escaldante = temperatura

# Encontrar o mês mais frio (ou menos escaldante)
mes_mais_frio = None
temperatura_mais_fria = None
for mes, temperatura in temperaturas.items():
  if temperatura_mais_fria is None or temperatura < temperatura_mais_fria:
    mes_mais_frio = mes
    temperatura_mais_fria = temperatura

# Exibir os resultados
print(f"Temperatura máxima média anual: {temp_maxima_media:.2f}°C")
print(f"Quantidade de meses escaldantes (acima de 33°C): {meses_escaldantes}")
print(f"Mês mais escaldante: {meses[mes_mais_escaldante]} ({temperaturas[mes_mais_escaldante]:.2f}°C)")
print(f"Mês mais frio: {meses[mes_mais_frio]} ({temperaturas[mes_mais_frio]:.2f}°C)")