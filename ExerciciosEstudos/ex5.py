a = float(input("Insira o tamanho do lado a do triangulo: "))
b = float(input("Insira o tamanho do lado b do triangulo: "))
c = float(input("Insira o tamanho do lado c do triangulo: "))

if (a > b + c) or (b > a + c) or (c > a + b):
    print("Os valores nao formam um triangulo!")
elif a == b and a == c and b == c:
    print("Triangulo Equilatero!")
elif a == b or a == c or b == c:
    print("Triangulo Isosceles!")
elif a != b or a != c or b != c:
    print("Triangulo Escaleno!")
