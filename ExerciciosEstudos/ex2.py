mediaPrimeiro = float(input('Informe a media do primeiro semestre: '))
mediaSegundo = float(input('Informe a media do segundo semestre: '))

media = (mediaSegundo * 0.4 + mediaPrimeiro * 0.6)/2

print(media)

if media >= 6:
    print('Aluno aprovado')
elif media >= 4:
    print('Aluno realizara exame')
else:
    print('Aluno reprovado')
