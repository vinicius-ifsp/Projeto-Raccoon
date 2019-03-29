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
def fixQuantity(data):
    # loop para percorrer os dados
    for i in range(len(data)):
        # verifica se nao existe a propriedade quantity
        if not "quantity" in data[i]:
            # caso nao exista realiza a cricao e atribuicao com 0
            data[i]["quantity"] = 0


# Questao 1
def fixDataFromDB():
    database = 'broken-database.json'
    data = json.load(open(database))

    fixName(data)  # questao 1 - A
    fixPrice(data)  # questao 1 - B
    fixQuantity(data)  # questao 1 - C

    with open("broken-database-corrigido.json", "w", encoding='UTF-8') as output:
        json.dump(data, output, ensure_ascii=False)


# Questao 2 - A (Salvar a saida)
def saveOutputOfOrder(data_ordered_id, data_ordered_category):
    arq = open("output-ordered-by-name-and-category.txt",
               "w", encoding='UTF-8')
    arq.write("Ordered By Id:\n\n")
    for product in data_ordered_id:
        arq.write(product['name']+"\n")
    arq.write("\n\nOrdered By Category:\n\n")
    for product in data_ordered_category:
        arq.write(product['name']+"\n")
    arq.close()


# Questao 2 - A
def printAllProductNamesOrderedByCategoryAndId(data):
    def compare(a, b, p): return a[p] > b[p]

    # metodo de ordenacao Insertion Sort
    def sort(arr, prop):
        for p in range(0, len(arr)):
            current_element = arr[p]

            while p > 0 and compare(arr[p - 1], current_element, prop):
                arr[p] = arr[p - 1]
                p -= 1

            arr[p] = current_element

    data_ordered_id = data[:]  # copia para salvar no arquivo de saida
    data_ordered_category = data[:]  # copia para salvar no arquivo de saida

    sort(data_ordered_id, "id")
    print("Ordered By Id:\n\n")
    for product in data_ordered_id:
        print(product['name']+"\n")

    sort(data_ordered_category, "category")
    print("\n\nOrdered By Category:\n\n")
    for product in data_ordered_category:
        print(product['name']+"\n")

    saveOutputOfOrder(data_ordered_id, data_ordered_category)


# Questao 2 - A (Salvar a saida)
def saveOutputTotalStockValueByCategory(dic_sotck):
    arq = open("output-total-stock-value-by-category.txt",
               "w", encoding='UTF-8')
    arq.write("Category | Total Value\n\n")
    for k, v in dic_sotck.items():
        arq.write(f"{k}  {v}\n")
    arq.close()


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
    saveOutputTotalStockValueByCategory(dic_sotck)


# Questao 2
def validateCorrectedDB():
    database = 'broken-database-corrigido.json'
    data = json.load(open(database))

    printAllProductNamesOrderedByCategoryAndId(data)  # questao 2 - A
    calculatorTotalStockValueByCategory(data)  # questao 2 - B


if __name__ == "__main__":
    fixDataFromDB()  # questao 1
    validateCorrectedDB()  # questao 2
