import csv
from collections import defaultdict

def carregar_dados(arquivo):
    """Carrega os dados do arquivo CSV."""
    with open(arquivo, 'r') as f:
        return list(csv.reader(f))[1:]

def maior_precipitacao_total(dados):
    """Encontra o mês/ano com maior precipitação considerando todos os dados."""
    mes_precipitacao = defaultdict(float)
    for linha in dados:
        data, precipitacao = linha[0], float(linha[1])
        mes_ano = "/".join(data.split('/')[1:])  # Obtém o mês/ano
        mes_precipitacao[mes_ano] += precipitacao

    mes_ano_maior_precipitacao = max(mes_precipitacao, key=mes_precipitacao.get)
    maior_precipitacao = mes_precipitacao[mes_ano_maior_precipitacao]
    return mes_ano_maior_precipitacao, maior_precipitacao

def dividir_data(data):
    """Divide a data em dia, mês e ano."""
    dia, mes, ano = data.split('/', maxsplit=2)
    return dia, mes, ano

def visualizar_dados(dados):
    """Visualiza os dados conforme o período e tipo de dados informados pelo usuário."""
    print("**Intervalo de Dados**")

    # Solicitar entrada do usuário para o período desejado
    inicio_mes = input("Informe o mês inicial (MM): ")
    inicio_ano = input("Informe o ano inicial (AAAA): ")
    fim_mes = input("Informe o mês final (MM): ")
    fim_ano = input("Informe o ano final (AAAA): ")

    # Validar o período informado pelo usuário
    meses_validos = [str(i).zfill(2) for i in range(1, 13)]

    if inicio_mes not in meses_validos or fim_mes not in meses_validos:
        print("Mês inválido.")
        return
    if int(inicio_ano) < 1961 or int(fim_ano) > 2016 or int(inicio_ano) > int(fim_ano):
        print("Ano inválido.")
        return

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

# Carregar os dados do arquivo CSV
arquivo = 'Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv'
dados = carregar_dados(arquivo)

# Executar visualização de dados
visualizar_dados(dados)

# Encontrar o mês/ano com maior precipitação considerando todos os dados
mes_ano_maior_precipitacao, maior_precipitacao = maior_precipitacao_total(dados)
print(f"\nMês/Ano com maior precipitação: {mes_ano_maior_precipitacao}, Precipitação: {maior_precipitacao} mm")
