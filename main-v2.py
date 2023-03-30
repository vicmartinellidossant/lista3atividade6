precoUnit = float(input("Qual é o preço de cada unidade do produto? "))
qtde = int(input("Quantas unidades foram vendidas? "))
desconto = float(input("Qual é o percentual de desconto para a venda? "))

totalSemDesconto = (precoUnit * qtde)
valorComDesconto = (totalSemDesconto - (totalSemDesconto * (desconto / 100))

print(f"O valor com desconto será R$ {valorComDesconto:.2f}")