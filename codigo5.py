maior = 0

for i in range(3):
    num1 = int(input('Digite um número: '))
    if num1 > maior:
        maior = num1
print('o maior número é {}', maior)
