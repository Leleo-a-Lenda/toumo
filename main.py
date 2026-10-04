from system import (
    concluir_tarefa,
    listar_tarefas,
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
            qtd_tarefas = int(command.split()[2])
            for i in range(qtd_tarefas):
                print('eai')
        case ['exit']:
            break
