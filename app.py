soma = 0
media = 0
Lista = []

for i in range(1,6):
    num = int(input(f"Digite o {i}º número: "))
    soma = soma + num
    media = soma / i
    Lista.append(num)


print(f"A soma é {soma}")
print(f"A média é {media}")
print(Lista)