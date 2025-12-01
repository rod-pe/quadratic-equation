import math

def bhaskara(a, b, c):
    delta = (b**2) - 4*a*c

    if delta < 0:
        return ("Delta negativo. Não é possível finalizar a equação.")
    elif delta == 0:
        x = -b / (2*a)
        return ("Delta é 0.", "Raiz única:", round(x, 2))
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return ("Delta: " + str(round(delta, 2)), ". As raízes são:", "x1 =", round(x1, 2), "x2 =", round(x2, 2))

def ler_inteiro(mensagem, not_zero=False):
    while True:
        try:
            valor = int(input(mensagem))
            if not_zero and valor == 0:
                print("Erro: o valor não pode ser 0. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Erro: Não é permitido inserir letras ou números decimais. Tente novamente.")

def ler_continuar(mensagem):
    while True:
        resposta = input(mensagem).lower()
        if resposta == "s" or resposta == "n":
            return resposta
        else:
            print("Erro: digite apenas 's' para sim ou 'n' para não.")

continuar = "s"

while continuar == "s":
    a = ler_inteiro("Insira o primeiro valor (não pode ser 0): ", not_zero=True)
    b = ler_inteiro("Insira o segundo valor: ")
    c = ler_inteiro("Insira o terceiro valor: ")

    resultado = bhaskara(a, b, c)
    print(*resultado)

    continuar = ler_continuar("Deseja calcular outra equação? (s/n): ")

print("Programa encerrado.")
