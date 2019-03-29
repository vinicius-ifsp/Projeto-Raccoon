# Questao 1 - B
def fixPrice(data):
    # loop para percorrer os dados
    for i in range(len(data)):
        # verifica se o numero nao esta como float
        if not isinstance(data[i]["price"], float):
            # caso nao esteja realiza a conversao
            data[i]["price"] = float(data[i]["price"])
