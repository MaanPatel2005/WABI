"""The dashboard page."""

from WABI.templates import template

import reflex as rx
# import reflex_local_auth

@template(route="/dashboard", title="Dashboard")
# @reflex_local_auth.require_login
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Dashboard", size="8"),
        rx.text("Welcome to Reflex!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/dashboard.py"),
        ),
    )
