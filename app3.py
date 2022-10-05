Lista = []

for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    Lista.append(num)

print(f"O maior é {max(Lista)}")
print(f"O menor é {min(Lista)}")
print(Lista)
