import os
import sys
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from openai import OpenAI, completions

sys.path.insert(0, '/home/varvara_murashova/Lectures/lecture_llm_api/src')
from lecture_llm_api.settings import OpenAISettings
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

console = Console()

def get_client() -> OpenAI:
    settings = OpenAISettings()
    client = OpenAI(
        api_key=settings.openai_api_key.get_secret_value(),
        base_url=str(settings.openai_base_url),
    )
    return client

def responses_variant():
    client = get_client()

    completion = client.responses.create(
        model="qwen/qwen3-vl-30b-a3b-thinking",
        instructions="Ты русский православный батюшка матершинник, который составляет молитвы людям с кучей мата и эмодзи",
        input="Составь молитву, чтобы не ломался автобус от ДГТУ до Шаповалова",
    )

    print(completion.output_text)
    
    if (assistant_message := completion.choices[0].message.content):
        messages.append({"role": "assistant", "content": assistant_message})
    return assistant_message

messages = [
    {
        "role": "system",
        "content": "Ты русский православный батюшка матершинник, который составляет молитвы людям с кучей мата и брани, и эмодзи",
    },
]

def completions_variant():
    client = get_client()  

    completion = client.chat.completions.create(
        model="qwen/qwen3-vl-30b-a3b-thinking",
        messages=messages,
    )
    assistant_message = completion.choices[0].message.content if completion.choices else None

    if assistant_message:
        messages.append({"role": "assistant", "content": assistant_message})
    return assistant_message

def saint_chat():
    console.print(Panel(
        "[dark_goldenrod]Чем тебе помочь, сын Божий?[/dark_goldenrod]\n"
        "Команды:\n"
        "\n[indian_red]/exit[/indian_red] - выход"
        "\n[indian_red]/clear[/indian_red] - очистить историю"
        "\n[indian_red]/system text[/indian_red] - изменить системный (Что вы хотите поменять в Батюшке или вы хотите убрать Батюшку?)",
        title="Заходи в храм Божий и приобрети покой",
        border_style="gold3"
    ))

    while True:
        user_input = console.input("\n[deep_pink4]>>>[/deep_pink4] ").strip()

        if user_input == "/exit":
            console.print("[dark_red]Выход[/dark_red]")
            break

        elif user_input == "/clear":
            console.print("[turquoise4]Очистка[/turquoise4]")
            system_prompt = messages[0]
            messages.clear()
            messages.append(system_prompt)
            console.print("[turquoise4]История очищена[/turquoise4]")
            continue

        elif not user_input:
            continue

        elif user_input.startswith("/system"):
            new_prompt = user_input[8:].strip()
            if new_prompt:
                messages[0] = {"role": "system", "content": new_prompt}
                console.print(f"[green]Что мы изменим в Батюшке?:[/green] {new_prompt}")
            continue

        messages.append({"role": "user", "content": user_input})

        console.print("\n[bold cyan]Батюшка формулирует молитву специально для вас[/bold cyan]")
        response = completions_variant()

        if response:
            console.print(Panel(
                Markdown(response),
                title="[bold red]Ответ батюшки:[/bold red]",
                border_style="red"
            ))
        else:
            console.print(Panel(
                "[red]Ошибка: пустой ответ от модели[/red]",
                title="[bold red]Ответ батюшки:[/bold red]",
                border_style="red"
            ))

if __name__ == "__main__":
    saint_chat()
    # ЗАДАЧА:
    # сделать бесконечй цикл для диалога с моделью в одном чате с сохранением всего этого контекста
    # если пользователь вводит "/exit", то выйти из цикла
    # если вводит "/clear", то очистить историю, кроме system prompt
    # если вводит "/system какой-то текст", то всё что после /system - будет системный промптом
    # для задачи обязательно использовать rich console https://rich.readthedocs.io/en/latest/console.html
    # и panel для красоты https://rich.readthedocs.io/en/latest/panel.html
    # + форматирование через https://rich.readthedocs.io/en/latest/markdown.html
