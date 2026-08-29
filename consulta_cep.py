import requests


historico = []


def limpar_cep(cep):
    return cep.replace("-", "").replace(".", "").strip()


def cep_valido(cep):
    return cep.isdigit() and len(cep) == 8


def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados


def exibir_endereco(dados):
    print("CEP:", dados["cep"])
    print("Rua:", dados["logradouro"])
    print("Bairro:", dados["bairro"])
    print("Cidade:", dados["localidade"])
    print("Estado:", dados["uf"])


while True:
    print("\n=== Consulta de CEP ===")
    print("1 - Buscar um CEP")
    print("2 - Ver histórico de buscas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cep = limpar_cep(input("Digite o CEP: "))

        if not cep_valido(cep):
            print("CEP inválido! Digite 8 números.")
            continue

        dados = consultar_cep(cep)

        if dados.get("erro"):
            print("CEP não encontrado.")
            continue

        exibir_endereco(dados)
        historico.append(dados)

    elif opcao == "2":
        if not historico:
            print("Nenhuma busca feita ainda.")

        for item in historico:
            print(item["cep"], "-", item["logradouro"])

    elif opcao == "3":
        print("Até logo!")
        break

    else:
        print("Opção inválida.")