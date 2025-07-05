print("Bem-vindos à Madeireira do Lenhador Vinicius ")

def escolha_tipo():
    # Função para escolher o tipo de madeira
    while True:
        madeira = input("Escolha um tipo de madeira entre PIN/PER/MOG/IPE/IMB: ").upper()
        if madeira == 'PIN':
            return 150.40
        elif madeira == 'PER':
            return 170.20
        elif madeira == 'MOG':
            return 190.90
        elif madeira == 'IPE':
            return 210.10
        elif madeira == 'IMB':
            return 220.70
        else:
            print("Opção inválida. Tente novamente.")

def qtd_toras():
    # Função para escolher a quantidade de toras
    while True:
        try:
            toras = int(input("Escolha a quantidade de toras: "))
            if toras < 100:
                desconto = 0
            elif 100 <= toras < 500:
                desconto = 4
            elif 500 <= toras < 1000:
                desconto = 9
            elif 1000 <= toras < 5000:
                desconto = 16
            else:
                print("Quantidade acima de 2000 não é aceita. Tente novamente.")  # Exigência J
                continue
            return toras, desconto  # Retorna a quantidade de toras e o desconto
        except ValueError:
            print("Por favor, insira um número válido.")  # Exigência F

def transporte():
    # Função para escolher o serviço de transporte
    while True:
        servico = input("Escolha o serviço de transporte (1 - Municipal, 2 - Estadual, 3 - Nacional): ")
        if servico == '1':
            return 50.00
        elif servico == '2':
            return 100.00
        elif servico == '3':
            return 200.00
        else:
            print("Opção de transporte inválida. Tente novamente.")

preco_madeira = escolha_tipo()
toras, desconto = qtd_toras()
preco_transporte = transporte()

total_madeira = preco_madeira * toras
total_desconto = (total_madeira * desconto) / 100
total_a_pagar = total_madeira - total_desconto + preco_transporte

print(f"\nResumo da compra:")
print(f"Tipo de madeira escolhida: R${preco_madeira:.2f} por unidade")
print(f"Quantidade de toras: {toras}")
print(f"Desconto aplicado: {desconto}%")
print(f"Valor do transporte: R${preco_transporte:.2f}")
print(f"Total a pagar: R${total_a_pagar:.2f}")

