def menu():
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Remover livro")
    print("4. Sair")

livros = []

def adicionar_livro():
    livro = input("Digite o título do livro")
    livros.append(livro)
    print("Livro adicionado com sucesso!")

def listar_livros():
    if len(livros) == 0:
        print("Não há livros cadastrados.")
    else:
        for i in livros:
            print(i)

def remover_livro():
    livro = input("Digite o título do livro")
    if livro in livros:
        livros.remove(livro)
        print("Livro removido com sucesso!")
    else:
        print("Livro não adicionado previamente")


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        print("Funcionalidade em desenvolvimento")
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")
