Lista = []

for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    Lista.append(num)

Lista.sort()
print(f"A ordem crescente é {Lista}")
Lista.reverse()
print(f"A ordem decrescente é {Lista}")



