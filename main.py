# operações matemáticas
resp = 1
while resp == 1:
    op = int(input('\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nEscolha uma operação matemática: '))
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    if op == 1:
        print(f'A soma de {n1} + {n2} é igual a {n1 + n2}')
    elif op == 2:
        print(f'A subtração de {n1} - {n2} é igual a {n1 - n2}')
    elif op == 3:
        print(f'A multiplicação de {n1} x {n2} é igual a {n1 * n2}')
    elif op == 4:
        print(f'A divisão de {n1} / {n2} é igual a {n1 // n2}')
    resp = int(input('Deseja continuar? 1 - Sim / 2 - Não\n'))
else:
    print('Obrigado!')
