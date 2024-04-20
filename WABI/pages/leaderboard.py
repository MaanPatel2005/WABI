import reflex as rx
import asyncio
"""The home page of the app."""

from WABI import styles
from WABI.templates import template

import reflex as rx
# import reflex_local_auth

class SoundEffectStateMonkey(rx.State):
    @rx.background
    async def delayed_play(self):
        await asyncio.sleep(1)
        return rx.call_script("playFromStart(button_sfx1)")
    
class SoundEffectStateDolphin(rx.State):
    @rx.background
    async def delayed_play(self):
        await asyncio.sleep(1)
        return rx.call_script("playFromStart(button_sfx2)")

class SoundEffectStateLion(rx.State):
    @rx.background
    async def delayed_play(self):
        await asyncio.sleep(1)
        return rx.call_script("playFromStart(button_sfx3)")

def sound_effect_monkey():
    return rx.hstack(
        rx.script(
            """
            var button_sfx1 = new Audio("/monkey_noises.mp3")
            function playFromStart (sfx1) {sfx1.load(); sfx1.play()}
            """
        ),
        rx.button(
            "Monkey Noises",
            on_click=SoundEffectStateMonkey.delayed_play,
        ),
    )


def sound_effect_dolphin():
    return rx.hstack(
        rx.script(
            """
            var button_sfx2 = new Audio("/dolphin_noises.mp3")
            function playFromStart (sfx2) {sfx2.load(); sfx2.play()}
            """
        ),
        rx.button(
            "Dolphin Noises",
            on_click=SoundEffectStateDolphin.delayed_play,
        ),
    )


def sound_effect_lion():
    return rx.hstack(
        rx.script(
            """
            var button_sfx3 = new Audio("/lion_noises.mp3")
            function playFromStart (sfx3) {sfx3.load(); sfx3.play()}
            """
        ),
        rx.button(
            "Lion Noises",
            on_click=SoundEffectStateLion.delayed_play,
        ),
    )

@template(route="/leaderboard", title="Leaderboard")

def leaderboard() -> rx.Component:
    
    return rx.center(
    rx.heading("Leaderboard"),
    rx.center(
    rx.flex(
    rx.table.root(
        rx.table.header(
        rx.table.row(
            rx.table.column_header_cell(""),
            rx.table.column_header_cell(""),
            rx.table.column_header_cell("Full Name"),
            rx.spacer(),
            rx.table.column_header_cell("Points"),
        ),
        ),
        rx.table.body(
            rx.table.row(
                rx.table.cell(rx.text("1.")),
                rx.table.cell(rx.avatar(fallback="PP"), style={"paddingRight": "125px"}),
                rx.table.row_header_cell(
                    rx.link("Purav Patel"),    
                    style={"paddingRight": "125px"}
                ),
                rx.spacer(),
                rx.table.cell("Points: 1000"),
                align="center",
            ),
            rx.table.row(
                rx.table.cell(rx.text("2.")),
                rx.table.cell(rx.avatar(fallback="DP"), style={"paddingRight": "125px"}),
                rx.table.row_header_cell(
                    rx.link("Dhruv Patel"),
                    style={"paddingRight": "125px"}
                ),
                rx.spacer(),
                rx.table.cell("Points: 800"),
                align="center",
            ),
            rx.table.row(
                rx.table.cell(rx.text("3.")),
                rx.table.cell(rx.avatar(fallback="MP"), style={"paddingRight": "125px"}),
                rx.table.row_header_cell(
                    rx.link("Maan Patel"),
                    style={"paddingRight": "125px"}
                ),
                rx.spacer(),
                rx.table.cell("Points: 700"),
                align="center",
            ),
        ),
    ),
    width = "100%"
    ),
    
    ),
    rx.center(
        rx.text("Interact to hear the roars and calls!")
    ),
    rx.center(
    rx.hstack(
        sound_effect_monkey(),
        sound_effect_dolphin(),
        sound_effect_lion(),
        ),
    ),
    
    direction="column",
    spacing="6",
    width="100%"
)


