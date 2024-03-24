import csv
from subprocess import DETACHED_PROCESS


# Função para carregar os dados do arquivo CSV
def carregar_dados(arquivo):
    with open(arquivo, 'r') as f:
        dados = list(csv.reader(f))
    return dados

# Função para formatar a data
def formatar_data(data):
    dia, mes, ano = data.split('/')
    return f'{dia}/{mes}/{ano[:2]}'

# Função para visualizar os dados
def visualizar_dados(dados, inicio, fim, tipo):
    print(f'**Dados de {formatar_data(inicio)} a {formatar_data(fim)}**')
    if tipo == 'todos':
        for linha in dados[1:]:
            print(linha)
    elif tipo in ('precipitacao', 'temperatura', 'umidade_vento'):
        for linha in dados[1:]:
            if tipo == 'precipitacao':
                print(f'{linha[0]} - Precipitação: {linha[1]} mm')
            elif tipo == 'temperatura':
                print(f'{linha[0]} - T. Máxima: {linha[2]}°C - T. Mínima: {linha[3]}°C')
            elif tipo == 'umidade_vento':
                print(f'{linha[0]} - Umidade: {linha[4]}% - Vento: {linha[5]} m/s')
    else:
        print('Tipo inválido!')

# Função para encontrar o mês mais chuvoso
def mes_mais_chuvoso(dados):
    mes_ano = {}
    for linha in dados[1:]:
        mes_ano[linha[0]] = mes_ano.get(linha[0], 0) + float(linha[1])
    maior_mes, maior_precipitacao = max(mes_ano.items(), key=lambda x: x[1])
    return maior_mes, maior_precipitacao

# Encontrar o mês mais chuvoso
mes_mais_chuvoso, maior_precipitacao = mes_mais_chuvoso(DETACHED_PROCESS)

# Exibir o resultado
print(f'Mês mais chuvoso: {mes_mais_chuvoso}')
print(f'Maior precipitação: {maior_precipitacao} mm')


# Função para calcular a média da temperatura mínima
def media_temperatura_minima(dados, mes, ano_inicio, ano_fim):
    medias = {}
    for ano in range(ano_inicio, ano_fim + 1):
        mes_ano = f'{mes}{ano:02}'
        medias[mes_ano] = []
        for linha in dados[1:]:
            if linha[0] == mes_ano:
                medias[mes_ano].append(float(linha[3]))
    for mes_ano, temperaturas in medias.items():
        medias[mes_ano] = sum(temperaturas) / len(temperaturas)
    return medias

# Função para gerar o gráfico de barras
def gerar_grafico_barras(medias):
    import matplotlib.pyplot as plt
    meses = []
    temperaturas = []
    for mes_ano, media in medias.items():
        meses.append(mes_ano[:2])
        temperaturas.append(media)
    plt.bar(meses, temperaturas)
    plt.xlabel('Mês')
    plt.ylabel('Temperatura Mínima (°C)')
    plt.title('Média da Temperatura Mínima')
    plt.show()

# Leitura do arquivo CSV
dados = carregar_dados('Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv')

# a) Visualização de intervalo de dados
inicio = input('Digite a data inicial (dd/mm/aa): ')
fim = input('Digite a data final (dd/mm/aa): ')
tipo = input('Digite o tipo de dado (todos, precipitacao, temperatura, umidade_vento): ')
visualizar_dados(dados, inicio, fim, tipo)

# b) Mês mais chuvoso
mes_mais_chuvoso, maior_precipitacao = mes_mais_chuvoso(dados)
print(f'Mês mais chuvoso: {mes_mais_chuvoso}')
print(f'Maior precipitação: {maior_precipitacao} mm')

# c) Média da temperatura mínima
mes = input('Digite o mês (mm): ')
ano_inicio = int(input('Digite o ano inicial (aaaa): '))
ano_fim = int(input('Digite o ano final (aaaa): '))
medias = media_temperatura_minima(dados, mes, ano_inicio, ano_fim)

# d) Gráfico de barras
gerar_grafico_barras(medias)

# e) Média geral da temperatura mínima
media_geral = sum(medias.values()) / len(medias)
print(f'Média geral da temperatura mínima: {media_geral:.2f}°C')

