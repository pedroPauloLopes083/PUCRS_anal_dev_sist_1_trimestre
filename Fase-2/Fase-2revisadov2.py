import csv
import matplotlib.pyplot as plt
from collections import defaultdict

def carregar_dados(arquivo):
    """Carrega os dados do arquivo CSV."""
    with open(arquivo, 'r') as f:
        return list(csv.reader(f))

def dividir_data(data):
    """Divide a data em dia, mês e ano."""
    return data.split('/')

def validar_mes(mes):
    """Valida se o mês fornecido é válido."""
    return mes.isdigit() and 1 <= int(mes) <= 12

def validar_ano(ano):
    """Valida se o ano fornecido é válido."""
    return ano.isdigit() and 1961 <= int(ano) <= 2016

def mes_com_maior_precipitacao(dados):
    """Encontra o mês com a maior precipitação."""
    mes_precipitacao = defaultdict(float)
    for linha in dados[1:]:
        data, precipitacao = linha[0], float(linha[1])
        _, mes, ano = dividir_data(data)
        mes_ano = f"{mes}/{ano}"
        mes_precipitacao[mes_ano] += precipitacao
    return max(mes_precipitacao, key=mes_precipitacao.get), mes_precipitacao

def media_temperatura_minima_mensal_por_ano(dados, mes_alvo):
    """Calcula a média da temperatura mínima para o mês alvo nos anos de 2006 a 2016."""
    medias_por_ano = defaultdict(list)
    for linha in dados[1:]:
        data, temperatura_minima = linha[0], float(linha[2])
        _, mes, ano = dividir_data(data)
        if mes == mes_alvo and 2006 <= int(ano) <= 2016:
            medias_por_ano[ano].append(temperatura_minima)
    return medias_por_ano

def media_geral_temperatura_minima(medias_por_ano):
    """Calcula a média geral da temperatura mínima."""
    temperaturas_totais = [temp for temperaturas in medias_por_ano.values() for temp in temperaturas]
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
while not validar_mes(inicio_mes):
    inicio_mes = input("Mês inicial inválido. Por favor, informe novamente o mês inicial (MM): ")

while not validar_ano(inicio_ano):
    inicio_ano = input("Ano inicial inválido. Por favor, informe novamente o ano inicial (AAAA): ")

while not validar_mes(fim_mes):
    fim_mes = input("Mês final inválido. Por favor, informe novamente o mês final (MM): ")

while not validar_ano(fim_ano) or int(fim_ano) < int(inicio_ano):
    fim_ano = input("Ano final inválido. Por favor, informe novamente o ano final (AAAA): ")

# Solicitar ao usuário que escolha o tipo de dados a serem exibidos
tipo_dados = input("Escolha o tipo de dados a serem exibidos:\n"
                   "1) Todos os dados\n"
                   "2) Apenas os de precipitação\n"
                   "3) Apenas os de temperatura\n"
                   "4) Apenas os de umidade e vento\n"
                   "Opção: ")

# Validar a entrada do usuário para o tipo de dados
while tipo_dados not in ['1', '2', '3', '4']:
    tipo_dados = input("Opção inválida. Por favor, escolha uma opção válida: ")

# Filtrar os dados conforme o tipo selecionado pelo usuário
cabecalho = dados[0]
print(f"De: {inicio_mes}/{inicio_ano} - Até: {fim_mes}/{fim_ano}")

if tipo_dados == '1':
    print(" ".join(cabecalho))

for linha in dados[1:]:
    data = linha[0]
    _, mes, ano = dividir_data(data)
    if int(inicio_ano) <= int(ano) <= int(fim_ano) and inicio_mes <= mes <= fim_mes:
        if tipo_dados == '1':
            print(" ".join(linha))
        elif tipo_dados == '2':
            print(f"{linha[0]} {linha[1]}")
        elif tipo_dados == '3':
            print(f"{linha[0]} {linha[2]}")
        elif tipo_dados == '4':
            print(" ".join(linha[3:]))

# Encontrar o mês/ano com maior precipitação considerando todos os dados
mes_mais_chuvoso, precipitacao_mes = mes_com_maior_precipitacao(dados)
maior_precipitacao = precipitacao_mes[mes_mais_chuvoso]

print(f"\nMês com maior precipitação: {mes_mais_chuvoso} com {maior_precipitacao} mm")

mes_alvo = input("Informe o mês desejado (Ex: 08 para agosto) para calcular a média geral mensal da sua temperatura mínima entre os anos de 2006 e 2016: ")

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
    print(f"Média geral da temperatura mínima para o mês {mes_alvo} entre os anos de 2006 e 2016: {media_geral:.2f} °C")

    # Plotar o gráfico de barras
    plotar_grafico_barras(medias_por_ano)
