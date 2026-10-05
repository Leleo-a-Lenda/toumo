from system import carregar_tarefas
from rich.panel import Panel
from rich import print

def logo_intro():
    return """
[bold magenta]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        [white]✦ T O U M O ✦[/white]
   [cyan]tarefas, foco e progresso[/cyan]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[/bold magenta]
"""

def help_dialog():
    return '''[dim]em caso de ajuda, digite: "help"[/]'''

def listq():
    tarefas = carregar_tarefas()
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "[green]✓[/]" if tarefa["concluida"] else " "
        print(Panel.fit(
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" 
            f"[{status}] [cyan]{indice}[/cyan] - [bold]{tarefa['titulo']}[/bold] \n    {tarefa['descricao']}"
            "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            title='tarefas',
            border_style='magenta'))
    
listq()