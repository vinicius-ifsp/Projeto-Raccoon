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
