def adicionar_produto(estoque, nome_produto, quantidade, preco):
    produto = {
        "nome": nome_produto,
        "quantidade": int(quantidade),
        "preco": float(preco)
    }
    estoque.append(produto)
    print(f"\nProduto '{nome_produto}' adicionado ao estoque com sucesso!")

def mostrar_estoque(estoque):
    if not estoque:
        print("\nEstoque vazio. Nenhum produto cadastrado.")
        return

    print("\n" + "=" * 55)
    print(f"{'ESTOQUE - REDE VAREJISTA':^55}")
    print("=" * 55)
    print(f"{'Nº':<4} {'Produto':<25} {'Qtd':>6} {'Preço':>10}")
    print("-" * 55)

    for indice, produto in enumerate(estoque, start=1):
        nome = produto["nome"]
        qtd = produto["quantidade"]
        preco = produto["preco"]
        alerta = " ⚠" if qtd <= 5 else ""
        print(f"{indice:<4} {nome:<25} {qtd:>6} {preco:>10.2f}{alerta}")

    print("=" * 55)
    print("  ⚠ = estoque baixo (5 unidades ou menos)")

def atualizar_quantidade(estoque, indice_produto, nova_quantidade):
    indice_ajustado = int(indice_produto) - 1

    if 0 <= indice_ajustado < len(estoque):
        nome = estoque[indice_ajustado]["nome"]
        estoque[indice_ajustado]["quantidade"] = int(nova_quantidade)
        print(f"\nQuantidade do produto '{nome}' atualizada para {nova_quantidade} unidades.")
    else:
        print("\nÍndice inválido. Nenhum produto foi alterado.")

def completar_produto(estoque, indice_produto):
    indice_ajustado = int(indice_produto) - 1

    if 0 <= indice_ajustado < len(estoque):
        nome = estoque[indice_ajustado]["nome"]
        estoque[indice_ajustado]["quantidade"] = 0
        print(f"\nEstoque do produto '{nome}' zerado com sucesso.")
    else:
        print("\nÍndice inválido. Nenhum produto foi alterado.")

def deletar_produtos_sem_estoque(estoque):
    qtd_antes = len(estoque)
    estoque[:] = [p for p in estoque if p["quantidade"] > 0]
    qtd_removidos = qtd_antes - len(estoque)

    if qtd_removidos > 0:
        print(f"\n{qtd_removidos} produto(s) com estoque zerado foram removidos.")
    else:
        print("\nNenhum produto com estoque zerado encontrado.")

# ── Programa principal ──────────────────────────────────────────

estoque = []

while True:
    print("\n" + "=" * 40)
    print(f"{'GERENCIADOR DE ESTOQUE':^40}")
    print("=" * 40)
    print("  1. Adicionar produto")
    print("  2. Mostrar estoque")
    print("  3. Atualizar quantidade")
    print("  4. Zerar estoque de um produto")
    print("  5. Remover produtos sem estoque")
    print("  6. Sair")
    print("-" * 40)

    escolha = input("  Digite sua opção: ").strip()

    if escolha == "1":
        nome = input("\nNome do produto: ").strip()
        quantidade = input("Quantidade inicial: ").strip()
        preco = input("Preço unitário (R$): ").strip()
        adicionar_produto(estoque, nome, quantidade, preco)

    elif escolha == "2":
        mostrar_estoque(estoque)

    elif escolha == "3":
        mostrar_estoque(estoque)
        if estoque:
            indice = input("\nNúmero do produto a atualizar: ").strip()
            nova_qtd = input("Nova quantidade: ").strip()
            atualizar_quantidade(estoque, indice, nova_qtd)

    elif escolha == "4":
        mostrar_estoque(estoque)
        if estoque:
            indice = input("\nNúmero do produto a zerar: ").strip()
            completar_produto(estoque, indice)

    elif escolha == "5":
        deletar_produtos_sem_estoque(estoque)
        mostrar_estoque(estoque)

    elif escolha == "6":
        print("\nEncerrando o sistema. Até logo!")
        break

    else:
        print("\nOpção inválida. Digite um número de 1 a 6.")

print("\nSistema finalizado.")