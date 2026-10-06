from system import (
    concluir_tarefa,
    adicionar_tarefa,
    remover_tarefa,
    carregar_tarefas,
    nome_tarefa
)
from tui import (
    logo_intro,
    help_dialog,
    listq
)
from rich import print
from rich.panel import Panel
from rich.console import Console
import readline

console = Console()
readline.set_history_length(1000)

MAGENTA = "\001\033[35m\002"
RESET = "\001\033[0m\002"


def ler_texto(prompt=""):
    return input(prompt)


PROMPT_COMANDO = f"{MAGENTA}> {RESET}"
PROMPT_TEXTO = f"{MAGENTA} ~ {RESET}"

print(logo_intro())
print(help_dialog())

while True:    
    command = ler_texto(PROMPT_COMANDO)
    match command.split():
        case ['toumo', 'list'] | ['toumo', 'l']:
            listq()
        case ['toumo', 'add']:
            titulo = ler_texto(PROMPT_TEXTO)
            if titulo == "exit":
                console.print("[red]operação cancelada[/]")
                break
            descricao = ler_texto('    ')
            if descricao == "exit":
                console.print("[red]operação cancelada[/]")
                break
            adicionar_tarefa(titulo, descricao)
            console.print(f"[cyan]--[/cyan] [white]tarefa '{titulo}' adcionada[/white] [cyan]--[/cyan]")
        case ['toumo', 'add', a]:
            try:
                qtd_tarefas = int(command.split()[2])
                for i in range(qtd_tarefas):
                    titulo = ler_texto(PROMPT_TEXTO)
                    if titulo == "exit":
                        console.print("[red]operação cancelada[/]")
                        break
                    descricao = ler_texto('    ')
                    if descricao == "exit":
                        console.print("[red]operação cancelada[/]")
                        break
                    adicionar_tarefa(titulo, descricao)
                    console.print(f"[cyan]--[/cyan] [white]tarefa '{titulo}' adcionada[/white] [cyan]--[/cyan]")
                
            except ValueError:
                console.print(
                    f"\n[red]{command}[/red]"
                    " [red]'ValueError'[/]\n'"
                    "é necessário digitar um valor inteiro após o comando 'add'"
                )
        case ['toumo', 'remove', 'i'] | ['toumo', 'rmi']:
            comma = ler_texto(PROMPT_TEXTO)
            try:
                if not nome_tarefa(comma):
                    console.print(
                        f"\n[red]{comma}[/red]"
                        " [red]'ValueError'[/]\n'"
                        "é necessário que o indice selecionado seja um valor inteiro"
                    )
                    break
                console.print(f"você quer excluir '{nome_tarefa(comma)}'? (y/yes or n/no)")
                c = ler_texto(PROMPT_TEXTO)
                if c == 'n' or c == 'no':
                    break
                console.print(remover_tarefa(comma))
            except IndexError:
                console.print(f"[red]'IndexError'[/red] a tarefa não foi encontrada")
        case ['exit']:
            break
