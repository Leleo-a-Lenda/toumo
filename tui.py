from system import listar_tarefas
from rich.panel import Panel
panel = Panel(__name__)

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
    a = panel(listar_tarefas())
    print(a)
    
