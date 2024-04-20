from WABI.templates import template, ThemeState
from WABI.components.dashboardComponents import challengeBox, challengeBodyBox, challengeSmallText, challengeTextBox, dashboardButton
import reflex as rx

style1 = {
    "color": "green",
    "font_family": "Helvetica",
}
style2 = {
    "color": "black",
    "padding": "10px",
}
equal_style = {
    "flex": "20%",  # Use flexbox to distribute the boxes evenly
    "padding": "10px",
    "box_sizing": "border-box",  # Ensure padding is included in the box size
}


_user_name = "Wabi"
_level = 10
_animal = "Jaguar"
_steps = 1000
_distance = 10
_calories = 800

def empty():
    pass


@template(route="/dashboard", title="Dashboard")
# @reflex_local_auth.require_login
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.center(
            rx.heading("Jungle Dashboard", size="8"),
            width="100%"
        ),
        rx.center(rx.avatar(src="/snake_head.png"), width='100%'),
        rx.center(rx.text(f"Explorer {_user_name}"), width='100%'),
        rx.center(rx.text(f"Lvl {_level} {_animal}"), width='100%'),
        rx.center(
            rx.hstack(
                dashboardButton('Daily Steps:', 'steps', ThemeState, flex = '20%'),
                dashboardButton('Distance Traveled:', 'miles', ThemeState, flex = '20%'),
                dashboardButton('Calories Burned:', 'calories', ThemeState, flex = '20%'),
                spacing="9",  # Adjust the spacing as needed
                width="100%"
            ),
            
            width = "100%",  # Make the component stretch across the whole page
        ),
        challengeBox(head='head', body='body but now it is very long so it has to wrap around and stuff', 
                     reward = 'reward', img='/github.svg',click_func = empty, ThemeState = ThemeState),
    width = '100%', height = '100vh'
    
    )
