def menu():
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Sair")

livros = []

def adicionar_livro(titulo, autor):
    livro = {"titulo": titulo, "autor": autor}
    livros.append(livro)
    print("Livro adicionado com sucesso!")

def listar_livros():
    if not livros:
        print("Não há livros cadastrados.")
    else:
        for livro in livros:
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}")


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Implementação da função adicionar_livro virá em um branch separado
        print("Funcionalidade em desenvolvimento...")
    elif opcao == "2":
        # Implementação da função listar_livros virá em um branch separado
        print("Funcionalidade em desenvolvimento...")
    elif opcao == "3":
        break
    else:
        print("Opção inválida.")

# Funções adicionar_livro e listar_livros serão implementadas em branches separados
