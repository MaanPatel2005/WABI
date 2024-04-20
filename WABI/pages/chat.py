from WABI import styles
from WABI.templates import template

import reflex as rx
from reflex_chat import chat

async def test_func(): return True


@template(route="/chat", title="Chat")
def index() -> rx.Component:
    return rx.container(
        rx.box(
            chat(process=test_func()),
            height="100vh",
        ),
        size="2",
    )
