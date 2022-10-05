Lista = []

for i in range(1,6):
    num = int(input(f"Digite o {i}º número: "))
    Lista.append(num)


print(f"A soma é {sum(Lista)}")
print(f"A média é {sum(Lista)/len(Lista)}")
print(Lista)