from WABI.templates import template, ThemeState
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
                    rx.vstack(
                        rx.center(rx.text("Daily Steps:",font_family='Helvetica Neue', style=[style1, style2, equal_style]), width='100%'),
                        rx.center(rx.text(f"{_steps} steps",font_family='Plus Jakarta Sans', weight='bold', style=[style1, style2, equal_style]), width='100%')
                    ),
                    **{"border_radius": "10px", "background_color": ThemeState.accent_color},
                    **equal_style,
                ),
                rx.box(
                    rx.vstack(
                        rx.center(rx.text("Distance Traveled:",font_family='Helvetica Neue', style=[style1, style2, equal_style]), width='100%'),
                        rx.center(rx.text(f"{_distance} miles",font_family='Plus Jakarta Sans', weight='bold', style=[style1, style2, equal_style]), width='100%')
                    ),
                    **{"border_radius": "10px", "background_color": ThemeState.accent_color},
                    **equal_style,
                ),
                rx.box(
                    rx.vstack(
                        rx.center(rx.text("Calories Burned:",font_family='Helvetica Neue', style=[style1, style2, equal_style]), width='100%'),
                        rx.center(rx.text(f'{_calories} calories',font_family='Plus Jakarta Sans', weight='bold', style=[style1, style2, equal_style]), width='100%')
                    ),
                    **{"border_radius": "10px", "background_color": ThemeState.accent_color},
                    **equal_style,
                ),
                spacing="9",  # Adjust the spacing as needed
                width="100%"
            ),
            width = "100%",  # Make the component stretch across the whole page
        ), width='100%', height='100vh'
    )
