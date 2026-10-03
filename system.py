import json

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)


def adicionar_tarefa(titulo, descricao):
    tarefas = carregar_tarefas()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)


def listar_tarefas():
    tarefas = carregar_tarefas()

    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["concluida"] else " "
        print(f"[{status}] {indice} - {tarefa['titulo']} \n {tarefa[descricao]}")


def concluir_tarefa(indice):
    tarefas = carregar_tarefas()

    tarefas[indice - 1]["concluida"] = True

    salvar_tarefas(tarefas)
