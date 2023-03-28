salario = float(input("Insira o salario:"))


print("1. Analista Jr")
print("2. Analista Pleno")
print("3. Analista Senior")
print("4. Arquiteto")
print("5. Gerente")
cargo = int(input("Entre com a opcao do cargo: "))

ajuste = float(input("Insira o percentual de ajuste: "))
porcento = ajuste/100

if cargo == 1:
    salario_final = salario*(1 + porcento) + salario*0.02
elif cargo == 2:
    salario_final = salario*(1 + porcento) + salario*0.025
elif cargo == 3:
    salario_final = salario*(1 + porcento) + salario*0.03
elif cargo == 4:
    salario_final = salario*(1 + porcento) + salario*0.035
elif cargo == 5:
    salario_final = salario*(1 + porcento) + salario*0.045

print("Salario Final:", salario_final)
