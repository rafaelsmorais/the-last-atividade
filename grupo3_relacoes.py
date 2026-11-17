"""Grupo 3 — Código-base: relações diretas, ainda sem inferência."""

# Cada tupla representa (responsavel, dependente).
relacoes = [
    ("Ana", "Bruno"),
    ("Ana", "Carla"),
    ("Bruno", "Daniel"),
    ("Bruno", "Elisa"),
    ("Carla", "Felipe"),
    ("Daniel", "Gabriela"),
    ("Helena", "Igor"),
]


def listar_pessoas():
    pessoas = set()
    for origem, destino in relacoes:
        pessoas.add(origem)
        pessoas.add(destino)
    return sorted(pessoas)


def dependentes_diretos(pessoa):
    encontrados = []
    for origem, destino in relacoes:
        if origem == pessoa:
            encontrados.append(destino)
    return encontrados


def responsaveis_diretos(pessoa):
    encontrados = []
    for origem, destino in relacoes:
        if destino == pessoa:
            encontrados.append(origem)
    return encontrados

def possui_relacao_direta(origem, destino):
    for responsavel, dependente in relacoes:
        if responsavel == origem and dependente == destino:
            return True
    return False

def dependentes_indiretos(pessoa):
    diretos = dependentes_diretos(pessoa)
    encontrados = []
    encontrados.extend(diretos)
    for dependente in diretos:
        encontrados.extend(dependentes_indiretos(dependente))
    return encontrados

def responsaveis_indiretos(pessoa):
    diretos = responsaveis_diretos(pessoa)
    encontrados = []
    encontrados.extend(diretos)
    for responsavel in diretos:
        encontrados.extend(responsaveis_indiretos(responsavel))
    return encontrados

def possui_relacao_indireta(origem, destino):
    indiretos = dependentes_indiretos(origem)
    if destino in indiretos:
        return True
    else:
        return False

print("=== CONSULTA DE RELAÇÕES ===")
print("Pessoas:", ", ".join(listar_pessoas()))
while True:
    print("\n1 - Dependentes diretos")
    print("2 - Responsáveis diretos")
    print("3 - Verificar relação direta")
    print("4 - Dependentes indiretos")
    print("5 - Responsáveis indiretos")
    print("6 - Verificar relação indireta")
    print("0 - Sair")
    opcao = input("Opção: ").strip()
    if opcao == "0":
        break
    if opcao in ("1", "2", "3", "4", "5", "6"):
        pessoa = input("Primeira pessoa: ").strip()
        if opcao == "1":
            print(dependentes_diretos(pessoa))
        elif opcao == "2":
            print(responsaveis_diretos(pessoa))
        elif opcao == "4":
            print(dependentes_indiretos(pessoa))
        elif opcao == "5":
            print(responsaveis_indiretos(pessoa))
        elif opcao == "3":
            outra = input("Segunda pessoa: ").strip()
            print(possui_relacao_direta(pessoa, outra))
        elif opcao == "6":
            outra = input("Segunda pessoa: ").strip()
            print(possui_relacao_indireta(pessoa, outra))
    else:
        print("Opção inválida.")
