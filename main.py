from .system import (
    concluir_tarefa,
    listar_tarefas,
    adicionar_tarefa
)
from rich.text import Text

titulo = Text()
titulo.append("╔══════════════════════╗\n", style="bold cyan")
titulo.append("   TOUMO TAREFAS\n", style="bold magenta")
titulo.append("╚══════════════════════╝", style="bold cyan")

print(titulo)
