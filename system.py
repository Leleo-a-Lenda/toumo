import json

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return f"arquivo não encontrado '{ARQUIVO}'"


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
    return f"tarefa '{titulo}' salva"

def concluir_tarefa(indice):
    tarefas = carregar_tarefas()

    tarefas[int(indice) - 1]["concluida"] = True
    
    salvar_tarefas(tarefas)

def remover_tarefa(indice):
    tarefas = carregar_tarefas()
    del tarefas[int(indice)]
    salvar_tarefas(tarefas)
