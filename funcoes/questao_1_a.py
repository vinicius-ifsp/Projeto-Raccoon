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
