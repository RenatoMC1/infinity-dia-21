contador = 1
soma = 0
Lista = []

while True:
    nota = int(input(f"Digite a {contador}ª nota: "))
    Lista.append(nota)
    soma = soma + nota
    resposta = int(input("Deseja continuar?\n[1] Sim\n[2] Nao\n"))
    if resposta == 2:
        break
    else:
        contador = contador + 1

media = soma/contador

print(f"A lista de notas é: {Lista}")
print(f"A soma das notas é: {soma}")
print(f"A média das notas é: {media}")
