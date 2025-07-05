print("---------------Bem-vindos à Pizzaria de Vinicius De Oliveira Mendes-------")
print('--------------------------Cardápio----------------------------------------')
print('--|Tamanho|  Pizza Salgada(PS)  | Pizza Doce(PD)|-------------------------')
print('--|   P   |       R$30.00       |    R$34.00    |-------------------------')
print('--|   M   |       R$45.00       |    R$48.00    |-------------------------')
print('--|   G   |       R$60.00       |    R$66.00    |-------------------------')
print('--------------------------------------------------------------------------')
print('Escolha do sabor: Pizza Salgada (PS) OU Pizza Doce (PD)')
print('Escolha um tamanho: Tamanhos disponíveis P(Pequeno), M(Média) ou G(Grande)')

valor_total_de_pedidos = 0

# Função para determinar o valor da pizza
def calcular_valor(sabor, tamanho):
    if sabor == "PS":
        if tamanho == 'P':
            return 30
        elif tamanho == 'M':
            return 45
        else:
            return 60
    elif sabor == "PD":
        if tamanho == 'P':
            return 34
        elif tamanho == 'M':
            return 48
        else:
            return 66

# Primeira pizza
while True:
    sabor = input('Escolha um Sabor (PS ou PD): ').upper() #aceita letras minusculas
    if sabor in ('PS', 'PD'):
        break
    else:
        print("Sabor inválido, tente novamente.")

while True:
    tamanho = input('Escolha um Tamanho (P, M ou G): ').upper() #aceita letras minusculas
    if tamanho in ('P', 'M', 'G'):
        break
    else:
        print("Tamanho inválido, tente novamente.")

# Cálculo do valor da primeira pizza
valor = calcular_valor(sabor, tamanho)
valor_total_de_pedidos += valor
print(f"Você pediu uma pizza {sabor} de tamanho {tamanho}, no valor: R${valor:.2f}")

# Loop para novos pedidos
while True:
    continuar = input("Deseja pedir mais alguma coisa? (SIM/NÃO): ").upper() #aceita letras minusculas
    if continuar != 'SIM':
        break

    # Repetindo o processo para um novo pedido
    while True:
        sabor = input('Escolha um Sabor (PS ou PD): ').upper() #aceita letras minusculas
        if sabor in ('PS', 'PD'):
            break
        else:
            print("Sabor inválido, tente novamente.")

    while True:
        tamanho = input('Escolha um Tamanho (P, M ou G): ').upper() #aceitas letras minusculas
        if tamanho in ('P', 'M', 'G'):
            break
        else:
            print("Tamanho inválido, tente novamente.")

    # Cálculo do valor da nova pizza
    valor = calcular_valor(sabor, tamanho)
    valor_total_de_pedidos += valor
    print(f"Você pediu uma pizza {sabor} de tamanho {tamanho}, no valor: R${valor:.2f}")

print(f'Fim do atendimento. O valor total do pedido é: R${valor_total_de_pedidos:.2f}')











