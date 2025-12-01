import math

a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))
c = int(input("Insira o terceiro valor: "))

def bhaskara(a, b, c):

    if a == 0:
        return "O valor de 'a' não pode ser igual a 0. Escolha outro valor."
    
    delta = (b**2) -4*a*c

    if delta < 0:
        return "Delta negativo. Não é possível finalizar a equação."
    elif delta == 0:
        x = -b / (2*a)
        return "Delta é 0. Raiz única: ", x
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return 'Delta: ', delta, '. As raízes são: ', x1, 'e ', x2
    
resultado = bhaskara(a, b, c)
print(resultado)