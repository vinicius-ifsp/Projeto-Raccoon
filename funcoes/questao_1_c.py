# Questao 1 - C
def fixQuantity(data):
    # loop para percorrer os dados
    for i in range(len(data)):
        # verifica se nao existe a propriedade quantity
        if not "quantity" in data[i]:
            # caso nao exista realiza a cricao e atribuicao com 0
            data[i]["quantity"] = 0
