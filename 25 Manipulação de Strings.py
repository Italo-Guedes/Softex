# Estruture três códigos, os quais devem conter uma função de manipulação de
# string que obtenha resultado.


def contar(string):
    return len(string)

print(" ",contar(input("1- Escreva uma palavra para saber o número de caracteres: ")), "caracteres.")



def maiuscula(string):
    return string.upper()

print(" Palavra convertida:", maiuscula(input("2 - Digite uma palavra para ser convertida em Maiúscula: ")))



def reverso(string):
    reverte = ""
    for i in range(len(string), 0, -1):
        reverte += string[i-1]
    return reverte

print(" Entrada revertida:", reverso(input("3 - Digite uma palavra para ser convertida de trás pra frente: ")))
    