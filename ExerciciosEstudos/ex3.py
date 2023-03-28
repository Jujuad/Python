valor = float(input('Insira o preço do produto: '))
quantidade = int(input('Insira a quantidade do produto: '))

if quantidade <= 500 and valor <= 30:
    valor = valor + valor * 0.10
    print('1. O produto ficou no valor de:', valor)
elif quantidade >= 501 and quantidade < 1200 and valor >= 31 and valor < 80:
    valor = valor + valor * 0.15
    print('2. O produto ficou no valor de:', valor)
elif quantidade > 1200 and valor > 80:
    valor = valor - valor * 0.20
    print('3. O produto ficou no valor de:', valor)
else:
    print('O preco nao sera alterado! Valor:', valor)


if valor < 0:
    valor = 0
    print('Erro! Valor Negativo.')
