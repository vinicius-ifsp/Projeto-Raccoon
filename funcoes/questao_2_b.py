import json
import re


# Questao 1 - A
def fixName(data):
    # dicionario com '\'+ caracter corrompido como chave e a letra correspondente correta como valor
    dic_regex = {"\\æ": "a", "\\¢": "c", "\\ø": "o", "\\ß": "b"}
    # monta expressao regular com as chaves do dicionario
    pattern = re.compile("|".join(dic_regex.keys()))
    # loop para percorrer os dados
    for i in range(len(data)):
        # Aplica a expressão em cima do nome da iteracao atual do loop
        data[i]["name"] = pattern.sub(
            lambda letra: dic_regex[re.escape(letra.group(0))], data[i]["name"])


# Questao 1 - B
def fixPrice(data):
    # loop para percorrer os dados
    for i in range(len(data)):
        # verifica se o numero nao esta como float
        if not isinstance(data[i]["price"], float):
            # caso nao esteja realiza a conversao
            data[i]["price"] = float(data[i]["price"])


# Questao 1 - C
# Questao 2 - B
def calculatorTotalStockValueByCategory(data):
    dic_sotck = {}
    for product in data:
        current_category = product["category"]
        if not current_category in dic_sotck:
            dic_sotck[current_category] = 0
        dic_sotck[current_category] += (product["price"] * product["quantity"])
    print("\n\nCategory | Total Value\n\n")
    for k, v in dic_sotck.items():
        print(f"{k}  {v}")
