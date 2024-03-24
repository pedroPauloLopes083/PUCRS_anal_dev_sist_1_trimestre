import csv
import matplotlib.pyplot as plt
from collections import defaultdict

def carregar_dados(arquivo):
    """Carrega os dados do arquivo CSV."""
    with open(arquivo, 'r') as f:
        return list(csv.reader(f))[1:]

def dividir_data(data):
    """Divide a data em dia, mês e ano."""
    dia, mes, ano = data.split('/', maxsplit=2)
    return dia, mes, ano

def media_temperatura_minima_mensal_por_ano(dados, mes_alvo):
    """Calcula a média da temperatura mínima para o mês alvo nos anos de 2006 a 2016."""
    medias_por_ano = defaultdict(list)
    for linha in dados:
        data, temperatura_minima = linha[0], float(linha[2])
        mes_csv = data.split('/')[1]
        if mes_csv == mes_alvo and 2006 <= int(data.split('/')[2]) <= 2016:
            medias_por_ano[data.split('/')[2]].append(temperatura_minima)
    return medias_por_ano

def media_geral_temperatura_minima(medias_por_ano):
    """Calcula a média geral da temperatura mínima para o mês alvo nos anos de 2006 a 2016."""
    temperaturas_totais = []
    for ano, temperaturas in medias_por_ano.items():
        temperaturas_totais.extend(temperaturas)
    return sum(temperaturas_totais) / len(temperaturas_totais)

def plotar_grafico_barras(medias_por_ano):
    """Plota um gráfico de barras com as médias de temperatura mínima por ano."""
    anos = list(medias_por_ano.keys())
    medias = [sum(medias_por_ano[ano]) / len(medias_por_ano[ano]) for ano in anos]

    plt.figure(figsize=(10, 6))
    plt.bar(anos, medias, color='skyblue')
    plt.xlabel('Ano')
    plt.ylabel('Média de Temperatura Mínima (°C)')
    plt.title('Média de Temperatura Mínima Mensal por Ano')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Carregar os dados do arquivo CSV
arquivo = 'Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv'
dados = carregar_dados(arquivo)

# Solicitar entrada do usuário para o período desejado
inicio_mes = input("Informe o mês inicial (MM): ")
inicio_ano = input("Informe o ano inicial (AAAA): ")
fim_mes = input("Informe o mês final (MM): ")
fim_ano = input("Informe o ano final (AAAA): ")

# Validar o período informado pelo usuário
meses_validos = [str(i).zfill(2) for i in range(1, 13)]
anos_validos = range(1961, 2017)

while inicio_mes not in meses_validos:
    inicio_mes = input("Mês inicial inválido. Por favor, informe novamente o mês inicial (MM): ")

while True:
    try:
        inicio_ano = int(inicio_ano)
        if inicio_ano not in anos_validos:
            raise ValueError
        break
    except ValueError:
        inicio_ano = input("Ano inicial inválido. Por favor, informe novamente o ano inicial (AAAA): ")

while fim_mes not in meses_validos:
    fim_mes = input("Mês final inválido. Por favor, informe novamente o mês final (MM): ")

while True:
    try:
        fim_ano = int(fim_ano)
        if fim_ano not in anos_validos or fim_ano < inicio_ano:
            raise ValueError
        break
    except ValueError:
        fim_ano = input("Ano final inválido. Por favor, informe novamente o ano final (AAAA): ")

# Filtrar os dados conforme o período informado pelo usuário
cabecalho = ["Data", "Precipitação (mm)", "Temperatura Mínima (°C)", "Umidade (%)", "Vento (m/s)"]
print(f"De: {inicio_mes}/{inicio_ano} - Até: {fim_mes}/{fim_ano}")
print(" ".join(cabecalho))

for linha in dados:
    data = linha[0]
    dia, mes, ano = dividir_data(data)
    if mes is None or dia is None or ano is None:
        print(f"Formato de data inválido para '{data}'.")
        continue

    if int(inicio_ano) <= int(ano) <= int(fim_ano) and inicio_mes <= mes <= fim_mes:
        print(" ".join(linha))

# Encontrar o mês/ano com maior precipitação considerando todos os dados
mes_precipitacao = defaultdict(float)
anos_precipitacao = defaultdict(str)  # Dicionário para armazenar o ano correspondente a cada mês
for linha in dados:
    data, precipitacao = linha[0], float(linha[1])
    mes_ano = data.split('/')[1]
    mes_precipitacao[mes_ano] += precipitacao
    # Armazenar o ano correspondente ao mês
    anos_precipitacao[mes_ano] = data.split('/')[2]

mes_ano_maior_precipitacao = max(mes_precipitacao, key=mes_precipitacao.get)
maior_precipitacao = mes_precipitacao[mes_ano_maior_precipitacao]

print(f"\nMês/Ano com maior precipitação: {mes_ano_maior_precipitacao}/{anos_precipitacao[mes_ano_maior_precipitacao]} com {maior_precipitacao} mm")

# Solicitar entrada do usuário para o mês desejado
mes_alvo = input("Informe o mês desejado (Ex: 08 para agosto): ")

# Validar o mês informado pelo usuário
if len(mes_alvo) != 2 or not mes_alvo.isdigit() or not 1 <= int(mes_alvo) <= 12:
    print("Mês inválido.")
else:
    # Calcular a média da temperatura mínima para o mês informado nos anos de 2006 a 2016
    medias_por_ano = media_temperatura_minima_mensal_por_ano(dados, mes_alvo)
    if not medias_por_ano:
        print(f"Não há dados disponíveis para o mês {mes_alvo} nos anos de 2006 a 2016.")
    else:
        # Exibir as médias da temperatura mínima por ano para o mês informado
        print(f"Médias da temperatura mínima para o mês {mes_alvo} nos anos de 2006 a 2016:")
        for ano, temperaturas in medias_por_ano.items():
            media = sum(temperaturas) / len(temperaturas)
            print(f"{ano}: {media:.2f} °C")
        
        # Calcular e exibir a média geral da temperatura mínima para o mês informado nos anos de 2006 a 2016
        media_geral = media_geral_temperatura_minima(medias_por_ano)
        print(f"Média geral da temperatura mínima para o mês {mes_alvo}: {media_geral:.2f} °C")

        # Plotar o gráfico de barras
        plotar_grafico_barras(medias_por_ano)
