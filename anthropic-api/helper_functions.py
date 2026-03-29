from dotenv import load_dotenv
from anthropic import Anthropic
from anthropic.types import MessageParam
from typing import Any, cast


load_dotenv()
client = Anthropic()
DEFAULT_MODEL = "claude-sonnet-4-0"


def add_user_message(messages: list[MessageParam], text: str) -> None:
    user_message = cast(MessageParam, {
        "role": "user",
        "content": text
    })
    messages.append(user_message)


def add_assistant_message(messages: list[MessageParam], text: str) -> None:
    assistant_message = cast(MessageParam, {
        "role": "assistant",
        "content": text
    })
    messages.append(assistant_message)


def chat(
    messages: list[MessageParam],
    max_tokens: int = 1000,
    model: str = DEFAULT_MODEL,
    temperature: float = 0.6,
    system: str | None = None,
    stop_sequences: list[str] | None = None,
) -> str:
    params = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": messages,
        "temperature": temperature,
    }
    if system is not None:
        params["system"] = system
    if stop_sequences is not None:
        params["stop_sequences"] = stop_sequences
    try:
        # ** means to unpack the params dict into keyword arguments
        message = client.messages.create(**params)

        first_block: Any = message.content[0]
        return str(getattr(first_block, "text", ""))

    except Exception as exc:
        raise RuntimeError(f"Anthropic request failed: {exc}") from exc
