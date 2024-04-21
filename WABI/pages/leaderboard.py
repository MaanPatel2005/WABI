import reflex as rx
import asyncio
"""The home page of the app."""

from WABI import styles
from WABI.templates import template

import reflex as rx
from firebase_admin import firestore
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

def get_initials(name: str):
    my_str = name.split()
    return my_str[0][0] + my_str[1][0]

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


def fetch_top_three():
    db = firestore.client()
    users_ref = db.collection('users')
    query = users_ref.order_by('point', direction=firestore.Query.DESCENDING).limit(3)
    results = query.stream()
    return (result.to_dict() for result in results)


@template(route="/leaderboard", title="Leaderboard")

def leaderboard() -> rx.Component:
    first, second, third = fetch_top_three()
    
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
                rx.table.cell(rx.avatar(fallback=get_initials(first['name'])), style={"paddingRight": "125px"}),
                rx.table.row_header_cell(
                    rx.link(first['name']),    
                    style={"paddingRight": "125px"}
                ),
                rx.spacer(),
                rx.table.cell(f"Points: {first['point']}"),
                align="center",
            ),
            rx.table.row(
                rx.table.cell(rx.text("2.")),
                rx.table.cell(rx.avatar(fallback=get_initials(second['name'])), style={"paddingRight": "125px"}),
                rx.table.row_header_cell(
                    rx.link(second['name']),
                    style={"paddingRight": "125px"}
                ),
                rx.spacer(),
                rx.table.cell(f"Points: {second['point']}"),
                align="center",
            ),
            rx.table.row(
                rx.table.cell(rx.text("3.")),
                rx.table.cell(rx.avatar(fallback=get_initials(third['name'])), style={"paddingRight": "125px"}),
                rx.table.row_header_cell(
                    rx.link(third['name']),
                    style={"paddingRight": "125px"}
                ),
                rx.spacer(),
                rx.table.cell(f"Points: {third['point']}"),
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


