desconto = 0

numeroPratos = int(input("Digite o número de pratos principais comprados: "))

while numeroPratos <= 0:
    numeroPratos = int(input("Valor inválido. Digite o número de pratos principais comprados: "))

if numeroPratos > 3:
    desconto += 4

valorNota = float(input("Digite o valor da nota: "))
while valorNota <= 0:
    valorNota = float(input("Valor inválido. Digite o valor total da nota:"))
if valorNota > 500:
    desconto += 6
    