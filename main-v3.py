precoUnit = float(input("Qual é o preço de cada unidade do produto? "))
qtde = int(input("Quantas unidades foram vendidas? "))
desconto = float(input("Qual é o percentual de desconto para a venda? "))

valorComDesconto = (precoUnit * qtde) * (1 - desconto / 100)

print(f"O valor com desconto será R$ {valorComDesconto:.2f}")
print("Deu certo: ")