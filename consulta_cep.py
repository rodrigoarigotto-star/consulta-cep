import requests
import json

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
    print("1 - Buscar um CEP")
    print("2 - Ver histórico de buscas")
    print("3 - Salvar histórico em arquivo")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cep = limpar_cep(input("Digite o CEP (só números): "))

        if not cep_valido(cep):
            print("CEP inválido! Digite 8 números, sem espaços ou traços.")
            continue

        dados = consultar_cep(cep)
        if dados.get("erro"):
            print("CEP não encontrado.")
            continue
        exibir_endereco(dados)

    elif opcao == "2":
        print("Até logo!")
        break
    # ... opções 1 e 2 continuam iguais
    elif opcao == "3":
        with open("historico.json", "w") as arquivo:
            json.dump(historico, arquivo, indent=2, ensure_ascii=False)
        print("Histórico salvo em historico.json!")
    elif opcao == "4":
        print("Até logo!")
        break


    else:
        print("Opção inválida.")