print("Bem vindo a lista de contatos do Vinicius")
print("-----------------------------------------")
print("--------------Menu princial--------------")

lista_contatos = []
id_global = 4959006

# C. Função para cadastrar contato
def cadastrar_contato(id):
    nome = input("Informe o nome do contato: ")
    atividade = input("Informe a atividade do contato: ")
    telefone = input("Informe o telefone do contato: ")

    # Cria um dicionário para o contato
    contato = {
        'id': id,
        'nome': nome,
        'atividade': atividade,
        'telefone': telefone
    }

    # Adiciona o contato à lista de contatos
    lista_contatos.append(contato.copy())

# D. Função para consultar contatos
def consultar_contatos():
    while True:
        opcao = input(
            "Escolha uma opção:\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Atividade\n4. Retornar ao menu\n")

        if opcao == '1':
            # Consultar todos os contatos
            for contato in lista_contatos:
                print(contato)
        elif opcao == '2':
            # Consultar por ID
            id_consulta = int(input("Informe o ID do contato: "))
            for contato in lista_contatos:
                if contato['id'] == id_consulta:
                    print(contato)
                    break
            else:
                print("Contato não encontrado.")
        elif opcao == '3':
            # Consultar por Atividade
            atividade_consulta = input("Informe a atividade: ")
            found = False
            for contato in lista_contatos:
                if contato['atividade'] == atividade_consulta:
                    print(contato)
                    found = True
            if not found:
                print("Nenhum contato encontrado com esta atividade.")
        elif opcao == '4':
            return
        else:
            print("Opção inválida.")

# E. Função para remover contato
def remover_contato():
    while True:
        id_remocao = int(input("Informe o ID do contato a ser removido: "))
        for contato in lista_contatos:
            if contato['id'] == id_remocao:
                lista_contatos.remove(contato)
                print(f"Contato com ID {id_remocao} removido.")
                return
        print("Id inválido.")

# F. Menu principal
while True:
    opcao_menu = input(
        "Escolha uma opção:\n1. Cadastrar Contato\n2. Consultar Contato\n3. Remover Contato\n4. Encerrar Programa\n")

    if opcao_menu == '1':
        id_global += 1
        cadastrar_contato(id_global)
    elif opcao_menu == '2':
        consultar_contatos()
    elif opcao_menu == '3':
        remover_contato()
    elif opcao_menu == '4':
        break
    else:
        print("Opção inválida.")
# Cadastro do próprio contato
cadastrar_contato(id_global)
# J. Cadastro de mais 2 contatos
id_global += 1
cadastrar_contato(id_global)  # Primeiro contato adicional
id_global += 1
cadastrar_contato(id_global)  # Segundo contato adicional

#Consulta de todos os contatos
consultar_contatos()

#Consulta por ID (exemplo: ID 1)
for contato in lista_contatos:
    if contato['id'] == 1:
        print(contato)
        break

#Consulta por atividade (exemplo: estudante)
for contato in lista_contatos:
    if contato['atividade'] == "estudante":
        print(contato)  # Exibe contatos que são estudantes

#Remoção de um contato (exemplo: ID 1) e consulta de todos
remover_contato()  # Remove contato pelo ID
consultar_contatos()  # Consulta todos os contatos para verificar a remoção



