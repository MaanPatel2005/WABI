from WABI.templates import template, ThemeState

import reflex as rx

style1 = {
    "color": "green",
    "font_family": "Helvetica",
    "border_radius": "10px",
    "background_color": ThemeState.accent_color,
}
style2 = {
    "color": "black",
    "padding": "10px",
}
equal_style = {
    "flex": "1",  # Use flexbox to distribute the boxes evenly
    "padding": "10px",
    "box_sizing": "border-box"  # Ensure padding is included in the box size
}

_user_name = "Wabi"
_level = 10
_animal = "Jaguar"
_steps = 1000
_distance = 10
_calories = 800

@template(route="/dashboard", title="Dashboard")
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
                rx.box(
                    rx.center(rx.text("Daily Steps:", style=[style1, style2, equal_style]), width='100%'),
                    equal_style,
                ),
                rx.box(
                    rx.center(rx.text(f"Distance Traveled: {_distance} miles", style=[style1, style2, equal_style]), width='100%'),
                    equal_style,
                ),
                rx.box(
                    rx.center(rx.text(f"Calories Burned: {_calories} calories", style=[style1, style2, equal_style]), width='100%'),
                    equal_style,
                ),
                spacing="9",  # Adjust the spacing as needed
                width="100%"
            ),
            width="100%",
        )
    )
