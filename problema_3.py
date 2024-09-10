import json

def calcular_faturamento():
    # Carregue o arquivo faturamento.json
    with open('../faturamento/faturamento.json') as f:
        faturamento = json.load(f)

    # Filtra apenas os dias com valor de faturamento maior que zero
    valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

    # Calcule o menor, maior valor de faturamento maior que zero
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)

    # Calcula quantos dias o faturamento foi acima da média
    dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

    # Imprime os resultados
    print(f"Menor valor de faturamento: R${menor_valor}")
    print(f"Maior valor de faturamento: R${maior_valor}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

if __name__ == "__main__":
    calcular_faturamento()
