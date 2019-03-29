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
