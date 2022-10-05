contador = 1
Lista = []
par = []
impar = []

while contador <= 10:
    num = int(input(f"Digite o {contador}º número maior que zero: "))
    if num > 0:
        Lista.append(num)
        contador = contador + 1
    elif num ==0:
        print("Digitou zero! Digite novamente: ")
    else:
        print("Digitou negativo! Digite novamente: ")

for item in Lista:
    if item%2 == 0:
        par.append(item)
    else:
        impar.append(item)

print(Lista)
print(f"Lista dos pares: {par}")
print(f"Lista dos pares: {impar}")
print(f"Soma dos pares: {sum(par)}")
print(f"Soma dos ímpares: {sum(impar)}")