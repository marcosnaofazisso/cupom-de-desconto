desconto = 0

print("----------------------------")
print("FINALIZAÇÃO DA CONTA")
print("----------------------------")

numeroPratos = int(input("Digite o número de pratos principais comprados: "))
while numeroPratos <= 0:
    numeroPratos = int(input("Valor inválido. Por favor, digite o número de pratos principais comprados: "))
if numeroPratos > 3:
    desconto += 4

valorNota = float(input("Digite o valor total da nota: "))
while valorNota <= 0:
    valorNota = float(input("Valor inválido. Por favor, digite o valor total da nota:"))
if valorNota > 500:
    desconto += 6

cupom = input("Você possui algum cupom de desconto? (S/N)").upper()
while cupom != "S" and cupom != "N":
    cupom = input("Por favor, insira uma resposta válida: (S/N)").upper()
while cupom == "S":
    cupom = input("Show de bola! Digite o nome do cupom de desconto: ").upper()

    if cupom == "DESCONTASSODEZ":
        desconto += 10
        cupom = "X"
        print("Cupom de 10% de desconto adicionado com sucesso! ") 
        
    elif cupom =="DESCONTAO5":
        desconto += 5
        cupom = "X"
        print("Cupom de 5% de desconto adicionado com sucesso! ")
    else:
        print("Cupom inválido.")
        cupom = input("Você possui algum cupom de desconto? (S/N)").upper()
        while cupom != "S" and cupom != "N":
            cupom = input("Por favor, insira uma resposta válida: (S/N)").upper()

visitante = input("É a primeira vez que visita o restaurante? (S/N)").upper()
while visitante != "S" and visitante != "N":
    visitante = input("Por favor, insira uma resposta válida: (S/N)")
if visitante == "S":
    desconto += 5


total_sem_desconto = valorNota
total_com_desconto = valorNota - (desconto * valorNota/100)

qtd_pessoas = int(input("Digite a quantidade de pessoas que realizaram a compra: "))
while qtd_pessoas <= 0:
    qtd_pessoas=int(input("Dados incorretos. Por favor, digite a quantidade de pessoas que realizaram a compra:"))

rachar = total_com_desconto/qtd_pessoas

print("-------------------------------------")
print("Valor total da nota:", total_sem_desconto)
print("Valor total da nota com desconto:", total_com_desconto)
print("")
print("Número de pessoas:", qtd_pessoas)
print("Valor por pessoa:", rachar)
print("-------------------------------------")