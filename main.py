import math

def bhaskara(a, b, c):

    if a == 0:
        return "O valor de 'a' não pode ser igual a 0. Escolha outro valor."
    
    delta = (b**2) - 4*a*c

    if delta < 0:
        return "Delta negativo. Não é possível finalizar a equação."
    elif delta == 0:
        x = -b / (2*a)
        return "Delta é 0. Raiz única: " + str(x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return "Delta: " + str(delta) + ". As raízes são: " + str(x1) + " e " + str(x2)

continuar = "s"

while continuar.lower() == "s":
    a = int(input("Insira o primeiro valor: "))
    b = int(input("Insira o segundo valor: "))
    c = int(input("Insira o terceiro valor: "))

    resultado = bhaskara(a, b, c)
    print(resultado)

    continuar = input("Deseja calcular outra equação? (s/n): ")

print("Programa encerrado.")