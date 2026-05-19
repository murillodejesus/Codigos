# faturamento = 1000
# custo = 250
# lucro = faturamento - custo

#print('O faturamento da Loja foi ' + str(faturamento) + ' .O Custo da Loja foi ' + str(custo) + 'O Lucro da Loja foi ' + str(lucro))

# com format
#print('O faturamento da loja foi {}. O Custo da Loja foi {}. O Lucro da Loja foi {}' .format(faturamento, custo, lucro))

# com f-string 
# print(f"O Faturamento foi de {faturamento} e o Lucro foi {lucro}")

faturamento = input("Insira o Faturamento: ")
custo = input("Insira o custo: ") 

print(type(faturamento))
print(type(custo))

lucro = faturamento - custo

print(lucro)