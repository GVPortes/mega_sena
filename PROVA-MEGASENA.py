#NOME: Gabriel Vieira Portes

import random

valores_apostas = [
    5.00, 35.00, 140.00, 420.00, 1050.00,
    2310.00, 4620.00, 8580.00, 15015.00,
    25025.00, 40040.00, 61880.00, 92820.00,
    135660.00, 193800.00
]

quantidade_apostas = 0
while quantidade_apostas < 6 or quantidade_apostas > 20:
    quantidade_apostas = int(input("Digite a quantidade de apostas (entre 6 e 20): "))
    if quantidade_apostas < 6 or quantidade_apostas > 20:
        print("Quantidade de apostas inválida. Tente novamente.")

valor_total = valores_apostas[quantidade_apostas - 6]
print(f"Valor total a ser pago: R$ {valor_total:.2f}")

apostas_usuario = []
while len(apostas_usuario) < quantidade_apostas:
    aposta = []
    while len(aposta) < 6:
        numero = int(input(f"Digite o {len(aposta)+1}º número da aposta (entre 1 e 60): "))
        if numero < 1 or numero > 60:
            print("Número inválido. Digite um número entre 1 e 60.")
            continue
        if numero in aposta:
            print("Número já escolhido. Escolha outro número.")
            continue
        aposta.append(numero)
    apostas_usuario.append(sorted(aposta))

numeros_sorteados = [random.randint(1, 60) for i in range(6)]
numeros_sorteados.sort()
print(f"Sorteio: {numeros_sorteados}")

def verificar_acertos(aposta, numeros_sorteados):
    acertos = 0
    for numero in aposta:
        if numero in numeros_sorteados:
            acertos += 1
    return acertos

for aposta in apostas_usuario:
    acertos = verificar_acertos(aposta, numeros_sorteados)
    if acertos == 4:
        print(f"A aposta {aposta} acertou a Quadra.")
    else:
        if acertos == 5:
            print(f"A aposta {aposta} acertou a Quina.")
        else:
            if acertos == 6:
                print(f"A aposta {aposta} acertou a Sena.")
            else:
                print(f"A aposta {aposta} não acertou nenhum prêmio.")
                
print (numeros_sorteados)