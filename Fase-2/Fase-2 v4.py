import csv
from dateparser import parse
from collections import defaultdict
import matplotlib.pyplot as plt

def dividir_data(data):
  """Divide a data em dia, mês e ano."""
  dia, mes, ano = data.split('/', maxsplit=2)
  return dia, mes, ano

def formatar_data(data):
  """Formata a data do formato dd/mm/aaaa para dd/mm/aa."""
  dia, mes, ano = dividir_data(data)
  return f'{dia}/{mes}/{ano[-2:]}' if dia and mes and ano else 'Data inválida'

def visualizar_dados(dados, inicio_mes, inicio_ano, fim_mes, fim_ano, tipo):
  """Visualiza os dados no intervalo especificado."""
  cabecalho = ["Data", "Precipitação (mm)", "Temperatura Mínima (°C)", "Umidade (%)", "Vento (m/s)"]

  print("**Intervalo de Dados**")
  print(f"De: {inicio_mes}/{inicio_ano} - Até: {fim_mes}/{fim_ano}")
  print(" ".join(cabecalho))

  # Validação do formato do mês
  meses_validos = [str(i).zfill(2) for i in range(1, 13)]
  if inicio_mes not in meses_validos or fim_mes not in meses_validos:
    print("Mês inválido.")
    return

  # Validação do formato do ano
  if inicio_ano < 2006 or fim_ano > 2016 or inicio_ano > fim_ano:
    print("Ano inválido.")
    return

  # Visualização dos dados
  for linha in dados:
    data = linha[0]
    dia, mes, ano = dividir_data(data)
    if mes is None or dia is None or ano is None:
      print(f"Formato de data inválido para '{data}'.")
      continue

    if inicio_ano <= ano <= fim_ano and (inicio_mes <= mes <= fim_mes or fim_mes == '12' and mes == '01'):
      if tipo == "todos":
        print(" ".join(linha))
      elif tipo == "precipitacao":
        print(f"{linha[0]} {linha[1]}")
      elif tipo == "temperatura":
        print(f"{linha[0]} {linha[2]} {linha[3]}")
      elif tipo == "umidade_vento":
        print(f"{linha[0]} {linha[4]} {linha[5]}")


def mes_mais_chuvoso(dados):
  """Encontra o mês mais chuvoso."""
  mes_precipitacao = defaultdict(float)
  for linha in dados:
    mes_ano, precipitacao = linha[0], float(linha[1])
    mes = mes_ano.split('/')[0]
    mes_precipitacao[mes] += precipitacao
  mes_mais_chuvoso, maior_precipitacao = max(mes_precipitacao, key=mes_precipitacao.get)

  # Imprime o resultado
  print(f'Mês mais chuvoso: {mes_mais_chuvoso}')
  print(f'Maior precipitação: {float(maior_precipitacao):.2f} mm')  # Converte para float antes de formatar

  return mes_mais_chuvoso, maior_precipitacao

def media_temperatura_minima_mensal(dados, mes_alvo):
  """Calcula a média da temperatura mínima para o mês alvo nos últimos 11 anos."""
  medias_por_ano = defaultdict(list)
  for linha in dados:
    data, temperatura_minima = linha[0], float(linha[3])
    mes, ano = data.split('/')[1:3]
    if mes == mes_alvo and int(ano) >= 2006 and int(ano) <= 2016:
      medias_por_ano[ano].append(temperatura_minima)

  # Imprime as médias anuais e a média geral              
    for ano, temperaturas in medias_por_ano.items():
        media = sum(temperaturas) / len(temperaturas)
        print(f"Ano {ano}: {media:.2f} °C")
    media_geral = sum(temperatura for ano, temperaturas in medias_por_ano.items() for temperatura in temperaturas) / len(list(medias_por_ano.values()))
    print(f"Média geral: {media_geral:.2f} °C")

    return medias_por_ano

def carregar_dados(arquivo):
  """Carrega os dados do arquivo CSV."""
  with open(arquivo, 'r') as f:
    return list(csv.reader(f))[1:]

def main():
  """Função principal do programa."""
  # Carrega os dados do arquivo CSV
  arquivo = 'Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv'
  dados = carregar_dados(arquivo)

  while True:
    # Opção 1: Visualizar dados
    inicio_mes = int(input("Digite o mês inicial (MM): "))

    # Validação do mês inicial
    meses_validos = [int(i) for i in range(1, 13)]
    if inicio_mes not in meses_validos:
      print(f"Mês inicial inválido: {inicio_mes}. Digite um valor entre 01 e 12.")
      continue

    inicio_ano = int(input("Digite o ano inicial (AAAA): "))

    # Validação do ano inicial
    anos_iniciais_validos = [int(i) for i in range(1961, 2016)]
    if inicio_ano not in anos_iniciais_validos:
      print("Ano inicial inválido. Digite um valor numérico com quatro dígitos, entre 1961 e 2016.")
      continue

    # Validação do mês final
    fim_mes = int(input("Digite o mês final (MM): "))

    # Validação do mês final
    meses_validos = [int(i) for i in range(1, 13)]
    if fim_mes not in meses_validos:
      print(f"Mês inicial inválido: {fim_mes}. Digite um valor entre 01 e 12.")
      continue

    fim_ano = int(input("Digite o ano inicial (AAAA): "))

    # Validação do ano final
    anos_finais_validos = [int(i) for i in range(1961, 2016)]
    if fim_ano not in anos_finais_validos:
      print("Ano final inválido. Digite um valor numérico com quatro dígitos, entre 1961 e 2016.")
      continue

    # Validação da ordem dos anos
    if inicio_ano > fim_ano:
      print("Ano inicial não pode ser maior que o ano final.")
      continue

    # Validação do tipo de dado
    tipo = input("Digite o tipo de dado (todos, precipitacao, temperatura, umidade_vento): ")

    # Validação do tipo de dado
    if tipo not in ["todos", "precipitacao", "temperatura", "umidade_vento"]:
      print(f"Tipo de dado inválido: {tipo}. Digite um dos tipos válidos: todos, precipitacao, temperatura, umidade_vento.")
      continue

    break

  parametros = (dados, inicio_mes, inicio_ano, fim_mes, fim_ano, tipo)
  visualizar_dados(*parametros)  # Desempacota a lista/tupla como argumentos individuais

if __name__ == "__main__":
  main()

