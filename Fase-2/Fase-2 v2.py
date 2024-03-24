import csv
from dateparser import parse
from collections import defaultdict

def dividir_data(data):
    """Divide a data em dia, mês e ano."""
    dia, mes, ano = data.split('/', maxsplit=2)
    return dia, mes, ano

def carregar_dados(arquivo):
    """Carrega os dados do arquivo CSV."""
    with open(arquivo, 'r') as f:
        return list(csv.reader(f))[1:]

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

    meses_validos = [str(i).zfill(2) for i in range(1, 13)]
    tipos_validos = ["todos", "precipitacao", "temperatura", "umidade_vento"]

    try:
        data_inicio = parse(f'{inicio_mes}/{inicio_ano}')
        data_fim = parse(f'{fim_mes}/{fim_ano}')
    except ValueError:
        print("Data inválida.")
        return

    if inicio_mes not in meses_validos or fim_mes not in meses_validos:
        print("Mês inválido.")
        return
    if inicio_ano < 2006 or fim_ano > 2016 or inicio_ano > fim_ano:
        print("Ano inválido.")
        return
    if tipo not in tipos_validos:
        print("Tipo de dado inválido.")
        return

    for linha in dados:
        data = linha[0]
        dia, mes, ano = dividir_data(data)
        if mes is None or dia is None or ano is None:
            print(f"Formato de data inválido para '{data}'.")
            continue

        if data_inicio <= parse(data) <= data_fim:
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
    return max(mes_precipitacao, key=mes_precipitacao.get)

def media_temperatura_minima_mensal(dados, mes_alvo):
    """Calcula a média da temperatura mínima para o mês alvo nos últimos 11 anos."""
    medias_por_ano = defaultdict(list)
    for linha in dados:
        data, temperatura_minima = linha[0], float(linha[3])
        mes, ano = data.split('/')[1:3]
        if mes == mes_alvo and int(ano) >= 2006 and int(ano) <= 2016:
            medias_por_ano[ano].append(temperatura_minima)
    return {ano: sum(temperaturas) / len(temperaturas) for ano, temperaturas in medias_por_ano.items()}

def media_geral_temperatura_minima_mensal(medias):
    """Calcula a média geral da temperatura mínima para o mês alvo nos últimos 11 anos."""
    total_temperaturas = sum(medias.values())
    qtd_anos = len(medias)
    return total_temperaturas / qtd_anos if qtd_anos != 0 else 0

# Carregar os dados do arquivo CSV
arquivo = 'Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv'
dados = carregar_dados(arquivo)

# Imprimir os resultados das funções
print("**Mês mais chuvoso:**", mes_mais_chuvoso(dados))
print("**Média da temperatura mínima para o mês alvo (01) nos últimos 11 anos:**")
media = media_temperatura_minima_mensal(dados, "01")
for ano, temperatura in media.items():
    print(f"Ano: {ano}, Média: {temperatura:.2f}°C")
print("**Média geral da temperatura mínima para o mês alvo (01) nos últimos 11 anos:**")
print("Média:", media_geral_temperatura_minima_mensal(media))
