
operação = input('''
Por favor escolha uma opção:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')



numero_1 = int(input('Escreva o primeiro numero: '))
numero_2 = int(input('Escolha o segundo numero: '))

if operação == '+':
    print(numero_1 + numero_2)
    


elif operação == '-':
    print(numero_1 - numero_2)

elif operação == '*':
    print(numero_1 * numero_2)


elif operação == '/':
    print(numero_1 / numero_2)



