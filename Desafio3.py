import json

soma = 0
diasComFaturamento = 0
diasComFaturamentoSuperiorAMedia = 0

with open("dados/dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

maior = menor = dados['valor' == 0]

for dado in dados:
    if(dado['valor'] != 0):
        soma += dado['valor']
        diasComFaturamento += 1
        if(dado['valor'] < menor['valor']):
            menor = dado
        if(dado['valor'] > maior['valor']):
            maior = dado

mediaMensal = soma / diasComFaturamento
for dado in dados:
    if(dado['valor'] > mediaMensal):
        diasComFaturamentoSuperiorAMedia += 1

print(f"O menor valor de faturamento foi de {menor['valor']} e ocorreu no dia {menor['dia']}")
print(f"O maior valor de faturamento foi de {maior['valor']} e ocorreu no dia {maior['dia']}")
print(f"Houveram {diasComFaturamentoSuperiorAMedia} dias com faturamento superior à média mensal, que foi de {mediaMensal:.4f}")