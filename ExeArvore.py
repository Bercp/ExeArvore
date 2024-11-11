def criar_arvore():
    return None


def criar_no(valor):
    return {"valor": valor, "esquerda": None, "direita": None}


def adicionar(raiz, valor):
    if raiz is None:
        return criar_no(valor)

    if valor < raiz["valor"]:
        raiz["esquerda"] = adicionar(raiz["esquerda"], valor)
    elif valor > raiz["valor"]:
        raiz["direita"] = adicionar(raiz["direita"], valor)

    return raiz


def remover(raiz, valor):
    if raiz is None:
        return raiz

    if valor < raiz["valor"]:
        raiz["esquerda"] = remover(raiz["esquerda"], valor)
    elif valor > raiz["valor"]:
        raiz["direita"] = remover(raiz["direita"], valor)
    else:
        if raiz["esquerda"] is None:
            return raiz["direita"]
        elif raiz["direita"] is None:
            return raiz["esquerda"]

        temp = menor_valor(raiz["direita"])
        raiz["valor"] = temp["valor"]
        raiz["direita"] = remover(raiz["direita"], temp["valor"])

    return raiz


def procurar(raiz, valor):
    if raiz is None or raiz["valor"] == valor:
        return raiz

    if valor < raiz["valor"]:
        return procurar(raiz["esquerda"], valor)
    else:
        return procurar(raiz["direita"], valor)


def menor_valor(raiz):
    atual = raiz
    while atual and atual["esquerda"] is not None:
        atual = atual["esquerda"]
    return atual


def exibir_pre_ordem(raiz):
    if raiz:
        print(raiz["valor"], end=" ")
        exibir_pre_ordem(raiz["esquerda"])
        exibir_pre_ordem(raiz["direita"])


def exibir_em_ordem_simetrica(raiz):
    if raiz:
        exibir_em_ordem_simetrica(raiz["esquerda"])
        print(raiz["valor"], end=" ")
        exibir_em_ordem_simetrica(raiz["direita"])


def exibir_pos_ordem(raiz):
    if raiz:
        exibir_pos_ordem(raiz["esquerda"])
        exibir_pos_ordem(raiz["direita"])
        print(raiz["valor"], end=" ")


def menu():
    raiz = criar_arvore()

    while True:
        print("\nMenu:")
        print("1. Adicionar valor")
        print("2. Remover valor")
        print("3. Buscar valor")
        print("4. Exibir pré-ordem")
        print("5. Exibir em ordem simétrica")
        print("6. Exibir pós-ordem")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = int(input("Digite o valor a ser adicionado: "))
            raiz = adicionar(raiz, valor)
            print("Valor ", valor, " adicionado")

        elif opcao == "2":
            valor = int(input("Digite o valor a ser removido: "))
            raiz = remover(raiz, valor)
            print("Valor ", valor, " remvido")

        elif opcao == "3":
            valor = int(input("Digite o valor a ser buscado: "))
            resultado = procurar(raiz, valor)
            if resultado:
                print("Valor ", valor, " Encontrado na Arvore")
            else:
                print("Valor ", valor, " Nao encontrado na Arvore")

        elif opcao == "4":
            print("Exibindo pre-ordem:")
            exibir_pre_ordem(raiz)
            print()

        elif opcao == "5":
            print("Exibindo em ordem simetrica:")
            exibir_em_ordem_simetrica(raiz)
            print()

        elif opcao == "6":
            print("Exibindo pós-ordem:")
            exibir_pos_ordem(raiz)
            print()

        elif opcao == "7":
            print("Saindo ...")
            break

        else:
            print("Opção inválida! Digite um numero do menu.")

menu()
