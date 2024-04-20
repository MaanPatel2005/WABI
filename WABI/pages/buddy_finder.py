from WABI import styles
from WABI.templates import template, ThemeState

import reflex as rx

@template(route="/buddy", title="Buddy Finder")
# @reflex_local_auth.require_login
def buddy_finder() -> rx.Component:
    
    return rx.center(
        rx.vstack(
        rx.center(
            rx.heading("Buddy Finder", size="8"),
            width="100%"
        ),
        rx.center(
            rx.heading("Upcoming Group Activities", size="6"),
            width="100%"
        ),
        rx.accordion.root(
            rx.accordion.item(
                header="Fanum Tax",
                content="Skibidi Ohio Rizz with Turkish Quandale Dingle",
                font_size="3em",
            ),
            rx.accordion.item(
                header="Second Item",
                content="The second accordion item's content",
                font_size="3em",
            ),
            rx.accordion.item(
                header="Third item",
                content="The third accordion item's content",
                font_size="3em",
            ),
            collapsible=True,
            width="300px",
            color_scheme = ThemeState.accent_color,
            orientation="horizontal",
        ),
        rx.spacer(),
        rx.spacer(),
        rx.center(
            rx.heading("Links", size="5"),
            width="100%"
        ),
        rx.spacer(),
        rx.link(
            rx.button("Chat With Your Groups"),
            href="/chat"
        ),
        rx.spacer(),
        rx.popover.root(
            rx.popover.trigger(
                rx.button("Create A Posting", variant="classic", style={"paddingRight": "50px"}),
            ),
            rx.popover.content(
                rx.inset(
                    side="top",
                    background="url('https://images.unsplash.com/photo-1570288685280-7802a8f8c4fa?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') center/cover",
                    height="100px",
                ),
                rx.box(
                    rx.text_area(
                        placeholder="Write Out An Activity Plan!",
                        style={"height": 80},
                    ),
                    rx.flex(
                        rx.popover.close(
                            rx.button("Share Activity", size="1")
                        ),
                        spacing="3",
                        margin_top="12px",
                        justify="between",
                    ),
                    padding_top="12px",
                ),
                style={"width": 360},
            ),
        )
        ),
        width= "100%"
    )