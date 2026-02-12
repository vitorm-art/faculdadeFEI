n1 = float(input("coloque sua primeira nota"))
n2 = int(input("coloque sua segunda nota"))
n3 = int(input("coloque sua terceira nota"))
soma = n1 + n2 + n3
media = soma / 3
if media >= 9: 
    print("aprovado com louvor")

elif media >5 and media >9:
    print("aprovado")

else: 
    print("reprovado")