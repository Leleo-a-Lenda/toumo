from system import (
    concluir_tarefa,
    adicionar_tarefa
)
from tui import (
    logo_intro,
    help_dialog,
    listq
)
from rich import print
from rich.panel import Panel
from rich.console import Console
console = Console()

print(logo_intro())
print(help_dialog())

while True:    
    command = input('')
    match command.split():
        case ['toumo', 'list'] | ['toumo', 'l']:
            listq()
        case ['toumo', 'add']:
            titulo = console.input('[magenta] ~ [/]')
            descricao = input('    ')
            adicionar_tarefa(titulo, descricao)
        case ['toumo', 'add', a]:
            try:
                qtd_tarefas = int(command.split()[2])
                for i in range(qtd_tarefas):
                    titulo = console.input('[magenta] ~ [/]')
                    if titulo == "exit":
                        console.print("[red]operação cancelada[/]")
                        break
                    descricao = input('    ')
                    if descricao == "exit":
                        console.print("[red]operação cancelada[/]")
                        break
                    adicionar_tarefa(titulo, descricao)
                    console.print(f"[cyan]--[/cyan] [white]tarefa '{titulo}' adcionada[/white] [cyan]--[/cyan]")
                
            except ValueError:
                console.print(
                    f"\n[red on white]{command}[/red on white]"
                    " [red]'ValueError'[/]\n'"
                    "é necessário digitar um valor inteiro após o comando 'add'"
                )
        case ['toumo', 'remove', 'i'] | ['toumo', 'rmi']:
            comma = console.input('[magenta] ~ [/]')
            remover_tarefa(comma)
        case ['exit']:
            break
