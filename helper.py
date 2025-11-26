
from datetime import datetime
from typing import Callable, List, Dict, Any, Optional, Callable, Union, get_args, get_origin
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

def debug_print(enabled: bool, *lines: str, **options: dict) -> None:
    if not enabled:
        return

    time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = "\n".join(map(str, lines))

    box_color = options.get("color", "white")
    box_title = options.get("title", "")

    log_text = f"[{time_str}]\n{content}"

    print_in_box(log_text, color=box_color, title=box_title)

    file_path = options.get("log_path", None)
    if file_path:
        with open(file_path, 'a') as file:
            file.write(log_text + '\n')


def print_in_box(
    content: str,
    output_console: Optional[Console] = None,
    box_title: str = "",
    border_color: str = "white"
) -> None:
    """
    Print the content inside a styled box-like structure.

    :param content: The text to display inside the box.
    :param output_console: Optional rich Console instance.
    :param box_title: The title displayed above the box.
    :param border_color: The color used for the title styling.
    """
    output_console = output_console or Console()

    header = "_" * 20 + box_title + "_" * 20
    output_console.print(header, style=f"bold {border_color}")
    output_console.print(content, highlight=True, emoji=True)

    

def ask_text(
    question: str,
    panel_title: str = "User",
    output_console: Optional[Console] = None,
    default_response: str = ""
) -> str:
    """
    Display a question in a panel and prompt the user for an answer.
    
    :param question: The question displayed to the user.
    :param panel_title: The title shown on the panel.
    :param output_console: Optional rich Console instance.
    :param default_response: Value used if user just presses Enter.
    :return: The text entered by the user.
    """
    output_console = output_console or Console()

    output_console.print(Panel(question, title=panel_title, border_style="green"))
    user_input = Prompt.ask(
        "Type your answer here (press Enter to accept default)",
        default=default_response
    )
    output_console.print(Panel(user_input, title=panel_title))

    return user_input



def debug_print_swarm(enabled: bool, *messages: str) -> None:
    if not enabled:
        return

    time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    combined_text = " ".join(map(str, messages))

    print(
        f"\033[97m[\033[90m{time_str}\033[97m]"
        f"\033[90m {combined_text}\033[0m"
    )





